package main

import (
	"os"
	"path/filepath"

	"github.com/ctreminiom/h-mandiola-api/pkg/api"
	"github.com/ctreminiom/h-mandiola-api/pkg/service"
	"github.com/spf13/viper"
)

func main() {

	err := service.Load("./")

	if err != nil {
		panic(err)
	}

	sqlServer := service.SQL{}

	sqlServer.Server = viper.GetString("sql.server")
	sqlServer.Port = viper.GetInt("sql.port")
	sqlServer.User = viper.GetString("sql.user")
	sqlServer.Password = viper.GetString("sql.password")
	sqlServer.Database = viper.GetString("sql.database")

	err = sqlServer.StartTheConnection()

	if err != nil {
		panic(err)
	}

	rootProjectPath, err := filepath.Abs(filepath.Dir(os.Args[0]))

	if err != nil {
		panic(err)
	}

	os.Setenv("GOOGLE_APPLICATION_CREDENTIALS", rootProjectPath+"/docs/h-mandiola-beb59920ed9d.json")

	api.Start()
}
