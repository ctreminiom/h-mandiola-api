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




