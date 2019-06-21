from config import config
import pymssql


class SQL:

    def __init__(self):
        try:
            self.conn = pymssql.connect(
                config.db_host, config.db_user, config.db_passw, config.db_name)
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


class errors:
    insert = "exec dba.insert_error @ID = '{}', @Username = '{}', @Date = '{}', @Detail = '{}';"
    getAll = "select * from dba.get_errors;"
    nextID = "exec dba.get_errors_sequence;"

class logs:
    insert = "exec dba.insert_log @ID = '{}', @Username = '{}', @Date = '{}', @Code = '{}', @Detail = '{}';"
    getAll = "select * from dba.get_logs;"
    nextID = "exec dba.get_logs_sequence;"


class consecutive_type:
    insert = "exec dba.insert_consecutive_type @ID = '{}', @Name = '{}';"
    getAll = "select * from dba.get_consecutives_types;"
    nextID = "exec dba.get_consecutives_types_sequence;"

class consecutive:
    insert = "exec dba.insert_consecutive @ID = '{}', @Type = '{}', @Description = '{}', @HasPrefix = '{}', @Prefix = '{}', @HasRange = '{}', @Initial = '{}', @Final = '{}', @Consecutive = '{}';"
    increase = "exec dba.increase_consecutive @ID = '{}', @Consecutive = '{}';"
    consecutive = "exec dba.get_actual_consecutive @ID = '{}';"
    update_final = "exec dba.update_final_consecutive_value @ID = '{}', @Final = '{}';"
    update_range = "exec dba.update_has_range_consecutive_value @ID = '{}', @hasRange = '{}';"
    update_ranges = "exec dba.update_ranges_consecutive_value @ID = '{}', @Initial = '{}', @Final = '{}';"
    getAll = "select * from dba.get_consecutives;"
    nextID = "exec dba.get_consecutives_sequence;"
    update_prefix_value = "exec dba.update_prefix_value @ID = '{}', @Prefix = '{}';"
    update_has_prefix_value = "exec dba.update_has_prefix_value @ID = '{}', @HasPrefix = '{}';"


