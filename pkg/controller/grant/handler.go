package grant

import (
	"fmt"
	"time"

	errorm "github.com/ctreminiom/h-mandiola-api/pkg/controller/error"
	"github.com/ctreminiom/h-mandiola-api/pkg/controller/log"
	"github.com/ctreminiom/h-mandiola-api/pkg/service"
)

type payload struct {
	Username string `json:"username"`
	Role     string `json:"role"`
}

type grant struct{ ID, User, Role string }
type user struct{ ID, Username, Email, Password, Question, Answer string }

func (g *grant) get(username string) ([]grant, error) {

	db := service.Pool()

	query := fmt.Sprintf(service.GetGrant, service.Encrypt(username))

	rows, err := db.Query(query)

	if err != nil {
		return nil, err
	}

	grants := []grant{}

	for rows.Next() {

		var g grant

		err = rows.Scan(&g.ID, &g.User, &g.Role)

		if err != nil {
			return nil, err
		}

		grants = append(grants, g)
	}

	return decodes(grants), nil
}

func (g *grant) delete() error {

	db := service.Pool()
	tx, err := db.Begin()

	if err != nil {
		tx.Rollback()
		return err
	}

	//Get userID
	query := fmt.Sprintf(service.GetUser, service.Encrypt(g.User))

	var r user
	err = tx.QueryRow(query).Scan(&r.ID, &r.Username, &r.Password, &r.Email, &r.Question)

	if err != nil {
		return err
	}

	query = fmt.Sprintf(service.RemoveGrant, r.ID, service.Encrypt(g.Role))

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
	entry.Detail = fmt.Sprintf("Table: %v | Grant deleted: %v", "dbo.grants", service.Encrypt(g.Role))

	err = entry.Insert()

	if err != nil {
		return err
	}

	return nil

}

func (g *grant) insert() error {

	db := service.Pool()
	tx, err := db.Begin()

	if err != nil {
		tx.Rollback()
		return err
	}

	var id string
	err = tx.QueryRow(service.NextIDGrants).Scan(&id)

	if err != nil {
		tx.Rollback()
		return err
	}

	//Get userID
	query := fmt.Sprintf(service.GetUser, service.Encrypt(g.User))

	var r user
	err = tx.QueryRow(query).Scan(&r.ID, &r.Username, &r.Password, &r.Email, &r.Question)

	if err != nil {
		return err
	}

	query = fmt.Sprintf(service.InsertGrant, service.Encrypt(id), r.ID, service.Encrypt(g.Role))

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
	entry.Detail = fmt.Sprintf("Table: %v | ID: %v", "dbo.grants", service.Encrypt(id))

	err = entry.Insert()

	if err != nil {
		return err
	}

	return nil
}

func decodes(r []grant) []grant {

	var result []grant

	for _, row := range r {
		result = append(result, decode(row))
	}

	return result
}

func decode(r grant) grant {
	return grant{ID: service.Decrypt(r.ID), User: service.Decrypt(r.User), Role: service.Decrypt(r.Role)}
}
