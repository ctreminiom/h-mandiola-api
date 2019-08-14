package grant

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

	newGrant := grant{}
	newGrant.User = body.Username
	newGrant.Role = body.Role

	err = newGrant.insert()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusCreated, gin.H{"message": fmt.Sprintf("The grant %v has been created!", newGrant.Role)})
}

// Get ...
func Get(c *gin.Context) {

	username := c.Param("username")

	context := grant{}

	result, err := context.get(username)

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": result})
}

// Delete ...
func Delete(c *gin.Context) {

	var body payload

	err := c.ShouldBindJSON(&body)

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	context := grant{}
	context.User = body.Username
	context.Role = body.Role

	err = context.delete()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusAccepted, gin.H{"message": fmt.Sprintf("The grant %v for the user %v has been removed!", context.Role, context.User)})
}
