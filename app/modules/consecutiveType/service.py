from app.utils.database import SQL, consecutiveType, error, log
from app.utils.encryt import encrypt, decrypt

from app.modules.error.service import insertError
from app.modules.log.service import insertLog

import datetime
import pymssql


class Type:
    def gets(self, data):
        try:
            database = SQL()
            cursor = database.execute(consecutiveType.getAll)

            types_json = []

            row = cursor.fetchone()
            while row:

                types_json.append({'id': decrypt(row[0]),
                                   'name': decrypt(row[1]),
                                   })

                row = cursor.fetchone()

            database.close()

            return {'message': types_json, 'status': 200}

        except Exception as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)

    def create(self, data):
        try:

            if 'name' not in data:
                return {'message': "name field is required", 'status': 400}

            database = SQL()

            cursor = database.execute(consecutiveType.nextID)
            row = cursor.fetchone()

            id = encrypt(str(row[0]))
            name = encrypt(data["name"])

            query = consecutiveType.insert.format(id, name)
            cursor = database.execute(query)

            context = {
                "database": database,
                "jwt_user": data["jwt_user"],
                "code": "INSERT",
                "table": "dbo.Consecutives_Types",
                "id": str(row[0]),
                "user": data["jwt_user"]
            }

            insertLog(context)

            database.commit()
            database.close()

            return {'message': 'The consecutive type has been created', 'status': 201}

        except pymssql.Error as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)
