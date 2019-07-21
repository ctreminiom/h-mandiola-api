from app.utils.database import SQL, consecutive, error, log
from app.utils.encryt import encrypt, decrypt

from app.modules.error.service import insertError
from app.modules.log.service import insertLog

import datetime
import pymssql


class Consecutive:
    def gets(self, data):
        try:
            database = SQL()

            cursor = database.execute(consecutive.getAll)

            result = []
            row = cursor.fetchone()

            while row:

                result.append({'id': decrypt(row[0]),
                               'type': decrypt(row[1]),
                               'description': decrypt(row[2]),
                               'has_prefix': decrypt(row[3]),
                               'prefix': decrypt(row[4]),
                               'has_range': decrypt(row[5]),
                               'initial': decrypt(row[6]),
                               'final': decrypt(row[7]),
                               })

                row = cursor.fetchone()

            database.close()

            return {'message': result, 'status': 200}

        except pymssql.Error as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)

    def create(self, data):

        try:
            database = SQL()

            cursor = database.execute(consecutive.nextID)
            row = cursor.fetchone()

            id = encrypt(str(row[0]))
            cType = encrypt(data["cType"])
            description = encrypt(data["description"])
            has_prefix = encrypt(data["has_prefix"])

            if 'prefix' not in data:
                prefix = encrypt('null')

            has_range = encrypt(data["has_range"])

            if 'initial' not in data:
                initial = encrypt('null')

            if 'final' not in data:
                final = encrypt('null')

            query = consecutive.insert.format(
                id, cType, description, has_prefix, prefix, has_range, initial, final)

            print(id)
            print(query)

            cursor = database.execute(query)

            context = {
                "database": database,
                "jwt_user": data["jwt_user"],
                "code": "INSERT",
                "table": "dbo.Consecutives",
                "id": str(row[0]),
                "user": data["jwt_user"]
            }

            insertLog(context)

            database.commit()
            database.close()

            return {'message': 'The consecutive has been created', 'status': 201}

        except pymssql.Error as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)

    def get(self, data):
        try:
            database = SQL()

            query = consecutive.getConsecutive.format(encrypt(data["id"]))
            cursor = database.execute(query)

            row = cursor.fetchone()

            if not row:
                return {'message': "The consecutive doesn't exits", 'status': 404}

            result = []
            while row:
                result.append({'id': decrypt(row[0]),
                               'type': decrypt(row[1]),
                               'description': decrypt(row[2]),
                               'has_prefix': decrypt(row[3]),
                               'prefix': decrypt(row[4]),
                               'has_range': decrypt(row[5]),
                               'initial': decrypt(row[6]),
                               'final': decrypt(row[7]),
                               })

                row = cursor.fetchone()

            database.close()

            return {'message': result, 'status': 200}

        except pymssql.Error as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)
