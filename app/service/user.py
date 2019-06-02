from app.service.database import SQL
from app.middleware.encrypt import encode, decode
from app.middleware.jwt import createToken


from config import procedures, views, sequences


class User:

    def create(self, body):

        try:
            db = SQL()

            # Get next ID value
            cursor = db.execute(sequences.role)
            row = cursor.fetchone()

            id_encrypted = encode(str(row[0]))
            username_encrypted = encode(body["username"])
            email_encrypted = encode(body["email"])
            password_encrypted = encode(body["password"])
            security_question_encrypted = encode(body["security_question"])
            security_answer_encrypted = encode(body["security_answer"])

            # Insert the user
            cursor = db.execute(procedures.insert_user.format(id_encrypted, username_encrypted, email_encrypted,
                                                              password_encrypted, security_question_encrypted, security_answer_encrypted))

            db.commit()
            db.close()

            message = {}
            message["message"] = "new user created!!!!!!"
            message["status"] = 201

            return message

        except AssertionError as error:
            message = {}
            message["message"] = error
            message["status"] = 500

            return message

    def getAll(self):
        try:
            db = SQL()

            # Fetch all users
            cursor = db.execute(views.get_users)

            result = []

            row = cursor.fetchone()
            while row:
                result.append({'id': decode(row[0]), 'username': decode(row[1]), 'email': decode(row[2])})
                row = cursor.fetchone()

            db.close()

            message = {}
            message["message"] = result
            message["status"] = 200

            return message

        except AssertionError as error:

            message = {}
            message["message"] = error
            message["status"] = 500

            return message


    def changePassword(self, body):

        try:
            db = SQL()

            #Get user by username
            cursor = db.execute(procedures.get_user_by_username.format(encode(body["username"])))
            row = cursor.fetchone()

            if not row:
                message = {}
                message["message"] = "The username doesn't exits"
                message["status"] = 400

                return message
            
            #update the password
            cursor = db.execute(procedures.change_user_password.format(encode(body["username"]), encode(body["new_password"])))

            db.commit()
            db.close()

            message = {}
            message["message"] = "The password have been changed!!"
            message["status"] = 201

            return message

        except AssertionError as error:

            message = {}
            message["message"] = error
            message["status"] = 500

            return message

    def getByUsername(self, username):

        try:
            db = SQL()

            #Get user by username
            cursor = db.execute(procedures.get_user_by_username.format(encode(username)))
            row = cursor.fetchone()

            if not row:
                message = {}
                message["message"] = "The username doesn't exits"
                message["status"] = 400

            result = []
            while row:
                result.append({'id': decode(row[0]), 'username': decode(row[1]), 'email': decode(row[2])})
                row = cursor.fetchone()

            db.close()

            message = {}
            message["message"] = result
            message["status"] = 200

            return message

        except AssertionError as error:
            message = {}
            message["message"] = error
            message["status"] = 500

            return message


    def login(self, body):

        try:
            db = SQL()

            #Get user by username
            cursor = db.execute(procedures.get_user_by_username.format(encode(body["user"])))
            row = cursor.fetchone()

            if row:

                username = decode(row[1])
                password = decode(row[3])


                if username == body["user"] and password == body["password"]:

                    token = createToken(body["user"])

                    message = {}
                    message["message"] = token
                    message["status"] = 201

                    return message

            

            #Get user by email
            cursor = db.execute(procedures.get_user_by_email.format(encode(body["user"])))
            row = cursor.fetchone()

            if row:

                email = decode(row[2])
                password = decode(row[3])

                if encode(email) == body["user"] and encode(password) == body["password"]:

                    token = createToken(body["user"])

                    message = {}
                    message["message"] = token
                    message["status"] = 201

                    return message
            

            message = {}
            message["message"] = "username or password incorrect"
            message["status"] = 400

            return message

        except AssertionError as error:
            message = {}
            message["message"] = error
            message["status"] = 500

            return message
