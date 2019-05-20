#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.service.database import SQL
from app.middleware.encrypt import encode, decode
from config import sequences, insertProcedures, selectViews


class Type:

    def create(self, name):
        handler = SQL()

        try:
            cursor = handler.execute(sequences.consecutive_type)
        except:
            print("ERROR")

        row = cursor.fetchone()

        id_encrypted = encode(str(row[0]))
        name_encypted = encode(name)

        try:
            cursor = handler.execute(
                insertProcedures.consecutive_type.format(id_encrypted, name_encypted))
        except:
            print("ERROR")

        handler.commit()
        handler.close()

        return "New consecutive type created"

    def gets(self):
        handler = SQL()

        try:
            cursor = handler.execute(selectViews.consecutive_type)
        except:
            print("ERROR")

        row = cursor.fetchone()

        result = []
        while row:
            result.append({'name': decode(row[1]), 'id': decode(row[0])})
            row = cursor.fetchone()

        handler.close()

        return result


class Consecutive:

    def create(self, type, description, has_prefix, prefix, has_range, initial, final, consecutive):
        if has_prefix in ['false', 'true']:

            if has_range in ['false', 'true']:
                handler = SQL()

                try:
                    cursor = handler.execute(sequences.consecutive)

                    row = cursor.fetchone()
                    print(row[0])

                    id_encrypted = encode(str(row[0]))
                    type_encryted = encode(type)
                    description_encryted = encode(description)
                    has_prefix_encryted = encode(has_prefix)
                    prefix_encryted = encode(prefix)
                    has_range_encryted = encode(has_range)
                    initial_encryted = encode(initial)
                    final_encryted = encode(final)
                    consecutive_encryted = encode(consecutive)

                    try:
                        cursor = handler.execute(
                            insertProcedures.consecutive.format(id_encrypted, type_encryted, description_encryted, has_prefix_encryted,
                                                                prefix_encryted, has_range_encryted, initial_encryted, final_encryted, consecutive_encryted)
                        )
                    except AssertionError as error:
                        print(error)
                        print("ERROR 1")

                    handler.commit()
                    handler.close()

                    message = {}
                    message["message"] = "New consecutive created"
                    message["status"] = 201

                    return message

                except AssertionError as error:
                    print(error)
                    print("ERROR 2")


        message = {}

        message["message"] = "ERROR"
        message["status"] = 400

        return message
