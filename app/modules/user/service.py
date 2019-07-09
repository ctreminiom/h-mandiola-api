from app.utils.database import SQL, user, error, log
from app.utils.encryt import encrypt, decrypt

import datetime, pymssql



class User:

    def getAll(self, data):

        try:
            database = SQL()

            # Get all logs encrypted
            cursor = database.execute(user.getAll)

            user_json = []

            row = cursor.fetchone()
            while row:

                user_json.append({'id': decrypt(row[0]),
                                  'username': decrypt(row[1]),
                                  'email': decrypt(row[2]),
                                  'security_question': decrypt(row[3]),
                                  })

                row = cursor.fetchone()

            database.close()

            message = {}
            message["message"] = user_json
            message["status"] = 200

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

            # validate the input
            if 'username' not in data:

                message = {}
                message["message"] = "Please set a username role value"
                message["status"] = 400

                return message

            if 'email' not in data:

                message = {}
                message["message"] = "Please set a email role value"
                message["status"] = 400

                return message

            if 'password' not in data:

                message = {}
                message["message"] = "Please set a password role value"
                message["status"] = 400

                return message

            if 'security_question' not in data:

                message = {}
                message["message"] = "Please set a security_question role value"
                message["status"] = 400

                return message

            if 'security_answer' not in data:

                message = {}
                message["message"] = "Please set a security_answer role value"
                message["status"] = 400

                return message

            database = SQL()

            # Get next ID
            cursor = database.execute(user.nextID)
            row = cursor.fetchone()

            id_encrypted = encrypt(str(row[0]))
            username_encrypted = encrypt(data["username"])
            email_encrypted = encrypt(data["email"])
            password_encrypted = encrypt(data["password"])
            security_question_encrypted = encrypt(data["security_question"])
            security_answer_encrypted = encrypt(data["security_answer"])

            cursor = database.execute(user.insert.format(id_encrypted, username_encrypted, email_encrypted,
                                                         password_encrypted, security_question_encrypted, security_answer_encrypted))

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
                "User", log_id, data["username"])
            detail_encrypted = encrypt(detail_message)

            # Insert the log
            cursor = database.execute(log.insert.format(
                id_encrypted, username_encrypted, code_encrypted, date_encrypted, detail_encrypted))

            database.commit()
            database.close()

            message = {}
            message["message"] = "The User has been created"
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

            id_encrypted = encrypt(str(row[0]))
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

    def getByUsername(self, data):

        try:
            database = SQL()

            # Get all logs encrypted
            cursor = database.execute(
                user.getAll.format(encrypt(data["username"])))
            row = cursor.fetchone()

            if not row:
                message = {}
                message["message"] = "The username doesn't exits"
                message["status"] = 404

                return message

            result = []
            while row:
                result.append({'id': decrypt(row[0]), 'username': decrypt(row[1]), 'email': decrypt(row[2]), 'security_question': decrypt(row[3])})
                row = cursor.fetchone()

            data.close()

            message = {}
            message["message"] = result
            message["status"] = 200

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
