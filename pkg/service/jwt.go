package service

import (
	"time"

	"github.com/spf13/viper"

	"github.com/dgrijalva/jwt-go"
)

// Claims ...
type Claims struct {
	Username string `json:"username"`
	jwt.StandardClaims
}

// EncodeToken ...
func EncodeToken(username string) (string, error) {

	expirationTime := time.Now().Add(60 * time.Minute)
	claims := &Claims{Username: username, StandardClaims: jwt.StandardClaims{ExpiresAt: expirationTime.Unix()}}

	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)

	tokenAsString, err := token.SignedString([]byte(viper.GetString("jwt.token")))

	if err != nil {
		return "", err
	}

	return tokenAsString, nil
}

// DecodeToken ...
func DecodeToken(tokenString string) (*Claims, error) {

	claims := &Claims{}

	tkn, err := jwt.ParseWithClaims(tokenString, claims, func(token *jwt.Token) (interface{}, error) {
		return []byte(viper.GetString("jwt.token")), nil
	})

	if err != nil {
		return nil, err
	}

	if !tkn.Valid {
		return nil, err
	}

	return claims, nil
}
