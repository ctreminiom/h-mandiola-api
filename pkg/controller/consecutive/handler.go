package consecutive

import (
	"fmt"
	"time"

	errorm "github.com/ctreminiom/h-mandiola-api/pkg/controller/error"
	"github.com/ctreminiom/h-mandiola-api/pkg/controller/log"
	"github.com/ctreminiom/h-mandiola-api/pkg/service"
)

type typePayload struct {
	Name string `json:"name" binding:"required"`
}

type consecutiveType struct{ ID, Name string }

func (c *consecutiveType) gets() ([]consecutiveType, error) {

	db := service.Pool()

	rows, err := db.Query(service.GetTypes)

	if err != nil {
		return nil, err
	}

	types := []consecutiveType{}

	for rows.Next() {

		var r consecutiveType

		err = rows.Scan(&r.ID, &r.Name)

		if err != nil {
			return nil, err
		}

		types = append(types, r)
	}

	return decodesType(types), nil
}

func (c *consecutiveType) insert() error {

	db := service.Pool()
	tx, err := db.Begin()

	if err != nil {
		tx.Rollback()
		return err
	}

	var id string
	err = tx.QueryRow(service.NextIDType).Scan(&id)

	if err != nil {
		tx.Rollback()
		return err
	}

	query := fmt.Sprintf(service.InsertType, service.Encrypt(id), service.Encrypt(c.Name))

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
	entry.Detail = fmt.Sprintf("Table: %v | ID: %v", "dbo.consecutive_types", service.Encrypt(id))

	err = entry.Insert()

	if err != nil {
		return err
	}

	return nil
}

func decodesType(r []consecutiveType) []consecutiveType {

	var result []consecutiveType

	for _, row := range r {
		result = append(result, decodeType(row))
	}

	return result
}

func decodeType(r consecutiveType) consecutiveType {
	return consecutiveType{ID: service.Decrypt(r.ID), Name: service.Decrypt(r.Name)}
}

type consecutivePayload struct {
	Type        string `json:"type" binding:"required"`
	Description string `json:"description" binding:"required"`
	HasPrefix   string `json:"hasPrefix" binding:"required"`
	Prefix      string `json:"prefix"`
	HasRange    string `json:"hasRange" binding:"required"`
	Initial     string `json:"initial"`
	Final       string `json:"final"`
}

type consecutive struct{ ID, Type, Description, HasPrefix, Prefix, HasRange, Initial, Final string }

func (c *consecutive) gets() ([]consecutive, error) {

	db := service.Pool()

	rows, err := db.Query(service.GetConsecutives)

	if err != nil {
		return nil, err
	}

	consecutives := []consecutive{}

	for rows.Next() {

		var r consecutive

		err = rows.Scan(&r.ID, &r.Type, &r.Description, &r.HasPrefix, &r.Prefix, &r.HasRange, &r.Initial, &r.Final)

		if err != nil {
			return nil, err
		}

		consecutives = append(consecutives, r)
	}

	return decodesConsecutive(consecutives), nil
}

func (c *consecutive) insert() error {

	db := service.Pool()
	tx, err := db.Begin()

	if err != nil {
		tx.Rollback()
		return err
	}

	var id string
	err = tx.QueryRow(service.NextIDConsecutive).Scan(&id)

	if err != nil {
		tx.Rollback()
		return err
	}

	query := fmt.Sprintf(service.InsertConsecutive, service.Encrypt(id), service.Encrypt(c.Type),
		service.Encrypt(c.Description),
		service.Encrypt(c.HasPrefix),
		service.Encrypt(c.Prefix),
		service.Encrypt(c.HasRange),
		service.Encrypt(c.Initial),
		service.Encrypt(c.Final))

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
	entry.Detail = fmt.Sprintf("Table: %v | ID: %v", "dbo.consecutives", service.Encrypt(id))

	err = entry.Insert()

	if err != nil {
		return err
	}

	return nil
}

func decodesConsecutive(r []consecutive) []consecutive {

	var result []consecutive

	for _, row := range r {
		result = append(result, decodeConsecutive(row))
	}

	return result
}

func decodeConsecutive(r consecutive) consecutive {
	return consecutive{ID: service.Decrypt(r.ID), Type: service.Decrypt(r.Type),
		Description: service.Decrypt(r.Description),
		HasPrefix:   service.Decrypt(r.HasPrefix),
		Prefix:      service.Decrypt(r.Prefix),
		HasRange:    service.Decrypt(r.HasRange),
		Initial:     service.Decrypt(r.Initial),
		Final:       service.Decrypt(r.Final)}
}
