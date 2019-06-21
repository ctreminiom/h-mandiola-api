import datetime

from app.utils.database import SQL, logs, errors
from app.utils.encrypt import decode, encode


class Log:

    def getAll(self, data):
        try:
            database = SQL()


            #Get all consecutive types
            cursor = database.execute(logs.getAll)

            log = []

            row = cursor.fetchone()
            while row:
                log.append( {'username': decode(row[1]),
                'id': decode(row[0]), 
                'date': decode(row[2]), 
                'code': decode(row[3]),
                'detail': decode(row[4])
                })

                row = cursor.fetchone()

            database.close()

            message = {}
            message["message"] = log
            message["status"] = 200

            return message

        except Exception as error:
            
            database = SQL()

            # Get next error value
            cursor = database.execute(errors.nextID)
            row = cursor.fetchone()


            date_time_str = '2018-06-29 08:15:27.243860'  
            date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')


            id_encrypted = encode(str(row[0]))
            username_encrypted = encode(data["username"])
            date_encrypted = encode(str(date_time_obj))
            detail_encrypted = encode(str(error))


            #Insert the error
            cursor = database.execute(errors.insert.format(id_encrypted, username_encrypted, date_encrypted,
            detail_encrypted))

            database.commit()
            database.close()

            message = {}
            message["message"] = str(error)
            message["status"] = 500

            return message

