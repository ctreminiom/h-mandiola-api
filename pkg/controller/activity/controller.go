package activity

import (
	"fmt"
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

	name := fmt.Sprintf("%v/img/%v", rootProjectPath, file.Filename)
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
