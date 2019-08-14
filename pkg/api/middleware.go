package api

import (
	"log"
	"strings"

	"github.com/gin-gonic/gin"
)

// JWT ...
func JWT() gin.HandlerFunc {

	return func(c *gin.Context) {

		if c.GetHeader("Authorization") != "" {

			token := strings.Split(c.GetHeader("Authorization"), " ")
			log.Println(token)

		}
	}

}
