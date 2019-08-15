package user

import (
	"errors"
	"fmt"
	"time"

	errorm "github.com/ctreminiom/h-mandiola-api/pkg/controller/error"
	"github.com/ctreminiom/h-mandiola-api/pkg/controller/log"
	"github.com/ctreminiom/h-mandiola-api/pkg/service"
)

type payload struct {
	Username string `json:"username" binding:"required"`
	Email    string `json:"email" binding:"required"`
	Password string `json:"password" binding:"required"`
	Question string `json:"question" binding:"required"`
	Answer   string `json:"answer" binding:"required"`
}

type payloadPass struct {
	Password string `json:"password" binding:"required"`
}

type payloadLogin struct {
	Username string `json:"username" binding:"required"`
	Password string `json:"password" binding:"required"`
}

type user struct{ ID, Username, Email, Password, Question, Answer string }

func (u *user) delete() error {

	db := service.Pool()
	tx, err := db.Begin()

	if err != nil {
		tx.Rollback()
		return err
	}

	query := fmt.Sprintf(service.DeleteUser, service.Encrypt(u.Username))

	_, err = tx.Exec(query)

	if err != nil {
		tx.Rollback()

		entry := errorm.Error{}
		entry.Username = "internal"
		entry.Date = time.Now().Format("2006-01-02 15:04:05")
		entry.Detail = err.Error()

		errInsert := entry.Insert()

		if errInsert != nil {
			return errInsert
		}

		return err
	}

	tx.Commit()

	entry := log.Log{}
	entry.Username = "internal"
	entry.Date = time.Now().Format("2006-01-02 15:04:05")
	entry.Code = "DELETE"
	entry.Detail = fmt.Sprintf("Table: %v | Username deleted: %v", "dbo.users", service.Encrypt(u.Username))

	err = entry.Insert()

	if err != nil {
		return err
	}

	return nil
}

func (u *user) login() (string, error) {

	db := service.Pool()
	tx, err := db.Begin()

	if err != nil {
		tx.Rollback()
		return "", err
	}

	query := fmt.Sprintf(service.GetUser, service.Encrypt(u.Username))

	var r user
	err = tx.QueryRow(query).Scan(&r.ID, &r.Username, &r.Password, &r.Email, &r.Question)

	if err != nil {
		return "", err
	}

	if service.Encrypt(u.Password) != r.Password {
		return "", errors.New("Incorrect username or password")
	}

	token, err := service.EncodeToken(u.Username)

	if err != nil {
		return "", err
	}

	return token, nil
}

func (u *user) gets() ([]user, error) {

	db := service.Pool()

	rows, err := db.Query(service.GetUsers)

	if err != nil {
		return nil, err
	}

	users := []user{}

	for rows.Next() {

		var r user

		err = rows.Scan(&r.ID, &r.Username, &r.Email, &r.Question)

		if err != nil {
			return nil, err
		}

		users = append(users, r)
	}

	return decodes(users), nil
}

func (u *user) password() error {

	db := service.Pool()
	tx, err := db.Begin()

	if err != nil {
		tx.Rollback()
		return err
	}

	query := fmt.Sprintf(service.UpdatePassword, service.Encrypt(u.Username), service.Encrypt(u.Password))

	_, err = tx.Exec(query)

	if err != nil {
		tx.Rollback()

		entry := errorm.Error{}
		entry.Username = "internal"
		entry.Date = time.Now().Format("2006-01-02 15:04:05")
		entry.Detail = err.Error()

		errInsert := entry.Insert()

		if errInsert != nil {
			return errInsert
		}

		return err
	}

	tx.Commit()

	entry := log.Log{}
	entry.Username = "internal"
	entry.Date = time.Now().Format("2006-01-02 15:04:05")
	entry.Code = "UPDATE"
	entry.Detail = fmt.Sprintf("Table: %v | Username updated: %v", "dbo.users", service.Encrypt(u.Username))

	err = entry.Insert()

	if err != nil {
		return err
	}

	return nil
}

func (u *user) insert() error {

	db := service.Pool()
	tx, err := db.Begin()

	if err != nil {
		tx.Rollback()
		return err
	}

	var id string
	err = tx.QueryRow(service.NextIDUser).Scan(&id)

	if err != nil {
		tx.Rollback()
		return err
	}

	query := fmt.Sprintf(service.InsertUser, service.Encrypt(id),
		service.Encrypt(u.Username),
		service.Encrypt(u.Email),
		service.Encrypt(u.Password),
		service.Encrypt(u.Question),
		service.Encrypt(u.Answer))

	_, err = tx.Exec(query)

	if err != nil {
		tx.Rollback()

		entry := errorm.Error{}
		entry.Username = "internal"
		entry.Date = time.Now().Format("2006-01-02 15:04:05")
		entry.Detail = err.Error()

		errInsert := entry.Insert()

		if errInsert != nil {
			return errInsert
		}

		return err
	}

	tx.Commit()

	entry := log.Log{}
	entry.Username = "internal"
	entry.Date = time.Now().Format("2006-01-02 15:04:05")
	entry.Code = "INSERT"
	entry.Detail = fmt.Sprintf("Table: %v | ID: %v", "dbo.users", service.Encrypt(id))

	err = entry.Insert()

	if err != nil {
		return err
	}

	return nil
}

func decodes(r []user) []user {

	var result []user

	for _, row := range r {
		result = append(result, decode(row))
	}

	return result
}

func decode(r user) user {
	return user{ID: service.Decrypt(r.ID), Username: service.Decrypt(r.Username),
		Email:    service.Decrypt(r.Email),
		Question: service.Decrypt(r.Question)}
}
