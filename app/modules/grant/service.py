from app.utils.database import SQL, grant, error, log, user, role
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

            # Get the username ID
            cursor = database.execute(
                user.getUser.format(encrypt(data["username"])))
            row = cursor.fetchone()
            userID = row[0]
            user_encripted = userID

            query = grant.insert.format(id, user_encripted, encrypt(data["role"]))
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

    def delete(self, data):
        try:
            database = SQL()

            # Get the username ID
            cursor = database.execute(
                user.getUser.format(encrypt(data["username"])))
            row = cursor.fetchone()
            userID = row[0]

            # Remove the grant
            database.execute(grant.removeGrant.format(userID, encrypt(data["role"])))

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
