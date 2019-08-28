package service

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/denisenkom/go-mssqldb" // The SQL Server Driver
)

// SQL ...
type SQL struct {
	Server   string
	Port     int
	User     string
	Password string
	Database string
}

var db *sql.DB

// StartTheConnection ...
func (s *SQL) StartTheConnection() error {

	connString := fmt.Sprintf("server=%s;user id=%s;password=%s;port=%d;database=%s;", s.Server, s.User, s.Password, s.Port, s.Database)

	conn, err := sql.Open("mssql", connString)

	if err != nil {
		log.Fatal("Open connection failed:", err.Error())
		return err
	}

	db = conn

	return nil
}

// Pool .
func Pool() *sql.DB { return db }

// .
const (
	NextIDUser     = "exec dbo.get_users_sequence;"
	InsertUser     = "exec dbo.insert_user @ID = '%v', @Username = '%v', @Email = '%v', @Password = '%v', @Question = '%v', @Answer = '%v';"
	GetUsers       = "select * from dbo.get_users;"
	GetUser        = "exec dbo.get_user @Username = '%v'"
	UpdatePassword = "exec dbo.update_password @Username = '%v', @Password = '%v';"
	DeleteUser     = "exec dbo.delete_user @Username = '%v';"

	NextIDLog = "exec dbo.get_logs_sequence;"
	InsertLog = "exec dbo.insert_log @ID = '%v', @Username = '%v', @Date = '%v', @Code = '%v', @Detail = '%v';"
	GetLogs   = "select * from dbo.get_logs;"

	NextIDError = "exec dbo.get_errors_sequence;"
	InsertError = "exec dbo.insert_error @ID = '%v', @Username = '%v', @Date = '%v', @Detail = '%v';"
	GetErrors   = "select * from dbo.get_errors;"

	NextIDRole = "exec dbo.get_roles_sequence;"
	InsertRole = "exec dbo.insert_role @ID = '%v', @Name = '%v';"
	GetRoles   = "select * from dbo.get_roles;"

	NextIDType = "exec dbo.get_consecutives_types_sequence;"
	InsertType = "exec dbo.insert_consecutive_type @ID = '%v', @Name = '%v';"
	GetTypes   = "select * from dbo.get_consecutives_types;"

	NextIDConsecutive = "exec dbo.get_consecutives_sequence;"
	InsertConsecutive = "exec dbo.insert_consecutive @ID = '%v', @Type = '%v', @Description = '%v', @HasPrefix = '%v', @Prefix = '%v', @HasRange = '%v', @Initial = '%v', @Final = '%v';"
	GetConsecutives   = "select * from dbo.get_consecutives;"

	NextIDClients = "exec dbo.get_clients_sequence;"
	InsertClient  = "exec dbo.insert_client @ID = '%v', @Consecutive = '%v', @First = '%v', @Last = '%v', @Username = '%v', @Email = '%v', @Sub = '%v', @Aud = '%v';"
	GetClients    = "select * from dbo.get_clients;"
	GetClient     = "exec dbo.get_client @Sub = '%v';"

	NextIDGrants = "exec dbo.get_grants_sequence;"
	InsertGrant  = "exec dbo.insert_grant @ID = '%v', @User = '%v', @Role = '%v';"
	GetGrant     = "exec dbo.get_grant @Username = '%v';"
	RemoveGrant  = "exec dbo.remove_grant @User = '%v', @Role = '%v';"

	NextIDActivity = "exec dbo.get_activities_sequence;"
	InsertActivity = "exec dbo.insert_activity @ID = '%v', @Consecutive = '%v', @Name = '%v', @Description = '%v', @Image = '%v';"
	GetActivities  = "select * from dbo.get_activities;"
	RemoveActivity = "exec dbo.delete_activity @ID = '%v';"

	NextIDProductType = "exec dbo.get_product_type_sequence;"
	InsertProductType = "exec dbo.insert_product_type @ID = '%v', @Name = '%v';"
	GetProductTypes   = "select * from dbo.get_product_types"

	NextIDProduct = "exec dbo.get_product_sequence;"
	InsertProduct = "exec dbo.insert_product @ID = '%v', @Consecutive = '%v', @Type = '%v', @Name = '%v';"
	GetProducts   = "select * from dbo.get_products;"
	RemoveProduct = "exec dbo.delete_product @ID = '%v';"

	NextIDRoomType = "exec dbo.get_rooms_type_sequence;"
	InsertRoomType = "exec dbo.insert_room_type @ID = '%v', @Name = '%v';"
	GetRoomsTypes  = "select * from dbo.get_rooms_types;"

	NextIDRooms = "exec dbo.get_rooms_sequence;"
	InsertRoom  = "exec dbo.insert_room @ID = '%v', @Consecutive = '%v', @RoomType = '%v', @Number = '%v', @Description = '%v', @Available = '%v', @Image = '%v';"
	GetRooms    = "select * from dbo.get_rooms;"
	RemoveRoom  = "exec dbo.delete_room @ID = '%v';"

	NextIDReservations = "exec dbo.get_reservations_sequence;"
	InsertReservation  = "exec dbo.insert_reservation @ID = '%v', @Consecutive = '%v', @Client = '%v', @Room = '%v', @StartDate = '%v', @EndDate = '%v', @HasPaid = '%v', @Adults = '%v', @Childrens = '%v';"
	GetReservations    = "select * from dbo.get_reservations;"
)
