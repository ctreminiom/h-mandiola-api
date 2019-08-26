package product

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

type productType struct{ ID, Name string }

func (c *productType) gets() ([]productType, error) {

	db := service.Pool()

	rows, err := db.Query(service.GetProductTypes)

	if err != nil {
		return nil, err
	}

	types := []productType{}

	for rows.Next() {

		var r productType

		err = rows.Scan(&r.ID, &r.Name)

		if err != nil {
			return nil, err
		}

		types = append(types, r)
	}

	return decodesType(types), nil
}

func (c *productType) insert() error {

	db := service.Pool()
	tx, err := db.Begin()

	if err != nil {
		tx.Rollback()
		return err
	}

	var id string
	err = tx.QueryRow(service.NextIDProductType).Scan(&id)

	if err != nil {
		tx.Rollback()
		return err
	}

	query := fmt.Sprintf(service.InsertProductType, service.Encrypt(id), service.Encrypt(c.Name))

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
	entry.Detail = fmt.Sprintf("Table: %v | ID: %v", "dbo.products_types", service.Encrypt(id))

	err = entry.Insert()

	if err != nil {
		return err
	}

	return nil
}

func decodesType(r []productType) []productType {

	var result []productType

	for _, row := range r {
		result = append(result, decodeType(row))
	}

	return result
}

func decodeType(r productType) productType {
	return productType{ID: service.Decrypt(r.ID), Name: service.Decrypt(r.Name)}
}

type productPayload struct {
	Consecutive string `json:"consecutive" binding:"required"`
	Type        string `json:"type" binding:"required"`
	Name        string `json:"name" binding:"required"`
}

type product struct{ ID, Consecutive, Type, Name string }

func (c *product) gets() ([]product, error) {

	db := service.Pool()

	rows, err := db.Query(service.GetProducts)

	if err != nil {
		return nil, err
	}

	products := []product{}

	for rows.Next() {

		var r product

		err = rows.Scan(&r.ID, &r.Consecutive, &r.Type, &r.Name)

		if err != nil {
			return nil, err
		}

		products = append(products, r)
	}

	return decodesproduct(products), nil
}

func (c *product) insert() error {

	db := service.Pool()
	tx, err := db.Begin()

	if err != nil {
		tx.Rollback()
		return err
	}

	var id string
	err = tx.QueryRow(service.NextIDProduct).Scan(&id)

	if err != nil {
		tx.Rollback()
		return err
	}

	query := fmt.Sprintf(service.InsertProduct, service.Encrypt(id), service.Encrypt(c.Consecutive),
		service.Encrypt(c.Type),
		service.Encrypt(c.Name))

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
	entry.Detail = fmt.Sprintf("Table: %v | ID: %v", "dbo.products", service.Encrypt(id))

	err = entry.Insert()

	if err != nil {
		return err
	}

	return nil
}

func (c *product) delete() error {

	db := service.Pool()
	tx, err := db.Begin()

	if err != nil {
		tx.Rollback()
		return err
	}

	query := fmt.Sprintf(service.RemoveProduct, service.Encrypt(c.ID))

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
	entry.Detail = fmt.Sprintf("Table: %v | ID: %v", "dbo.products", service.Encrypt(c.ID))

	err = entry.Insert()

	if err != nil {
		return err
	}

	return nil
}

func decodesproduct(r []product) []product {

	var result []product

	for _, row := range r {
		result = append(result, decodeproduct(row))
	}

	return result
}

func decodeproduct(r product) product {
	return product{ID: service.Decrypt(r.ID), Consecutive: service.Decrypt(r.Consecutive),
		Type: service.Decrypt(r.Type),
		Name: service.Decrypt(r.Name)}
}
