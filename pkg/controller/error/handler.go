package errorm

import (
	"fmt"

	"github.com/ctreminiom/h-mandiola-api/pkg/service"
)

// Error ...
type Error struct{ ID, Username, Date, Detail string }

func (e *Error) gets() ([]Error, error) {

	db := service.Pool()

	rows, err := db.Query(service.GetErrors)

	if err != nil {
		return nil, err
	}

	errorn := []Error{}

	for rows.Next() {

		var e Error

		err = rows.Scan(&e.ID, &e.Username, &e.Date, &e.Detail)

		if err != nil {
			return nil, err
		}

		errorn = append(errorn, e)
	}

	return decodes(errorn), nil
}

// Insert ..
func (e *Error) Insert() error {

	db := service.Pool()
	tx, err := db.Begin()

	if err != nil {
		tx.Rollback()
		return err
	}

	var id string
	err = tx.QueryRow(service.NextIDError).Scan(&id)

	if err != nil {
		tx.Rollback()
		return err
	}

	query := fmt.Sprintf(service.InsertError, service.Encrypt(id),
		service.Encrypt(e.Username),
		service.Encrypt(e.Date),
		service.Encrypt(e.Detail))

	_, err = tx.Exec(query)

	if err != nil {
		tx.Rollback()
		return err
	}

	tx.Commit()

	return nil
}

func decodes(r []Error) []Error {

	var result []Error

	for _, row := range r {
		result = append(result, decode(row))
	}

	return result
}

func decode(l Error) Error {
	return Error{ID: service.Decrypt(l.ID), Username: service.Decrypt(l.Username),
		Date:   service.Decrypt(l.Date),
		Detail: service.Decrypt(l.Detail)}
}
