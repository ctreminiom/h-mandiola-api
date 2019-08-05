from app.utils.database import SQL, product, consecutive
from app.utils.encryt import encrypt, decrypt

from app.modules.error.service import insertError
from app.modules.log.service import insertLog
from app.modules.consecutive.service import Consecutive


import pymssql


class Product:

    def gets(self, data):
        try:
            database = SQL()
            cursor = database.execute(product.getAll)

            result = []
            row = cursor.fetchone()
            while row:
                result.append({
                    'id': decrypt(row[0]),
                    'consecutive': decrypt(row[1]),
                    'prefix': decrypt(row[2]),
                    'consecutive_num': decrypt(row[3]),
                    'product_type_name': decrypt(row[4]),
                    'name': decrypt(row[5]),
                    'description': decrypt(row[6]),
                    'price': decrypt(row[7]),
                    'inventory': decrypt(row[8]),
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

            cursor = database.execute(product.nextID)
            row = cursor.fetchone()

            id = encrypt(str(row[0]))
            consecutive = encrypt(data['consecutive'])

            #Get the consecutive code
            service = Consecutive()
            consecutive_query = {"jwt_user": "internal", "id": data["consecutive"]}
            message = service.get(consecutive_query)

            if message["status"] == 404:
                return message

            prefix = encrypt(message["message"][0]["prefix"])
            consecutive_num = encrypt(str(row[0]))

            product_type_ID = encrypt(data['product_type_ID'])

            print(data['product_type_ID'])


            name = encrypt(data['name'])
            description = encrypt(data['description'])
            price = encrypt(data['price'])
            inventory = encrypt(data['inventory'])

            query = product.insert.format(id, consecutive, prefix, consecutive_num, product_type_ID, name, description, price, inventory)
            cursor = database.execute(query)

            context = {
                "database": database,
                "jwt_user": data["jwt_user"],
                "code": "INSERT",
                "table": "dbo.Product",
                "id": str(row[0]),
                "user": data["jwt_user"]
            }

            insertLog(context)

            database.commit()
            database.close()

            return {'message': "The product has been created", 'status': 201}

        except pymssql.Error as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)
