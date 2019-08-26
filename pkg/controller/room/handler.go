package room

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

type roomType struct{ ID, Name string }

func (c *roomType) gets() ([]roomType, error) {

	db := service.Pool()

	rows, err := db.Query(service.GetRoomsTypes)

	if err != nil {
		return nil, err
	}

	types := []roomType{}

	for rows.Next() {

		var r roomType

		err = rows.Scan(&r.ID, &r.Name)

		if err != nil {
			return nil, err
		}

		types = append(types, r)
	}

	return decodesType(types), nil
}

func (c *roomType) insert() error {

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

	query := fmt.Sprintf(service.InsertRoomType, service.Encrypt(id), service.Encrypt(c.Name))

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
	entry.Detail = fmt.Sprintf("Table: %v | ID: %v", "dbo.rooms_types", service.Encrypt(id))

	err = entry.Insert()

	if err != nil {
		return err
	}

	return nil
}

func decodesType(r []roomType) []roomType {

	var result []roomType

	for _, row := range r {
		result = append(result, decodeType(row))
	}

	return result
}

func decodeType(r roomType) roomType {
	return roomType{ID: service.Decrypt(r.ID), Name: service.Decrypt(r.Name)}
}

type roomPayload struct {
	Consecutive string `json:"consecutive" binding:"required"`
	Type        string `json:"type" binding:"required"`
	Number      string `json:"number" binding:"required"`
	Description string `json:"description" binding:"required"`
	Available   string `json:"available" binding:"required"`
	Image       string `json:"image" binding:"required"`
}

type room struct{ ID, Consecutive, Type, Number, Description, Available, Image string }

func (a *room) gets() ([]room, error) {

	db := service.Pool()

	rows, err := db.Query(service.GetRooms)

	if err != nil {
		return nil, err
	}

	rooms := []room{}

	for rows.Next() {

		var r room

		err = rows.Scan(&r.ID, &r.Consecutive, &r.Type, &r.Number, &r.Description, &r.Available, &r.Image)

		if err != nil {
			return nil, err
		}

		rooms = append(rooms, r)
	}

	return decodes(rooms), nil
}

func (a *room) insert(source string) error {

	db := service.Pool()
	tx, err := db.Begin()

	if err != nil {
		tx.Rollback()
		return err
	}

	var id string
	err = tx.QueryRow(service.NextIDRooms).Scan(&id)

	if err != nil {
		tx.Rollback()
		return err
	}

	//Upload the image to Google Storage
	blobName := fmt.Sprintf("rooms/%v%v", service.Encrypt(id), a.Image)

	storageURL, err := service.Upload(source, "h-mandiola-files", blobName)

	if err != nil {
		return err
	}

	query := fmt.Sprintf(service.InsertRoom, service.Encrypt(id), service.Encrypt(a.Consecutive),
		service.Encrypt(a.Type),
		service.Encrypt(a.Number),
		service.Encrypt(a.Description),
		service.Encrypt(a.Available),
		service.Encrypt(storageURL))

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
	entry.Detail = fmt.Sprintf("Table: %v | ID: %v", "dbo.rooms", service.Encrypt(id))

	err = entry.Insert()

	if err != nil {
		return err
	}

	return nil

}

func (a *room) delete() error {

	db := service.Pool()
	tx, err := db.Begin()

	if err != nil {
		tx.Rollback()
		return err
	}

	query := fmt.Sprintf(service.RemoveRoom, service.Encrypt(a.ID))

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
	entry.Detail = fmt.Sprintf("Table: %v | Room deleted: %v", "dbo.rooms", service.Encrypt(a.ID))

	err = entry.Insert()

	if err != nil {
		return err
	}

	return nil

}

func decodes(r []room) []room {

	var result []room

	for _, row := range r {
		result = append(result, decode(row))
	}

	return result
}

func decode(r room) room {
	return room{ID: service.Decrypt(r.ID), Consecutive: service.Decrypt(r.Consecutive),
		Number:      service.Decrypt(r.Number),
		Description: service.Decrypt(r.Description),
		Type:        service.Decrypt(r.Type),
		Available:   service.Decrypt(r.Available),
		Image:       service.Decrypt(r.Image)}
}
