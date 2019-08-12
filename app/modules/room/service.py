from app.utils.database import SQL, room, consecutive
from app.utils.encryt import encrypt, decrypt

from app.modules.error.service import insertError
from app.modules.log.service import insertLog
from app.modules.consecutive.service import Consecutive

from app.utils.storage import upload_blob
from werkzeug.utils import secure_filename
from config import configuration
import pymssql, os


class Room:

    def gets(self, data):
        try:
            database = SQL()
            cursor = database.execute(room.getAll)

            result = []
            row = cursor.fetchone()
            while row:
                result.append({
                    'id': decrypt(row[0]),
                    'consecutive': decrypt(row[1]),
                    'prefix': decrypt(row[2]),
                    'consecutive_num': decrypt(row[3]),
                    'room_type_name': decrypt(row[4]),
                    'number': decrypt(row[5]),
                    'description': decrypt(row[6]),
                    'available': decrypt(row[7]),
                    'image_path': decrypt(row[8]),
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
            print(data)
            database = SQL()

            cursor = database.execute(room.nextID)
            row = cursor.fetchone()

            id = encrypt(str(row[0]))
            consecutive = encrypt(data['consecutive'])

            #Get the consecutive code
            service = Consecutive()
            consecutive_query = {"jwt_user": "internal", "id": data["consecutive"]}
            message = service.get(consecutive_query)

            if message["status"] == 404:
                return message

            prefix = encrypt(message["message"][0]["prefix"])
            consecutive_num = encrypt(str(row[0]))

            room_type_ID = encrypt(data['room_type_ID'])

            number = encrypt(data['number'])
            description = encrypt(data['description'])
            available = encrypt(data['available'])

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

                test = "rooms/{}".format(file_name)

                image_location = upload_blob("h-mandiola-files",path, test)
                os.remove(path)

            image_path = encrypt(image_location)


            query = room.insert.format(id, consecutive, prefix, consecutive_num, room_type_ID, number, description, available, image_path)
            cursor = database.execute(query)

            context = {
                "database": database,
                "jwt_user": data["jwt_user"],
                "code": "INSERT",
                "table": "dbo.Rooms",
                "id": str(row[0]),
                "user": data["jwt_user"]
            }

            insertLog(context)

            database.commit()
            database.close()

            return {'message': "The room has been created", 'status': 201}

        except pymssql.Error as err:
            context = {"database": database,
                       "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)


    def delete(self, data):
        try:
            database = SQL()

            query = room.deleteRoom.format(encrypt(data['id']))
            database.execute(query)

            context = {
                "database": database,
                "jwt_user": data["jwt_user"],
                "code": "DELETE",
                "table": "dbo.Rooms",
                "id": "PASSWORD",
                "user": data["jwt_user"]
            }

            insertLog(context)

            database.commit()
            database.close()

            return {'message': "The room has been removed", 'status': 201}

        except pymssql.Error as err:
            context = {"database": database,
                    "jwt_user": data["jwt_user"], "err": err}
            return insertError(context)



def allowed_file(filename):
    print(filename.rsplit('.', 1)[1].lower())
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in configuration.allowed_extensions