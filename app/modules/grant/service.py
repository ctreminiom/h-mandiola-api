from app.utils.database import SQL, grant, error, log
from app.utils.encryt import encrypt, decrypt

from app.modules.error.service import insertError
from app.modules.log.service import insertLog

import pymssql


class Grant:
    def get(self, data):
        try:

            if 'username' not in data:
                return {'message': "username field is required", 'status': 400}

            database = SQL()
            cursor = database.execute(
                grant.getGrant.format(encrypt(data["username"])))

            result = []

            row = cursor.fetchone()
            while row:
                result.append(
                    {'id': decrypt(row[0]), 'user': decrypt(row[2]), 'role': decrypt(row[1])})
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

            cursor = database.execute(grant.nextID)
            row = cursor.fetchone()

            id = encrypt(str(row[0]))
            user = encrypt(data["username"])
            role = encrypt(data["role"])

            query = grant.insert.format(id, user, role)
            cursor = database.execute(query)

            context = {
                "database": database,
                "jwt_user": data["jwt_user"],
                "code": "INSERT",
                "table": "dbo.Grants",
                "id": str(row[0]),
                "user": data["jwt_user"]
            }

            insertLog(context)

            database.commit()
            database.close()

            return {'message': "The grant has been created", 'status': 201}

        except pymssql.Error as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)

    def remove(self, data):
        try:
            database = SQL()

            database.execute(grant.removeGrant.format(
                encrypt(data["username"]), encrypt(data["role"])))

            context = {
                "database": database,
                "jwt_user": data["jwt_user"],
                "code": "DELETE",
                "table": "dbo.Grants",
                "id": "null",
                "user": data["jwt_user"]
            }

            insertLog(context)

            database.commit()
            database.close()

            return {"message": "Grant removedd", "status": 202}

        except pymssql.Error as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)
