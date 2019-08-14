package activity

import (
	"fmt"
	"time"

	errorm "github.com/ctreminiom/h-mandiola-api/pkg/controller/error"
	"github.com/ctreminiom/h-mandiola-api/pkg/controller/log"
	"github.com/ctreminiom/h-mandiola-api/pkg/service"
)

type payload struct {
	Consecutive string `form:"consecutive" binding:"required"`
	Name        string `form:"name" binding:"required"`
	Description string `form:"description" binding:"required"`
	Image       string `form:"image" binding:"required"`
}

type activity struct{ ID, Consecutive, Name, Description, Image string }

func (a *activity) gets() ([]activity, error) {

	db := service.Pool()

	rows, err := db.Query(service.GetActivities)

	if err != nil {
		return nil, err
	}

	activities := []activity{}

	for rows.Next() {

		var r activity

		err = rows.Scan(&r.ID, &r.Consecutive, &r.Name, &r.Description, &r.Image)

		if err != nil {
			return nil, err
		}

		activities = append(activities, r)
	}

	return decodes(activities), nil
}

func (a *activity) insert(imagePath string) error {

	db := service.Pool()
	tx, err := db.Begin()

	if err != nil {
		tx.Rollback()
		return err
	}

	var id string
	err = tx.QueryRow(service.NextIDActivity).Scan(&id)

	if err != nil {
		tx.Rollback()
		return err
	}

	query := fmt.Sprintf(service.InsertActivity, service.Encrypt(id), service.Encrypt(a.Consecutive),
		service.Encrypt(a.Name),
		service.Encrypt(a.Description),
		service.Encrypt(a.Image))

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
	entry.Detail = fmt.Sprintf("Table: %v | ID: %v", "dbo.activity", service.Encrypt(id))

	err = entry.Insert()

	if err != nil {
		return err
	}

	return nil

}

func (a *activity) delete() error {

	db := service.Pool()
	tx, err := db.Begin()

	if err != nil {
		tx.Rollback()
		return err
	}

	query := fmt.Sprintf(service.RemoveActivity, service.Encrypt(a.ID))

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
	entry.Detail = fmt.Sprintf("Table: %v | Username deleted: %v", "dbo.users", service.Encrypt(a.ID))

	err = entry.Insert()

	if err != nil {
		return err
	}

	return nil

}

func decodes(r []activity) []activity {

	var result []activity

	for _, row := range r {
		result = append(result, decode(row))
	}

	return result
}

func decode(r activity) activity {
	return activity{ID: service.Decrypt(r.ID), Consecutive: service.Decrypt(r.Consecutive),
		Name:        service.Decrypt(r.Name),
		Description: service.Decrypt(r.Description),
		Image:       service.Decrypt(r.Image)}
}
