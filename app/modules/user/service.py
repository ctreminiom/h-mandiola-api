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

            return {'message': user_json, 'status': 200}

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

            return {'message': str(err), 'status': 500}

    def create(self, data):

        try:

            if 'username' not in data: return {'message': 'username file is required', 'status': 400}
            if 'email' not in data: return {'message': 'email file is required', 'status': 400}
            if 'security_question' not in data: return {'message': 'security_question file is required', 'status': 400}
            if 'security_answer' not in data: return {'message': 'security_answer file is required', 'status': 400}

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

            return {'message': "The user has been created", 'status': 201}

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

            return {'message': str(err), 'status': 500}

    def getByUsername(self, data):

        try:
            database = SQL()

            cursor = database.execute(user.getUser.format(encrypt(data["username"])))
            row = cursor.fetchone()

            if not row: return {'message': "The username doesn't exits", 'status': 404}

            result = []
            while row:
                result.append({'id': decrypt(row[0]), 'username': decrypt(row[1]), 'email': decrypt(row[2]), 'security_question': decrypt(row[3])})
                row = cursor.fetchone()

            database.close()

            return {'message': result, 'status': 200}

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

            return {'message': str(err), 'status': 500}
