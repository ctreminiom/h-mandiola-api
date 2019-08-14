package role

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

	newRole := role{}
	newRole.Name = body.Name

	err = newRole.insert()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusCreated, gin.H{"message": fmt.Sprintf("The role %v has been created!", newRole.Name)})
}

// Gets ...
func Gets(c *gin.Context) {

	context := role{}

	roles, err := context.gets()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": roles})
}
