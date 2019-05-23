from app.service.database import SQL
from app.middleware.encrypt import encode, decode


from config import sequences, views, procedures



class Role:

    def create(self, name):
        try:
            db = SQL()

            # Get next ID value
            cursor = db.execute(sequences.role)
            row = cursor.fetchone()

            id_encrypted = encode(str(row[0]))
            name_encryped = encode(name)


            #Insert to info
            cursor = db.execute(procedures.insert_role.format(id_encrypted, name_encryped))

            db.commit()
            db.close()


            message = {}
            message["message"] = "new role created!!!!"
            message["status"] = 201

            return message

        except AssertionError as error:
            message = {}
            message["message"] = error
            message["status"] = 500

            return message

    def getAll(self):
        try:
            db = SQL()

            #Fetch all roles
            cursor = db.execute(views.get_roles)


            #Iterate the rows and encode it
            result = []

            row = cursor.fetchone()
            while row:
                result.append({'id': decode(row[0]), 'name': decode(row[1])})
                row = cursor.fetchone()

            db.close()

            message = {}
            message["message"] = result
            message["status"] = 200

            return message

        except AssertionError as error:
            message = {}
            message["message"] = error
            message["status"] = 500

            return message