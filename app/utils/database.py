from config import configuration as conf
import pymssql


def checkOut():
    conn = pymssql.connect(
        conf.host, conf.user, conf.passw, conf.name, )

    cursor = conn.cursor()

    if not cursor.connection:
        print("error")


class SQL:
    def __init__(self):
        try:
            self.conn = pymssql.connect(
                conf.host, conf.user, conf.passw, conf.name)
        except AssertionError as error:
            print(error)

    def execute(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)

        return cursor

    def close(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()


class error:
    insert = "exec dbo.insert_error @ID = '{}', @Username = '{}', @Date = '{}', @Detail = '{}';"
    getAll = "select * from dbo.get_errors;"
    nextID = "exec dbo.get_errors_sequence;"


class log:
    insert = "exec dbo.insert_log @ID = '{}', @Username = '{}', @Date = '{}', @Code = '{}', @Detail = '{}';"
    getAll = "select * from dbo.get_logs;"
    nextID = "exec dbo.get_logs_sequence;"


class role:
    insert = "exec dbo.insert_role @ID = '{}', @Name = '{}';"
    getAll = "select * from dbo.get_roles;"
    nextID = "exec dbo.get_roles_sequence;"

class user:
    insert = "exec dbo.insert_user @ID = '{}', @Username = '{}', @Email = '{}', @Password = '{}', @Security_Question = '{}', @Security_Answer = '{}';"
    getAll = "select * from dbo.get_users;"
    nextID = "exec dbo.get_users_sequence;"
    getUser = "exec dbo.get_user @Username = '{}'"
    updatePass = "exec dbo.update_password @Username = '{}', @Password = '{}';"
    checkSecurityPass = "exec dbo.check_security_password = @Username = '{}';"

class grant:
    insert = "exec dbo.insert_grant @ID = '{}', @User = '{}', @Role = '{}';" 
    getGrant = "exec dbo.get_grant @Username = '{}';"
    nextID = "exec dbo.get_grants_sequence;"
    removeGrant = "exec dbo.remove_grant = @User = '{}', @Role = '{}';"


class consecutiveType:
    insert = "exec dbo.insert_consecutive_type @ID = '{}', @Name = '{}';"
    getAll = "select * from dbo.get_consecutives_types;"
    nextID = "exec dbo.get_consecutives_types_sequence;"

class consecutive:
    insert = "exec dbo.insert_consecutive @ID = '{}', @ConsecutiveType = '{}', @Description = '{}', @HasPrefix = '{}', @Prefix = '{}', @HasRange = '{}', @Initial = '{}', @Final = '{}';"
    getAll = "select * from dbo.get_consecutives;"
    getConsecutive = "exec dbo.get_consecutive @ID = '{}';"
    nextID = "exec dbo.get_consecutives_sequence;"
    update_has_prefix = "exec dbo.update_has_prefix @ID = '{}', @HasPrefix = '{}';"

class activity:
    insert = "exec dbo.insert_activity @ID = '{}', @Consecutive = '{}', @ConsecutiveKey = '{}', @ConsecutiveNum = '{}', @Name = '{}', @Description = '{}', @ImagePath = '{}';"
    getAll = "select * from dbo.get_activities;"
    nextID = "exec dbo.get_activities_sequence;"

class productType:
    insert = "exec dbo.insert_product_type @ID = '{}', @Name = '{}';"
    getAll = "select * from dbo.get_product_types;"
    nextID = "exec dbo.get_product_type_sequence;"






