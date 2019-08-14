package activity

import (
	"fmt"
	"net/http"
	"os"
	"path/filepath"

	"github.com/ctreminiom/h-mandiola-api/pkg/service"

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

	destinationBlobName := fmt.Sprintf("activities/%v", file.Filename)

	url, err := service.Upload(name, "h-mandiola-files", destinationBlobName)

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.String(http.StatusOK, fmt.Sprintf("'%s' uploaded!", url))
}
