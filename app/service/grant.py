import pymssql
from app.service.database import SQL
from app.middleware.encrypt import encode, decode

from config import sequences, views, procedures



class Grant:


    def create(self, body):

        try:
            db = SQL()

            #Get next ID value
            cursor = db.execute(sequences.grant)
            row = cursor.fetchone()

            id_encrypted = encode(str(row[0]))
            user_encryted = encode(body["user"])
            role_encrypted = encode(body["role"])


            #Insert the grant
            cursor = db.execute(procedures.insert_grant.format(id_encrypted, user_encryted, role_encrypted))

            db.commit()
            db.close()

            message = {}
            message["message"] = "new grant created!!!!"
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

            #Fetch all roles
            cursor = db.execute(views.get_grants)


            #Iterate the rows and encode it
            result = []

            row = cursor.fetchone()
            while row:
                result.append({'id': decode(row[0]), 'user': decode(row[1]), 'role': decode(row[2])})
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

    def remove(self, body):

        try:
            db = SQL()

            #Get grant by User and Role
            cursor = db.execute(procedures.get_grant_by_user_and_role.format(encode(body["user"]), encode(body["role"])))
            row = cursor.fetchone()

            if not row:
                message = {}
                message["message"] = "The grant doesn't exits"
                message["status"] = 404

                return message


            #Delete grant
            db.execute(procedures.remove_grant.format(encode(body["user"]), encode(body["role"])))

            db.commit()
            db.close()

            message = {}
            message["message"] = "Grant removed!!"
            message["status"] = 392

            return message

        except pymssql.InternalError as error:

            message = {}
            message["message"] = error
            message["status"] = 500

            return message