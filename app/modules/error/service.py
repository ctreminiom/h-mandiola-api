from app.utils.database import SQL, log, error
from app.utils.encryt import encrypt, decrypt

import datetime


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

            return {'message': str(err), 'status': 500}
