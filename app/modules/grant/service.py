from app.utils.database import SQL, grant, error, log
from app.utils.encryt import encrypt, decrypt

import datetime, pymssql


class Grant:

    def get(self, data):

        try:
            if 'username' not in data:

                message = {"message": "Please set a username role value", "status": 400}
                return message
            
            database = SQL()
            cursor = database.execute(grant.getGrant.format(encrypt(data["username"])))

            grant_json = []

            row = cursor.fetchone()
            while row:
                grant_json.append({'id': decrypt(row[0]), 'user': decrypt(row[1]), 'role': decrypt(row[2])})
                row = cursor.fetchone()

            database.close()

            message = {"message": grant_json, "status": 200}
            return message

        except pymssql.Error as err:

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

            message = {}
            message["message"] = str(err)
            message["status"] = 500

            return message

    def create(self, data):
        try:
            database = SQL()

            # Get next ID
            cursor = database.execute(grant.nextID)
            row = cursor.fetchone()

            id_encrypted = encrypt(str(row[0]))
            user_encrypted = encrypt(data["username"])
            role_encrypted = encrypt(data["role"])

            cursor = database.execute(grant.insert.format(id_encrypted, user_encrypted, role_encrypted))

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
                "Grant", log_id, data["username"])
            detail_encrypted = encrypt(detail_message)

            # Insert the log
            cursor = database.execute(log.insert.format(
                id_encrypted, username_encrypted, code_encrypted, date_encrypted, detail_encrypted))

            database.commit()
            database.close()

            message = {}
            message["message"] = "The Grant has been created"
            message["status"] = 201

            return message


        except pymssql.Error as err:
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

            message = {"message": str(err), "status": 500}
            return message


    def remove(self, data):
        try:
            database = SQL()

            database.execute(grant.removeGrant.format(encrypt(data["username"]), encrypt(data["role"])))
            database.commit()
            database.close()

            message = {"message": "Grant removedd", "status": 202}
            return message


        except pymssql.Error as err:
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

            message = {"message": str(err), "status": 500}
            return message
