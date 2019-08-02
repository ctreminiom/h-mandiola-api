from app.utils.database import SQL, role
from app.utils.encryt import encrypt, decrypt

from app.modules.error.service import insertError
from app.modules.log.service import insertLog

import pymssql


class Role:

    def gets(self, data):
        try:
            database = SQL()
            cursor = database.execute(role.getAll)

            result = []
            row = cursor.fetchone()
            while row:

                result.append({'id': decrypt(row[0]), 'name': decrypt(row[1])})
                row = cursor.fetchone()

            database.close()
            return {'message': result, 'status': 200}

        except pymssql.Error as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)

    def create(self, data):
        try:
            if 'name' not in data:
                return {'message': 'name field is required', 'status': 400}
            database = SQL()

            cursor = database.execute(role.nextID)
            row = cursor.fetchone()

            id = encrypt(str(row[0]))
            name = encrypt(data['name'])

            query = role.insert.format(id, name)
            cursor = database.execute(query)

            context = {
                "database": database,
                "jwt_user": data["jwt_user"],
                "code": "INSERT",
                "table": "dbo.Roles",
                "id": str(row[0]),
                "user": data["jwt_user"]
            }

            insertLog(context)

            database.commit()
            database.close()

            return {'message': "The role has been created", 'status': 201}

        except pymssql.Error as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)
