from app.utils.database import SQL, log, error
from app.utils.encryt import encrypt, decrypt

import pymssql, datetime

class Error:

    def getAll(self, data):

        try:

            database = SQL()

            # Get all logs encrypted
            cursor = database.execute(error.getAll)

            error_json = []

            row = cursor.fetchone()
            while row:

                error_json.append({'username': decrypt(row[1]),
                                 'id': decrypt(row[0]),
                                 'date': decrypt(row[2]),
                                 'detail': decrypt(row[3])
                                 })

                row = cursor.fetchone()

            database.close()

            return {'message': error_json, 'status': 200}

        except pymssql.Error as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)


def insertError(context):

    database = context["database"]

    cursor = database.execute(error.nextID)
    row = cursor.fetchone()

    id = encrypt(str(row[0]))
    username = encrypt(context["jwt_user"])
    date = encrypt(datetime.datetime.now().replace(microsecond=0).isoformat())

    err = context["err"]
    detail = encrypt(str(err))

    cursor = database.execute(error.insert.format(id,username,date,detail))

    database.commit()
    database.close()

    return {'message': str(err), 'status': 500}
