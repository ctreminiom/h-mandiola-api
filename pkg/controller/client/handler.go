package client

import (
	"fmt"
	"time"

	errorm "github.com/ctreminiom/h-mandiola-api/pkg/controller/error"
	"github.com/ctreminiom/h-mandiola-api/pkg/controller/log"
	"github.com/ctreminiom/h-mandiola-api/pkg/service"
)

type payload struct {
	Consecutive string `json:"consecutive"`
	First       string `json:"first"`
	Last        string `json:"last"`
	Username    string `json:"username" binding:"required"`
	Email       string `json:"email" binding:"required"`
	Sub         string `json:"sub" binding:"required"`
	Aud         string `json:"aud" binding:"required"`
}

type client struct{ ID, Consecutive, First, Last, Username, Email, Sub, Aud string }

func (c *client) gets() ([]client, error) {

	db := service.Pool()

	rows, err := db.Query(service.GetClients)

	if err != nil {
		return nil, err
	}

	clients := []client{}

	for rows.Next() {

		var r client

		err = rows.Scan(&r.ID, &r.Consecutive, &r.First, &r.Last, &r.Username, &r.Email, &r.Sub, &r.Aud)

		if err != nil {
			return nil, err
		}

		clients = append(clients, r)
	}

	return decodes(clients), nil
}

func (c *client) insert() error {

	db := service.Pool()
	tx, err := db.Begin()

	if err != nil {
		tx.Rollback()
		return err
	}

	var id string
	err = tx.QueryRow(service.NextIDClients).Scan(&id)

	if err != nil {
		tx.Rollback()
		return err
	}

	query := fmt.Sprintf(service.InsertClient, service.Encrypt(id), service.Encrypt(c.Consecutive),
		service.Encrypt(c.First),
		service.Encrypt(c.Last),
		service.Encrypt(c.Username),
		service.Encrypt(c.Email),
		service.Encrypt(c.Sub),
		service.Encrypt(c.Aud))

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
	entry.Detail = fmt.Sprintf("Table: %v | ID: %v", "dbo.clients", service.Encrypt(id))

	err = entry.Insert()

	if err != nil {
		return err
	}

	return nil
}

func decodes(r []client) []client {

	var result []client

	for _, row := range r {
		result = append(result, decode(row))
	}

	return result
}

func decode(r client) client {
	return client{ID: service.Decrypt(r.ID), Consecutive: service.Decrypt(r.Consecutive),
		First:    service.Decrypt(r.First),
		Last:     service.Decrypt(r.Last),
		Username: service.Decrypt(r.Username),
		Email:    service.Decrypt(r.Email),
		Sub:      service.Decrypt(r.Sub),
		Aud:      service.Decrypt(r.Aud)}
}
