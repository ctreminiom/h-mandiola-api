package client

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

// Create ...
func Create(c *gin.Context) {

	var body payload

	err := c.ShouldBindJSON(&body)

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	newClient := client{}
	newClient.Consecutive = body.Consecutive
	newClient.First = body.First
	newClient.Last = body.Last
	newClient.Username = body.Username
	newClient.Email = body.Email
	newClient.Sub = body.Sub
	newClient.Aud = body.Aud

	err = newClient.insert()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusCreated, gin.H{"message": fmt.Sprintf("The user %v has been created!", newClient.Email)})
}

// Gets ...
func Gets(c *gin.Context) {

	context := client{}

	clients, err := context.gets()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": clients})
}

// Get ...
func Get(c *gin.Context) {

	aud := c.Param("aud")
	context := client{Aud: aud}

	result, err := context.get()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": result})
}
