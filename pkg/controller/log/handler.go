package log

import (
	"fmt"

	"github.com/ctreminiom/h-mandiola-api/pkg/service"
)

// Log ...
type Log struct{ ID, Username, Date, Code, Detail string }

func (l *Log) gets() ([]Log, error) {

	db := service.Pool()

	rows, err := db.Query(service.GetLogs)

	if err != nil {
		return nil, err
	}

	logs := []Log{}

	for rows.Next() {

		var l Log

		err = rows.Scan(&l.ID, &l.Username, &l.Date, &l.Code, &l.Detail)

		if err != nil {
			return nil, err
		}

		logs = append(logs, l)
	}

	return decodes(logs), nil
}

// Insert ..
func (l *Log) Insert() error {

	db := service.Pool()
	tx, err := db.Begin()

	if err != nil {
		tx.Rollback()
		return err
	}

	var id string
	err = tx.QueryRow(service.NextIDLog).Scan(&id)

	if err != nil {
		tx.Rollback()
		return err
	}

	query := fmt.Sprintf(service.InsertLog, service.Encrypt(id),
		service.Encrypt(l.Username),
		service.Encrypt(l.Date),
		service.Encrypt(l.Code),
		service.Encrypt(l.Detail))

	_, err = tx.Exec(query)

	if err != nil {
		tx.Rollback()
		return err
	}

	tx.Commit()

	return nil
}

func decodes(r []Log) []Log {

	var result []Log

	for _, row := range r {
		result = append(result, decode(row))
	}

	return result
}

func decode(l Log) Log {
	return Log{ID: service.Decrypt(l.ID), Username: service.Decrypt(l.Username),
		Date:   service.Decrypt(l.Date),
		Code:   service.Decrypt(l.Code),
		Detail: service.Decrypt(l.Detail)}
}
