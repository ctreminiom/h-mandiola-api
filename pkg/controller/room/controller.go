package room

import (
	"crypto/rand"
	"fmt"
	"log"
	"net/http"
	"os"
	"path/filepath"

	"github.com/gin-gonic/gin"
)

// CreateType ...
func CreateType(c *gin.Context) {

	var body typePayload

	err := c.ShouldBindJSON(&body)

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	newRoomType := roomType{}
	newRoomType.Name = body.Name

	err = newRoomType.insert()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusCreated, gin.H{"message": fmt.Sprintf("The consecutive type %v has been created!", newRoomType.Name)})
}

// GetsTypes ...
func GetsTypes(c *gin.Context) {

	context := roomType{}

	types, err := context.gets()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": types})
}

// CreateRoom ...
func CreateRoom(c *gin.Context) {

	file, err := c.FormFile("image")

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	rootProjectPath, err := filepath.Abs(filepath.Dir(os.Args[0]))

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	b := make([]byte, 16)
	_, err = rand.Read(b)
	if err != nil {
		log.Fatal(err)
	}
	uuid := fmt.Sprintf("%x-%x-%x-%x-%x",
		b[0:4], b[4:6], b[6:8], b[8:10], b[10:])

	name := fmt.Sprintf("%v/img/%v-%v", rootProjectPath, uuid, file.Filename)
	c.SaveUploadedFile(file, name)

	newRoom := room{}
	newRoom.Consecutive = c.PostForm("consecutive")
	newRoom.Type = c.PostForm("type")
	newRoom.Number = c.PostForm("number")
	newRoom.Description = c.PostForm("description")
	newRoom.Available = c.PostForm("available")
	newRoom.Image = file.Filename

	err = newRoom.insert(name)

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	err = os.Remove(name)

	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusCreated, gin.H{"message": fmt.Sprintf("The room %v has been created!", newRoom.Number)})
}

// GetsRooms ...
func GetsRooms(c *gin.Context) {

	context := room{}

	activities, err := context.gets()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": activities})
}

// DeleteRoom ...
func DeleteRoom(c *gin.Context) {

	id := c.Param("id")

	context := room{ID: id}

	err := context.delete()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": fmt.Sprintf("Room %v deleted", id)})
}
