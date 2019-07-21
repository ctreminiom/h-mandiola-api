from app.utils.database import SQL, user
from app.utils.encryt import encrypt, decrypt

from app.modules.error.service import insertError
from app.modules.log.service import insertLog

import pymssql


class User:
    def gets(self, data):
        try:
            database = SQL()
            cursor = database.execute(user.getAll)

            result = []
            row = cursor.fetchone()
            while row:
                result.append({'id': decrypt(row[0]),
                               'username': decrypt(row[1]),
                               'email': decrypt(row[2]),
                               'security_question': decrypt(row[3])})
                row = cursor.fetchone()

            database.close()
            return {'message': result, 'status': 200}
        except pymssql.Error as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)

    def create(self, data):
        try:
            if 'username' not in data:
                return {'message': 'username field is required', 'status': 400}
            if 'email' not in data:
                return {'message': 'email field is required', 'status': 400}
            if 'security_question' not in data:
                return {'message': 'security_question field is required', 'status': 400}
            if 'security_answer' not in data:
                return {'message': 'security_answer field is required', 'status': 400}

            database = SQL()

            # Get next ID
            cursor = database.execute(user.nextID)
            row = cursor.fetchone()

            id = encrypt(str(row[0]))
            username = encrypt(data["username"])
            email = encrypt(data["email"])
            passw = encrypt(data["password"])

            security_q = encrypt(data["security_question"])
            security_a = encrypt(data["security_answer"])

            query = user.insert.format(
                id, username, email, passw, security_q, security_a)
            cursor = database.execute(query)

            context = {
                "database": database,
                "jwt_user": data["jwt_user"],
                "code": "INSERT",
                "table": "dbo.Users",
                "id": str(row[0]),
                "user": data["jwt_user"]
            }

            insertLog(context)

            database.commit()
            database.close()

            return {'message': "The user has been created", 'status': 201}

        except pymssql.Error as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)

    def get(self, data):
        try:
            database = SQL()

            cursor = database.execute(
                user.getUser.format(encrypt(data["username"])))
            row = cursor.fetchone()

            if not row:
                return {'message': "The username doesn't exits", 'status': 404}

            result = []
            while row:
                result.append({'id': decrypt(row[0]), 'username': decrypt(
                    row[1]), 'email': decrypt(row[2]), 'security_question': decrypt(row[3])})
                row = cursor.fetchone()

            database.close()

            return {'message': result, 'status': 200}

        except pymssql.Error as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)

    def updatePassword(self, data):

        try:
            database = SQL()

            cursor = database.execute(
                user.getUser.format(encrypt(data["username"])))
            row = cursor.fetchone()
            if not row:
                return {'message': "The username doesn't exits", 'status': 404}

            #Update the password
            query = user.updatePass.format(encrypt(data["username"]), encrypt(data["password"]))
            cursor = database.execute(query)

            context = {
                "database": database,
                "jwt_user": data["jwt_user"],
                "code": "UPDATE",
                "table": "dbo.Users",
                "id": "PASSWORD",
                "user": data["jwt_user"]
            }

            insertLog(context)

            database.commit()
            database.close()

            return {'message': "The passwrd has been removed", 'status': 201}
            

        except pymssql.Error as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)