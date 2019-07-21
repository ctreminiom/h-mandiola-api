from app.utils.database import SQL, productType
from app.utils.encryt import encrypt, decrypt

from app.modules.error.service import insertError
from app.modules.log.service import insertLog

import pymssql


class ProductType:

    def gets(self, data):
        try:
            database = SQL()
            cursor = database.execute(productType.getAll)

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
            database = SQL()

            cursor = database.execute(productType.nextID)
            row = cursor.fetchone()

            id = encrypt(str(row[0]))
            name = encrypt(data['name'])

            query = productType.insert.format(id, name)
            cursor = database.execute(query)

            context = {
                "database": database,
                "jwt_user": data["jwt_user"],
                "code": "INSERT",
                "table": "dbo.Product_Type",
                "id": str(row[0]),
                "user": data["jwt_user"]
            }

            insertLog(context)

            database.commit()
            database.close()

            return {'message': "The product type has been created", 'status': 201}

        except pymssql.Error as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)
