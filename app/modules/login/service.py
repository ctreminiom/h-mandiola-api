from app.utils.database import SQL, user, error, log
from app.utils.encryt import encrypt, decrypt
from app.utils.jwt import create

from app.modules.grant.service import Grant
from app.modules.error.service import insertError

import pymssql


class Login:
    def authenticate(self, data):
        try:
            database = SQL()

            cursor = database.execute(
                user.getUser.format(encrypt(data["username"])))
            row = cursor.fetchone()

            if row:
                username, password = decrypt(row[1]), decrypt(row[2])

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

                        if role == 'Administration':
                            token_payload["admin"] = True
                        if role == 'Consecutive':
                            token_payload["consecutive"] = True
                        if role == 'Security':
                            token_payload["security"] = True
                        if role == 'Queries':
                            token_payload["queries"] = True

                    token = create(token_payload)

                    return {'message': token, 'status': 201}

                return {"message": "Username or password incorrect", "status": 400}

        except pymssql.Error as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)
