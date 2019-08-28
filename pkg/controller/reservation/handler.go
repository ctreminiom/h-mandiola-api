package reservation

import (
	"fmt"
	"time"

	errorm "github.com/ctreminiom/h-mandiola-api/pkg/controller/error"
	"github.com/ctreminiom/h-mandiola-api/pkg/controller/log"
	"github.com/ctreminiom/h-mandiola-api/pkg/service"
)

type payload struct {
	Consecutive string `json:"consecutive" binding:"required"`
	Client      string `json:"client" binding:"required"`
	Room        string `json:"room" binding:"required"`
	StartDate   string `json:"startDate" binding:"required"`
	EndDate     string `json:"endDate" binding:"required"`
	HasPaid     string `json:"hasPaid" binding:"required"`
	Adults      string `json:"adults" binding:"required"`
	Children    string `json:"children" binding:"required"`
}

type reservation struct{ ID, Consecutive, Client, Room, StartDate, EndDate, HasPaid, Adults, Children string }

func (r *reservation) insert() error {

	db := service.Pool()
	tx, err := db.Begin()

	if err != nil {
		tx.Rollback()
		return err
	}

	var id string
	err = tx.QueryRow(service.NextIDReservations).Scan(&id)

	if err != nil {
		tx.Rollback()
		return err
	}

	query := fmt.Sprintf(service.InsertReservation, service.Encrypt(id),
		service.Encrypt(r.Consecutive),
		service.Encrypt(r.Client),
		service.Encrypt(r.Room),
		service.Encrypt(r.StartDate),
		service.Encrypt(r.EndDate),
		service.Encrypt(r.HasPaid),
		service.Encrypt(r.Adults),
		service.Encrypt(r.Children),
	)

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
	entry.Detail = fmt.Sprintf("Table: %v | ID: %v", "dbo.reservations", service.Encrypt(id))

	err = entry.Insert()

	if err != nil {
		return err
	}

	return nil
}

func (r *reservation) gets() ([]reservation, error) {

	db := service.Pool()

	rows, err := db.Query(service.GetReservations)

	if err != nil {
		return nil, err
	}

	reservations := []reservation{}

	for rows.Next() {

		var r reservation

		err = rows.Scan(&r.ID, &r.Consecutive, &r.Client, &r.Room, &r.StartDate, &r.EndDate, &r.HasPaid, &r.Adults, &r.Children)

		if err != nil {
			return nil, err
		}

		reservations = append(reservations, r)
	}

	return decodes(reservations), nil

}

func decodes(r []reservation) []reservation {

	var result []reservation

	for _, row := range r {
		result = append(result, decode(row))
	}

	return result
}

func decode(r reservation) reservation {
	return reservation{ID: service.Decrypt(r.ID), Consecutive: service.Decrypt(r.Consecutive),
		Client:    service.Decrypt(r.Client),
		Room:      service.Decrypt(r.Room),
		StartDate: service.Decrypt(r.StartDate),
		EndDate:   service.Decrypt(r.EndDate),
		HasPaid:   service.Decrypt(r.HasPaid),
		Adults:    service.Decrypt(r.Adults),
		Children:  service.Decrypt(r.Children),
	}
}
