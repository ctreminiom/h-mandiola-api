package service

import (
	"strings"

	"github.com/spf13/viper"
)

// Load ...
func Load(path string) error {

	viper.SetConfigName("config")
	viper.AddConfigPath(path)
	viper.SetEnvKeyReplacer(strings.NewReplacer(".", "_"))

	return viper.ReadInConfig()
}
