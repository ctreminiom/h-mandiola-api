package reservation

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

	newReservation := reservation{}
	newReservation.Consecutive = body.Consecutive
	newReservation.Client = body.Client
	newReservation.Room = body.Room
	newReservation.StartDate = body.StartDate
	newReservation.EndDate = body.EndDate
	newReservation.HasPaid = body.HasPaid
	newReservation.Adults = body.Adults
	newReservation.Children = body.Children

	err = newReservation.insert()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusCreated, gin.H{"message": fmt.Sprintf("The user %v has been created!", newReservation.ID)})
}

// Gets ...
func Gets(c *gin.Context) {

	context := reservation{}

	reservations, err := context.gets()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": reservations})
}
