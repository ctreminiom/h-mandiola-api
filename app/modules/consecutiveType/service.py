import datetime

from app.utils.database import SQL, consecutive_type, errors, logs
from app.utils.encrypt import encode, decode


class ConsecutiveType:

    def create(self, data):
        try:

            database = SQL()

            # Get next consecutive value
            cursor = database.execute(consecutive_type.nextID)
            row = cursor.fetchone()

            id_encrypted = encode(str(row[0]))
            name_encypted = encode(data["name"])

            # insert the consecutive type
            cursor = database.execute(consecutive_type.insert.format(id_encrypted, name_encypted))

            #Insert the transiction on the Log table
            cursor = database.execute(logs.nextID)
            row = cursor.fetchone()

            date_time_str = '2018-06-29 08:15:27.243860'  
            date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')


            id_encrypted = encode(str(row[0]))
            username_encrypted = encode(data["username"])
            date_encrypted = encode(str(date_time_obj))
            code_encrypted = encode("INSERT")
            detail_encrypted = encode("The consecutive type {} has been created".format(data["name"]))

            #Insert the Log
            cursor = database.execute(logs.insert.format(id_encrypted, username_encrypted, date_encrypted, code_encrypted,detail_encrypted))

            database.commit()
            database.close()

            message = {}
            message["message"] = "The consecutive type {} has been created".format(data["name"])
            message["status"] = 201

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

    def getAll(self, data):
        try:
            database = SQL()


            #Get all consecutive types
            cursor = database.execute(consecutive_type.getAll)

            consecutives = []

            row = cursor.fetchone()
            while row:
                consecutives.append({'name': decode(row[1]), 'id': decode(row[0])})
                row = cursor.fetchone()

            database.close()

            message = {}
            message["message"] = consecutives
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
            date_encrypted = encode(date_time_obj)
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
