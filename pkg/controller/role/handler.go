package role

import (
	"fmt"
	"time"

	errorm "github.com/ctreminiom/h-mandiola-api/pkg/controller/error"
	"github.com/ctreminiom/h-mandiola-api/pkg/controller/log"
	"github.com/ctreminiom/h-mandiola-api/pkg/service"
)

type payload struct {
	Name string `json:"name" binding:"required"`
}

type role struct{ ID, Name string }

func (r *role) gets() ([]role, error) {

	db := service.Pool()

	rows, err := db.Query(service.GetRoles)

	if err != nil {
		return nil, err
	}

	roles := []role{}

	for rows.Next() {

		var r role

		err = rows.Scan(&r.ID, &r.Name)

		if err != nil {
			return nil, err
		}

		roles = append(roles, r)
	}

	return decodes(roles), nil
}

func (r *role) insert() error {

	db := service.Pool()
	tx, err := db.Begin()

	if err != nil {
		tx.Rollback()
		return err
	}

	var id string
	err = tx.QueryRow(service.NextIDRole).Scan(&id)

	if err != nil {
		tx.Rollback()
		return err
	}

	query := fmt.Sprintf(service.InsertRole, service.Encrypt(id), service.Encrypt(r.Name))

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

func decodes(r []role) []role {

	var result []role

	for _, row := range r {
		result = append(result, decode(row))
	}

	return result
}

func decode(r role) role {
	return role{ID: service.Decrypt(r.ID), Name: service.Decrypt(r.Name)}
}
