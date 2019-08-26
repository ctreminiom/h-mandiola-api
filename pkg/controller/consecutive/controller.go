package consecutive

import (
	"fmt"
	"net/http"

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

	newConsecutiveType := consecutiveType{}
	newConsecutiveType.Name = body.Name

	err = newConsecutiveType.insert()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusCreated, gin.H{"message": fmt.Sprintf("The consecutive type %v has been created!", newConsecutiveType.Name)})
}

// GetsTypes ...
func GetsTypes(c *gin.Context) {

	context := consecutiveType{}

	types, err := context.gets()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": types})
}

// CreateConsecutive ...
func CreateConsecutive(c *gin.Context) {

	var body consecutivePayload

	err := c.ShouldBindJSON(&body)

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	newConsecutive := consecutive{}
	newConsecutive.Type = body.Type
	newConsecutive.Description = body.Description
	newConsecutive.HasPrefix = body.HasPrefix
	newConsecutive.Prefix = body.Prefix
	newConsecutive.HasRange = body.HasRange
	newConsecutive.Initial = body.Initial
	newConsecutive.Final = body.Final

	err = newConsecutive.insert()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusCreated, gin.H{"message": fmt.Sprintf("The consecutive %v has been created!", newConsecutive.ID)})
}

// GetsConsecutives ...
func GetsConsecutives(c *gin.Context) {

	context := consecutive{}

	types, err := context.gets()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": types})
}
