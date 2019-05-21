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
