import pymssql
from app.service.database import SQL
from app.middleware.encrypt import encode, decode
from config import sequences, views, procedures


class Activity:


    def create(self, body):
        try:
            db = SQL()

            #Get next ID value
            cursor = db.execute(sequences.activity)
            row = cursor.fetchone()

            id_encrypted = encode(str(row[0]))
            consecutive_encrypted = encode(body["consecutive"])
            name_encrypted = encode(body["name"])
            description_encrypted = encode(body["description"])
            image_path_encrypted = encode(body["image_path"])


            #Insert the activity
            cursor = db.execute(procedures.insert_activity.format(id_encrypted, consecutive_encrypted, name_encrypted, description_encrypted, image_path_encrypted))


            db.commit()
            db.close()

            message = {}
            message["message"] = "new activity created!!!!"
            message["status"] = 201

            return message


        except pymssql.InternalError as error:
            message = {}
            message["message"] = error
            message["status"] = 500

            return message


    def getAll(self):
        try:
            db = SQL()


            #Fetch all activities
            cursor = db.execute(views.get_activities)


            #Iterate the rows and decode it
            result = []

            row = cursor.fetchone()
            
            while row:
                result.append({'id': decode(row[0]), 'consecutive': decode(row[1]), 'name': decode(row[2]), 'description': decode(row[3]), 'image_path': decode(row[4]) })
                row = cursor.fetchone()

            db.close()

            message = {}
            message["message"] = result
            message["status"] = 200

            return message


        except pymssql.InternalError as error:
            message = {}
            message["message"] = error
            message["status"] = 500

            return message
