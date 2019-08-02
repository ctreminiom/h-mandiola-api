from app.utils.database import SQL, log, error
from app.utils.encryt import encrypt, decrypt
from app.modules.error.service import insertError


import datetime, pymssql


class Log:

    def getAll(self, data):
        try:
            database = SQL()
            cursor = database.execute(log.getAll)

            result = []
            row = cursor.fetchone()
            while row:

                result.append({'username': decrypt(row[1]),
                                 'id': decrypt(row[0]),
                                 'date': decrypt(row[2]),
                                 'code': decrypt(row[3]),
                                 'detail': decrypt(row[4])
                                 })

                row = cursor.fetchone()

            database.close()

            return {'message': result, 'status': 200}

        except pymssql.Error as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)


def insertLog(context):

    database = context["database"]

    cursor = database.execute(log.nextID)
    row = cursor.fetchone()

    id = encrypt(str(row[0]))
    username = encrypt(context["jwt_user"])
    date = encrypt(datetime.datetime.now().replace(microsecond=0).isoformat())
    code = encrypt(context["code"])

    message = "Table = {} || ID = {} || User = {}"
    detail = encrypt(message.format(context["table"], context["id"], context["user"]))


    cursor = database.execute(log.insert.format(id, username, code, date, detail))

