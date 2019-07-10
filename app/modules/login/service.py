from app.utils.database import SQL, user, error, log
from app.utils.encryt import encrypt, decrypt
from app.utils.jwt import create

from app.modules.grant.service import Grant

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

                    service = Grant()
                    data["jwt_user"] = "admin"

                    message = service.get(data)

                    token_payload = {
                        'user': data["username"],
                        'admin': False,
                        'consecutive': False,
                        'security': False,
                        'queries': False
                    }

                    for i in range(len(message["message"])):

                        role = message["message"][i]["role"]

                        if role == 'Administracion': token_payload["admin"] = True
                        if role == 'consecutive': token_payload["consecutive"] = True
                        if role == 'security': token_payload["security"] = True
                        if role == 'queries': token_payload["queries"] = True

                    token = create(token_payload)

                    return {'message': token, 'status': 201}

                return {"message": "Username or password incorrect", "status": 400}
            
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

            return {"message": str(err), "status": 500}