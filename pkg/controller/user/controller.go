package user

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

	newUser := user{}
	newUser.Username = body.Username
	newUser.Email = body.Email
	newUser.Password = body.Password
	newUser.Question = body.Question
	newUser.Answer = body.Answer

	err = newUser.insert()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusCreated, gin.H{"message": fmt.Sprintf("The user %v has been created!", newUser.Username)})
}

// Password ...
func Password(c *gin.Context) {

	var body payloadPass

	err := c.ShouldBindJSON(&body)

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	username := c.Param("username")

	context := user{Username: username, Password: body.Password}

	err = context.password()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": fmt.Sprintf("The username %v has change the passowrd", username)})
}

// Delete ..
func Delete(c *gin.Context) {
	username := c.Param("username")

	context := user{Username: username}

	err := context.delete()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": fmt.Sprintf("User %v deleted", username)})

}

// Gets ...
func Gets(c *gin.Context) {

	context := user{}

	users, err := context.gets()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": users})
}
