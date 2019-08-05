from app.utils.database import SQL, roomType
from app.utils.encryt import encrypt, decrypt

from app.modules.error.service import insertError
from app.modules.log.service import insertLog

import pymssql


class RoomType:

    def gets(self, data):
        try:
            database = SQL()
            cursor = database.execute(roomType.getAll)

            result = []
            row = cursor.fetchone()
            while row:
                result.append({'id': decrypt(row[0]), 'name': decrypt(row[1]), 'description': decrypt(row[2]), 'price': decrypt(row[3])})
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

            cursor = database.execute(roomType.nextID)
            row = cursor.fetchone()

            id = encrypt(str(row[0]))
            name = encrypt(data['name'])
            description = encrypt(data['description'])
            price = encrypt(data['price'])


            query = roomType.insert.format(id, name, description, price)
            cursor = database.execute(query)

            context = {
                "database": database,
                "jwt_user": data["jwt_user"],
                "code": "INSERT",
                "table": "dbo.Room_Type",
                "id": str(row[0]),
                "user": data["jwt_user"]
            }

            insertLog(context)

            database.commit()
            database.close()

            return {'message': "The room type has been created", 'status': 201}

        except pymssql.Error as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)
