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
	"github.com/ctreminiom/h-mandiola-api/pkg/controller/product"
	"github.com/ctreminiom/h-mandiola-api/pkg/controller/role"
	"github.com/ctreminiom/h-mandiola-api/pkg/controller/room"
	"github.com/ctreminiom/h-mandiola-api/pkg/controller/user"
	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

// Start ...
func Start() {

	router := gin.Default()

	//router.Use(CORS())

	router.Use(cors.New(cors.Config{
		AllowOrigins:     []string{"*"},
		AllowMethods:     []string{"*"},
		AllowHeaders:     []string{"*"},
		AllowCredentials: true,
		MaxAge:           12 * time.Hour,
	}))

	router.GET("/module/users", user.Gets)

	public := router.Group("/public")
	{
		//public.Use(cors.Default())
		public.POST("/module/user/login", user.Login)

		public.GET("/module/clients", client.Gets)
		public.POST("/module/client", client.Create)
		public.GET("/module/client/:aud", client.Get)

		public.GET("/module/users", user.Gets)
	}

	private := router.Group("/private")
	{

		//private.Use(CORS())
		//private.Use(CORS())
		private.Use(JWT())

		private.GET("/module/users", user.Gets)
		private.POST("/module/user", user.Create)
		private.DELETE("/module/user/:username", user.Delete)
		private.PUT("/module/user/change/password/:username", user.Password)

		private.POST("/module/role", role.Create)
		private.GET("/module/roles", role.Gets)

		private.POST("/module/consecutive/type", consecutive.CreateType)
		private.GET("/module/consecutive/types", consecutive.GetsTypes)

		private.POST("/module/consecutive", consecutive.CreateConsecutive)
		private.GET("/module/consecutives", consecutive.GetsConsecutives)

		private.POST("/module/grant", grant.Create)
		private.GET("/module/grant/:username", grant.Get)
		private.DELETE("/module/grant", grant.Delete)

		private.POST("/module/activity", activity.Create)
		private.DELETE("/module/activity/:id", activity.Delete)
		private.GET("/module/activities", activity.Gets)

		private.POST("/module/product/type", product.CreateType)
		private.GET("/module/product/types", product.GetsTypes)

		private.POST("/module/product", product.CreateProduct)
		private.GET("/module/products", product.GetsProducts)

		private.POST("/module/room/type", room.CreateType)
		private.GET("/module/room/types", room.GetsTypes)

		private.POST("/module/room", room.CreateRoom)
		private.GET("/module/rooms", room.GetsRooms)
		private.DELETE("/module/room/:id", room.DeleteRoom)

		private.GET("/module/logs", log.Gets)
		private.GET("/module/errors", errorm.Gets)
	}

	/*
		router.GET("/module/users", user.Gets)
		router.POST("/module/user", user.Create)
		router.DELETE("/module/user/:username", user.Delete)
		router.PUT("/module/user/change/password/:username", user.Password)
		//router.POST("/module/user/login", user.Login)

		router.POST("/module/role", role.Create)
		router.GET("/module/roles", role.Gets)

		router.POST("/module/consecutive/type", consecutive.CreateType)
		router.GET("/module/consecutive/types", consecutive.GetsTypes)

		router.POST("/module/consecutive", consecutive.CreateConsecutive)
		router.GET("/module/consecutives", consecutive.GetsConsecutives)

		router.POST("/module/grant", grant.Create)
		router.GET("/module/grant/:username", grant.Get)
		router.DELETE("/module/grant", grant.Delete)

		//router.POST("/module/client", client.Create)
		//router.GET("/module/clients", client.Gets)

		router.POST("/module/activity", activity.Create)
		router.DELETE("/module/activity/:id", activity.Delete)
		router.GET("/module/activities", activity.Gets)

		router.POST("/module/product/type", product.CreateType)
		router.GET("/module/product/types", product.GetsTypes)

		router.POST("/module/product", product.CreateProduct)
		router.GET("/module/products", product.GetsProducts)

		router.POST("/module/room/type", room.CreateType)
		router.GET("/module/room/types", room.GetsTypes)

		router.POST("/module/room", room.CreateRoom)
		router.GET("/module/rooms", room.GetsRooms)
		router.DELETE("/module/room/:id", room.DeleteRoom)

		router.GET("/module/logs", log.Gets)
		router.GET("/module/errors", errorm.Gets)
	*/

	srv := &http.Server{
		Addr:    ":8000",
		Handler: router,
	}

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
