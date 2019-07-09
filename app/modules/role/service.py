from app.utils.database import SQL, role, error, log
from app.utils.encryt import encrypt, decrypt

import datetime


class Role:

    def getAll(self, data):

        try:

            database = SQL()

            # Get all logs encrypted
            cursor = database.execute(role.getAll)

            role_json = []

            row = cursor.fetchone()
            while row:

                role_json.append({'id': decrypt(row[0]),
                                  'name': decrypt(row[1]),
                                  })

                row = cursor.fetchone()

            database.close()

            message = {}
            message["message"] = role_json
            message["status"] = 200

            return message

        except Exception as err:

            database = SQL()

            # Get next ID
            cursor = database.execute(error.nextID)
            row = cursor.fetchone()

            date_time_str = '2018-06-29 08:15:27.243860'
            date_time_obj = datetime.datetime.strptime(
                date_time_str, '%Y-%m-%d %H:%M:%S.%f')

            id_encrypted = encrypt(row[0])
            username_encrypted = encrypt(data["username"])
            date_encrypted = encrypt(str(date_time_obj))
            detail_encrypted = encrypt(str(err))

            # Insert the error
            cursor = database.execute(error.insert.format(
                id_encrypted, username_encrypted, date_encrypted, detail_encrypted))

            database.commit()
            database.close()

            message = {}
            message["message"] = str(err)
            message["status"] = 500

            return message

    def create(self, data):

        try:

            # validate the input
            if 'name' not in data:

                message = {}
                message["message"] = "Please set a name role value"
                message["status"] = 400

                return message

            database = SQL()

            # Get next ID
            cursor = database.execute(role.nextID)
            row = cursor.fetchone()

            id_encrypted = encrypt(str(row[0]))
            name_encrypted = encrypt(data["name"])

            cursor = database.execute(
                role.insert.format(id_encrypted, name_encrypted))

            log_id = str(row[0])

            # Insert the transaction on the Log table
            cursor = database.execute(log.nextID)
            row = cursor.fetchone()

            date_time_str = '2018-06-29 08:15:27.243860'
            date_time_obj = datetime.datetime.strptime(
                date_time_str, '%Y-%m-%d %H:%M:%S.%f')

            id_encrypted = encrypt(str(row[0]))
            username_encrypted = encrypt(data["username"])
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

            message = {}
            message["message"] = "The Role has been created"
            message["status"] = 201

            return message

        except Exception as err:

            database = SQL()

            # Get next ID
            cursor = database.execute(error.nextID)
            row = cursor.fetchone()

            date_time_str = '2018-06-29 08:15:27.243860'
            date_time_obj = datetime.datetime.strptime(
                date_time_str, '%Y-%m-%d %H:%M:%S.%f')

            id_encrypted = encrypt(row[0])
            username_encrypted = encrypt(data["username"])
            date_encrypted = encrypt(str(date_time_obj))
            detail_encrypted = encrypt(str(err))

            # Insert the error
            cursor = database.execute(error.insert.format(
                id_encrypted, username_encrypted, date_encrypted, detail_encrypted))

            database.commit()
            database.close()

            message = {}
            message["message"] = str(err)
            message["status"] = 500

            return message
