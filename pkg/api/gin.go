package api

import (
	"context"
	logg "log"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"

	"github.com/ctreminiom/h-mandiola-api/pkg/controller/activity"
	"github.com/ctreminiom/h-mandiola-api/pkg/controller/client"
	"github.com/ctreminiom/h-mandiola-api/pkg/controller/consecutive"
	errorm "github.com/ctreminiom/h-mandiola-api/pkg/controller/error"
	"github.com/ctreminiom/h-mandiola-api/pkg/controller/grant"
	"github.com/ctreminiom/h-mandiola-api/pkg/controller/log"
	"github.com/ctreminiom/h-mandiola-api/pkg/controller/role"
	"github.com/ctreminiom/h-mandiola-api/pkg/controller/user"
	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

// Start ...
func Start() {

	router := gin.Default()
	router.Use(cors.Default())

	srv := &http.Server{
		Addr:    ":8000",
		Handler: router,
	}

	router.GET("/module/users", user.Gets)
	router.POST("/module/user", user.Create)
	router.DELETE("/module/user/:username", user.Delete)
	router.PUT("/module/user/change/password/:username", user.Password)

	router.POST("/module/role", role.Create)
	router.GET("/module/roles", role.Gets)

	router.POST("/module/consecutive/type", consecutive.CreateType)
	router.GET("/module/consecutive/types", consecutive.GetsTypes)

	router.POST("/module/consecutive", consecutive.CreateConsecutive)
	router.GET("/module/consecutives", consecutive.GetsConsecutives)

	router.POST("/module/grant", grant.Create)
	router.GET("/module/grant/:username", grant.Get)
	router.DELETE("/module/grant", grant.Delete)

	router.POST("/module/client", client.Create)
	router.GET("/module/clients", client.Gets)

	router.POST("/module/activity", activity.Create)
	router.GET("/module/activities", activity.Gets)

	router.GET("/module/logs", log.Gets)
	router.GET("/module/errors", errorm.Gets)

	go func() {
		if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
			logg.Fatalf("listen: %s\n", err)
		}
	}()

	quit := make(chan os.Signal, 1)

	signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
	<-quit

	logg.Println("Shutdown Server ...")

	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	if err := srv.Shutdown(ctx); err != nil {
		logg.Fatal("Server Shutdown: ", err)
	}

	logg.Println("Server exiting")
}
