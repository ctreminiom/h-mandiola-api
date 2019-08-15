package api

import (
	"log"
	"net/http"
	"strings"

	"github.com/ctreminiom/h-mandiola-api/pkg/service"

	"github.com/gin-gonic/gin"
)

// JWT ...
func JWT() gin.HandlerFunc {

	return func(c *gin.Context) {

		if c.GetHeader("Authorization") == "" {

			c.JSON(http.StatusBadRequest, gin.H{"error": "Token required"})
			c.Abort()
		}

		if c.GetHeader("Authorization") != "" {

			token := strings.Split(c.GetHeader("Authorization"), " ")
			log.Println(token[1])

			claims, err := service.DecodeToken(token[1])

			if err != nil {
				c.JSON(http.StatusUnauthorized, gin.H{"error": err.Error()})
				c.Abort()
			}

			log.Println(claims)

			c.Next()
		}

		c.Next()
	}

}
