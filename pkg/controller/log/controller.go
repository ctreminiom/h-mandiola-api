package log

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

// Gets ...
func Gets(c *gin.Context) {

	context := Log{}

	logs, err := context.gets()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": logs})
}
