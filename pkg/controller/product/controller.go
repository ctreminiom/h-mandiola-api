package product

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

	newProductType := productType{}
	newProductType.Name = body.Name

	err = newProductType.insert()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusCreated, gin.H{"message": fmt.Sprintf("The consecutive type %v has been created!", newProductType.Name)})
}

// GetsTypes ...
func GetsTypes(c *gin.Context) {

	context := productType{}

	types, err := context.gets()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": types})
}

// CreateProduct ...
func CreateProduct(c *gin.Context) {

	var body productPayload

	err := c.ShouldBindJSON(&body)

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	newProduct := product{}
	newProduct.Type = body.Type
	newProduct.Consecutive = body.Consecutive
	newProduct.Name = body.Name

	err = newProduct.insert()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusCreated, gin.H{"message": fmt.Sprintf("The consecutive %v has been created!", newProduct.ID)})
}

// GetsProducts ...
func GetsProducts(c *gin.Context) {

	context := product{}

	types, err := context.gets()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": types})
}

// DeleteProduct ..
func DeleteProduct(c *gin.Context) {
	id := c.Param("id")

	context := product{ID: id}

	err := context.delete()

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": fmt.Sprintf("User %v deleted", id)})

}
