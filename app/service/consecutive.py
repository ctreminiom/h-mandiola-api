#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.service.database import SQL
from app.middleware.encrypt import encode, decode

from config import sequences, procedures, views


class Type:
    def create(self, name):
        try:
            db = SQL()

            # Get next ID value
            cursor = db.execute(sequences.consecutive_type)
            row = cursor.fetchone()

            id_encrypted = encode(str(row[0]))
            name_encypted = encode(name)

            # Insert the info
            cursor = db.execute(procedures.insert_consecutive_type.format(
                id_encrypted, name_encypted))

            db.commit()
            db.close()

            message = {}
            message["message"] = "new consecutive type created!!"
            message["status"] = 201

            return message

        except AssertionError as error:
            print(error)

            message = {}
            message["message"] = error
            message["status"] = 500

            return message

    def getAll(self):
        try:
            db = SQL()

            # Fetch all info
            cursor = db.execute(views.gets_consecutives_types)

            # Iterate the rows and encode it.
            result = []

            row = cursor.fetchone()
            while row:
                result.append({'name': decode(row[1]), 'id': decode(row[0])})
                row = cursor.fetchone()

            db.close()

            message = {}
            message["message"] = result
            message["status"] = 200

            return message

        except AssertionError as error:
            print(error)

            message = {}
            message["message"] = error
            message["status"] = 500

            return message


class Consecutive:
    def create(self, body):
        try:

            if body["has_prefix"] in ['false', 'true']:

                if body["has_range"] in ['false', 'true']:

                    db = SQL()

                    # Get next ID value
                    cursor = db.execute(sequences.consecutive)
                    row = cursor.fetchone()

                    id_encrypted = encode(str(row[0]))
                    type_encryted = encode(body["type"])
                    description_encryted = encode(body["description"])
                    has_prefix_encryted = encode(body["has_prefix"])
                    prefix_encryted = encode(body["prefix"])
                    has_range_encryted = encode(body["has_range"])
                    initial_encryted = encode(body["initial"])
                    final_encryted = encode(body["final"])
                    consecutive_encryted = encode(body["consecutive"])

                    cursor = db.execute(
                        procedures.insert_consecutive.format(id_encrypted, type_encryted, description_encryted, has_prefix_encryted,
                                                             prefix_encryted, has_range_encryted, initial_encryted, final_encryted, consecutive_encryted)
                    )

                    db.commit()
                    db.close()

                    message = {}
                    message["message"] = "New consecutive created"
                    message["status"] = 201

                    return message

                else:
                    message = {}
                    message["message"] = "The has_range field doesn't allow this value"
                    message["status"] = 400

                    return message

            else:
                message = {}
                message["message"] = "The has_prefix value doesn't allowed"
                message["status"] = 400

                return message

        except AssertionError as error:
            print(error)

            message = {}
            message["message"] = error
            message["status"] = 500

            return message

    def getAll(self):
            try:
                db = SQL()

                # Fetch all info
                cursor = db.execute(views.gets_consecutives)

                # Iterate the rows and encode it.
                result = []

                row = cursor.fetchone()
                while row:

                    result.append({

                        'id': decode(row[0]),
                        'type': decode(row[1]),
                        'description': decode(row[2]),
                        'has_prefix': decode(row[3]),
                        'prefix': decode(row[4]),
                        'has_range': decode(row[5]),
                        'initial': decode(row[6]),
                        'final': decode(row[7]),
                        'consecutive': decode(row[8])
                    })
                    row = cursor.fetchone()

                db.close()

                message = {}
                message["message"] = result
                message["status"] = 200

                return message

            except AssertionError as error:
                print(error)

                message = {}
                message["message"] = error
                message["status"] = 500

                return message

    def update(self, id, body):

        try:
            db = SQL()

            #Get consecutive by ID
            cursor = db.execute(procedures.get_actual_consecutive.format(encode(id)))

            row = cursor.fetchone()

            if not row:
                message = {}
                message["message"] = "The consecutive doesn't exits"
                message["status"] = 404

                return message

            prefix_on_the_db = decode(row[0])
            if 'prefix' in body and body["prefix"] == "" and body["has_prefix"] == "true" and prefix_on_the_db == 'true':
                message = {}
                message["message"] = "You cannot remove the prefix if the prefix is set as true"
                message["status"] = 400
                
                return message


            consecutive_on_the_db = decode(row[5])

            print(consecutive_on_the_db)

            if 'final' in body and int(consecutive_on_the_db) >= int(body["final"]):

                message = {}
                message["message"] = "You cannot add this final value because this value overwrite the actual consecutive value"
                message["status"] = 400

                return message


            if 'final' in body and int(consecutive_on_the_db) > int(body["final"]):
                cursor = db.execute(procedures.update_final_consecutive_value.format(encode(id), encode(body["final"])))

                db.commit()


            
            if 'has_range' in body and body["has_range"] == "false":

                ranges_value = encode("null")
                cursor = db.execute(procedures.update_consecutive_ranges.format(encode(id), ranges_value, ranges_value))

                db.commit()



            db.close()

            message = {}
            message["message"] = "Consecutive updated"
            message["status"] = 200

            return message


        except AssertionError as error:
            message = {}
            message["message"] = error
            message["status"] = 500

            return message

    def increase(self, id):
        try:
            db = SQL()

            #Get consecutive by ID
            cursor = db.execute(procedures.get_actual_consecutive.format(encode(id)))

            row = cursor.fetchone()

            if not row:
                message = {}
                message["message"] = "The consecutive doesn't exists"
                message["status"] = 400

                return message


            has_range = decode(row[2])

            if has_range == "true":

                actual_consecutive = decode(row[5])

                initial_as_int = int(decode(row[3]))
                final_as_int = int(decode(row[4]))

                if initial_as_int > int(actual_consecutive) + 1:

                    message = {}
                    message["message"] = "The next consecutive value is bigger than the initial value"
                    message["status"] = 400

                    return message

                if final_as_int <= int(actual_consecutive) + 1:
                    message = {}
                    message["message"] = "The next consecutive value is bigger than the final value"
                    message["status"] = 400

                    return message

                #increase consecutive with range
                new_consecutive = int(actual_consecutive) + 1

                cursor = db.execute(procedures.increase_consecutive.format(encode(str(new_consecutive)), encode(id)))

                db.commit()
                db.close()

                message = {}
                message["message"] = "Consecutive increased!"
                message["status"] = 201
                
                return message


            if has_range == "false":

                #increase consecutive without range
                new_consecutive = int(actual_consecutive) + 1

                new_consecutive_as_string = str(new_consecutive)

                cursor = db.execute(procedures.increase_consecutive.format(encode(new_consecutive_as_string),encode(id)))
                db.commit()
                db.close()


                message = {}
                message["message"] = "Consecutive increased!"
                message["status"] = 201
                
                return message

            

            db.close()

            message = {}
            message["message"] = "ASD"
            message["status"] = 200

            return message


        except AssertionError as error:
            message = {}
            message["message"] = error
            message["status"] = 500

            return message




        
