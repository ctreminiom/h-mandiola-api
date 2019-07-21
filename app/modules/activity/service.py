from app.utils.database import SQL, activity, consecutive, error, log
from app.utils.encryt import encrypt, decrypt

from app.modules.error.service import insertError
from app.modules.log.service import insertLog
from app.modules.consecutive.service import Consecutive
from app.utils.storage import upload_blob

import datetime, pymssql, os
from config import configuration

from werkzeug.utils import secure_filename


class Activity:
    def gets(self,data):
        try:
            database = SQL()
            cursor = database.execute(activity.getAll)

            result = []
            row = cursor.fetchone()

            while row:

                result.append({'id': decrypt(row[0]),
                               'consecutive': decrypt(row[1]),
                               'code': decrypt(row[2]),
                               'sum': decrypt(row[3]),
                               'name': decrypt(row[4]),
                               'description': decrypt(row[5]),
                               'image_path': decrypt(row[6]),
                               })

                row = cursor.fetchone()

            database.close()

            return {'message': result, 'status': 200}
        except pymssql.Error as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)

    def create(self, data):
        try:
            database = SQL()

            cursor = database.execute(activity.nextID)
            row = cursor.fetchone()

            id = encrypt(str(row[0]))
            consecutive = encrypt(data["consecutive"])

            #Get the consecutive code
            service = Consecutive()
            consecutive_query = {"jwt_user": "internal", "id": data["consecutive"]}
            message = service.get(consecutive_query)

            if message["status"] == 404:
                return message

            consecutive_code = encrypt(message["message"][0]["prefix"])
            consecutive_num = encrypt(str(row[0]))

            print("-------------")
            print(data['name'])
            print("-------------")

            name = encrypt(data["name"])
            description = encrypt(data["description"])

            
            #Process the image
            file = data["image_path"]
            image_location = ""

            if file and allowed_file(file.filename):

                image_type = file.filename.rsplit('.', 1)[1].lower()

                file_name = secure_filename("activity-{}.{}".format(id, image_type))
                print(file_name)

                path = os.path.join(os.environ["ASSETS_PATH"], file_name)
                print(path)

                file.save(path)

                test = "activities/{}".format(file_name)

                image_location = upload_blob("h-mandiola-files",path, test)
                print("------------")
                print(image_location)
                print("------------")


            image_path = encrypt(image_location)


            query = activity.insert.format(id, consecutive, consecutive_code, consecutive_num, name, description, image_path)
            print(query)
            cursor = database.execute(query)

            context = {
                "database": database,
                "jwt_user": data["jwt_user"],
                "code": "INSERT",
                "table": "dbo.Activities",
                "id": str(row[0]),
                "user": data["jwt_user"]
            }

            insertLog(context)

            database.commit()
            database.close()

            return {'message': 'The activity has been created', 'status': 201}

        except pymssql.Error as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)










def allowed_file(filename):
    print(filename.rsplit('.', 1)[1].lower())
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in configuration.allowed_extensions