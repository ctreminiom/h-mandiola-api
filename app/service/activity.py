import pymssql
from app.service.database import SQL
from app.middleware.encrypt import encode, decode
from config import sequences, views, procedures, config

import os
from werkzeug.utils import secure_filename


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


            #save image
            file = body['image_path']

            if file and allowed_file(file.filename):

                image_type = file.filename.rsplit('.', 1)[1].lower()

                file_name = secure_filename("activity-{}.{}".format(id_encrypted, image_type))

                path = os.path.join(config.upload_folder, file_name)

                file.save(path)

                image_path_encrypted = encode(path)

                #Insert the activity
                cursor = db.execute(procedures.insert_activity.format(id_encrypted, consecutive_encrypted, name_encrypted, description_encrypted, image_path_encrypted))

                db.commit()
                db.close()

                message = {}
                message["message"] = "new activity created!!!!"
                message["status"] = 201

                return message

            
            message = {}
            message["message"] = "Invalid image format"
            message["status"] = 400

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

    def remove(self, id):
        try:
            db = SQL()

            #Get activity by ID
            cursor = db.execute(procedures.get_activity_by_ID.format(encode(id)))
            row = cursor.fetchone()

            if not row:
                message = {}
                message["message"] = "The activity doesn't exits"
                message["status"] = 404

                return message

            #Delete grant
            db.execute(procedures.remove_activity.format(encode(id)))

            db.commit()
            db.close()

            message = {}
            message["message"] = "activity removed!!"
            message["status"] = 392

            return message

        except pymssql.InternalError as error:

            message = {}
            message["message"] = error
            message["status"] = 500

            return message

    def update(self, body, id):
        try:
            db = SQL()
            
            #Get activity by ID
            cursor = db.execute(procedures.get_activity_by_ID.format(encode(id)))
            row = cursor.fetchone()

            if not row:
                message = {}
                message["message"] = "The activity doesn't exits"
                message["status"] = 404

                return message

            if 'name' in body:
                cursor = db.execute(procedures.update_activity_name.format(encode(id), encode(body["name"])))
                db.commit()

            if 'description' in body:
                cursor = db.execute(procedures.update_activity_description.format(encode(id), encode(body["description"])))
                db.commit()

            db.close()

            message = {}
            message["message"] = "activity updated!!"
            message["status"] = 201

            return message

        except pymssql.InternalError as error:

            message = {}
            message["message"] = error
            message["status"] = 500

            return message

    def updateImage(self, body, id):
        try:
            db = SQL()
            
            #Get activity by ID
            cursor = db.execute(procedures.get_activity_by_ID.format(encode(id)))
            row = cursor.fetchone()

            if not row:
                message = {}
                message["message"] = "The activity doesn't exits"
                message["status"] = 404

                return message

            new_image = body["image_path"]

            if new_image and allowed_file(new_image.filename):

                #delete the actual image
                actual_image_path = decode(row[4])
                os.remove(actual_image_path)

                image_type = new_image.filename.rsplit('.', 1)[1].lower()

                file_name = secure_filename("activity-{}.{}".format(row[0], image_type))

                path = os.path.join(config.upload_folder, file_name)
                image_type.save(path)

                image_path_encrypted = encode(path)

                cursor = db.execute(procedures.update_activity_image.format(row[0], image_path_encrypted))

                db.commit()
                db.close()

                message = {}
                message["message"] = "The image has been changed!!!"
                message["status"] = 202

                return message

            
            message = {}
            message["message"] = "Invalid image format"
            message["status"] = 400

            return message
            
        except pymssql.InternalError as error:

            message = {}
            message["message"] = error
            message["status"] = 500

            return message





def allowed_file(filename):
    print(filename.rsplit('.', 1)[1].lower())
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in config.allowed_extensions