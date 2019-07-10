from app.utils.database import SQL, consecutiveType, error, log
from app.utils.encryt import encrypt, decrypt

import datetime


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

            database = SQL()

            # Get next ID
            cursor = database.execute(error.nextID)
            row = cursor.fetchone()

            date_time_str = '2018-06-29 08:15:27.243860'
            date_time_obj = datetime.datetime.strptime(
                date_time_str, '%Y-%m-%d %H:%M:%S.%f')

            id_encrypted = encrypt(row[0])
            username_encrypted = encrypt(data["jwt_user"])
            date_encrypted = encrypt(str(date_time_obj))
            detail_encrypted = encrypt(str(err))

            # Insert the error
            cursor = database.execute(error.insert.format(
                id_encrypted, username_encrypted, date_encrypted, detail_encrypted))

            database.commit()
            database.close()

            return {'message': str(err), 'status': 500}

    def create(self, data):
        try:

            if 'name' not in data: return {'message': "name field is required", 'status': 400}

            database = SQL()

            # Get next ID
            cursor = database.execute(consecutiveType.nextID)
            row = cursor.fetchone()

            id_encrypted = encrypt(str(row[0]))
            name_encrypted = encrypt(data["name"])

            cursor = database.execute(consecutiveType.insert.format(id_encrypted, name_encrypted))

            log_id = str(row[0])

            # Insert the transaction on the Log table
            cursor = database.execute(log.nextID)
            row = cursor.fetchone()

            date_time_str = '2018-06-29 08:15:27.243860'
            date_time_obj = datetime.datetime.strptime(
                date_time_str, '%Y-%m-%d %H:%M:%S.%f')

            id_encrypted = encrypt(str(row[0]))
            username_encrypted = encrypt(data["jwt_user"])
            date_encrypted = encrypt(str(date_time_obj))
            code_encrypted = encrypt("INSERT")

            detail_message = 'Entity: {}, ID: {}, Name: {}'.format(
                "Role", log_id, data["name"])
            detail_encrypted = encrypt(detail_message)

            # Insert the log
            cursor = database.execute(log.insert.format(
                id_encrypted, username_encrypted, code_encrypted, date_encrypted, detail_encrypted))

            database.commit()
            database.close()

            return {'message': 'The consecutive type has been created', 'status': 201}

        except Exception as err:

            database = SQL()

            # Get next ID
            cursor = database.execute(error.nextID)
            row = cursor.fetchone()

            date_time_str = '2018-06-29 08:15:27.243860'
            date_time_obj = datetime.datetime.strptime(
                date_time_str, '%Y-%m-%d %H:%M:%S.%f')

            id_encrypted = encrypt(row[0])
            username_encrypted = encrypt(data["jwt_user"])
            date_encrypted = encrypt(str(date_time_obj))
            detail_encrypted = encrypt(str(err))

            # Insert the error
            cursor = database.execute(error.insert.format(
                id_encrypted, username_encrypted, date_encrypted, detail_encrypted))

            database.commit()
            database.close()

            return {'message': str(err), 'status': 500}
