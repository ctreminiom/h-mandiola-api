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
