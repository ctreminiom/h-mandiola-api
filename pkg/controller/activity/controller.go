package activity

import (
	"crypto/rand"
	"fmt"
	"log"
	"net/http"
	"os"
	"path/filepath"

	"github.com/gin-gonic/gin"
)

// Create ...
func Create(c *gin.Context) {

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

	newActivity := activity{}
	newActivity.Consecutive = c.PostForm("consecutive")
	newActivity.Name = c.PostForm("name")
	newActivity.Description = c.PostForm("description")
	newActivity.Image = file.Filename

	err = newActivity.insert(name)

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	err = os.Remove(name)

	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusCreated, gin.H{"message": fmt.Sprintf("The activity %v has been created!", newActivity.Name)})
}

// Gets ...
func Gets(c *gin.Context) {

	context := activity{}

	activities, err := context.gets()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": activities})
}

// Delete ...
func Delete(c *gin.Context) {

	id := c.Param("id")

	context := activity{ID: id}

	err := context.delete()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": fmt.Sprintf("Activity %v deleted", id)})
}
