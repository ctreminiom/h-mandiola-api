from app.utils.database import SQL, user, error, log
from app.utils.encryt import encrypt, decrypt
from app.utils.jwt import create

import datetime, pymssql



class Login:


    def authenticate(self, data):

        try:
            database = SQL()

            #Get user by username
            cursor = database.execute(user.getUser.format(encrypt(data["username"])))
            row = cursor.fetchone()

            if row:
                username, password = decrypt(row[1]), decrypt(row[2])

                print(username, password)

                if username == data["username"] and password == data["password"]:

                    token_payload = {
                        'user': data["username"],
                        'admin': True,
                        'consecutive': True,
                        'security': True,
                        'queries': True
                    }

                    print("-----------------------")
                    print(token_payload)
                    print("-----------------------")

                    token = create(token_payload)

                    message = {"message": token, "status": 201}
                    return message

                message = {"message": "Username or password incorrect", "status": 400}
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
            username_encrypted = encrypt("login_user")
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