import datetime

from app.utils.database import SQL, consecutive, errors, logs
from app.utils.encrypt import encode, decode


class Consecutive:

    def create(self, data):
        try:
            database = SQL()

            # Get next consecutive
            cursor = database.execute(consecutive.nextID)
            row = cursor.fetchone()

            id_encrypted = encode(str(row[0]))
            type_encryted = encode(data["type"])
            description_encryted = encode(data["description"])
            has_prefix_encryted = encode(data["has_prefix"])
            prefix_encryted = encode(data["prefix"])
            has_range_encryted = encode(data["has_range"])
            initial_encryted = encode(data["initial"])
            final_encryted = encode(data["final"])
            consecutive_encryted = encode(data["consecutive"])

            # Insert the consecutive
            cursor = database.execute(consecutive.insert.format(id_encrypted, type_encryted, description_encryted, has_prefix_encryted, prefix_encryted,
                                                                has_range_encryted, initial_encryted, final_encryted, consecutive_encryted))

            # Insert the transiction on the Log table
            cursor = database.execute(logs.nextID)
            row = cursor.fetchone()

            date_time_str = '2018-06-29 08:15:27.243860'
            date_time_obj = datetime.datetime.strptime(
                date_time_str, '%Y-%m-%d %H:%M:%S.%f')

            id_encrypted = encode(str(row[0]))
            username_encrypted = encode(data["username"])
            date_encrypted = encode(str(date_time_obj))
            code_encrypted = encode("INSERT")
            detail_encrypted = encode("The consecutive has been created")

            # Insert the Log
            cursor = database.execute(logs.insert.format(
                id_encrypted, username_encrypted, date_encrypted, code_encrypted, detail_encrypted))

            database.commit()
            database.close()

            message = {}
            message["message"] = "The consecutive has been created"
            message["status"] = 201

            return message

        except Exception as error:

            database = SQL()

            # Get next error value
            cursor = database.execute(errors.nextID)
            row = cursor.fetchone()

            date_time_str = '2018-06-29 08:15:27.243860'
            date_time_obj = datetime.datetime.strptime(
                date_time_str, '%Y-%m-%d %H:%M:%S.%f')

            id_encrypted = encode(str(row[0]))
            username_encrypted = encode(data["username"])
            date_encrypted = encode(str(date_time_obj))
            detail_encrypted = encode(str(error))

            # Insert the error
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

            # Get all consecutive
            cursor = database.execute(consecutive.getAll)

            consecutives = []

            row = cursor.fetchone()
            while row:
                consecutives.append({

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
            date_time_obj = datetime.datetime.strptime(
                date_time_str, '%Y-%m-%d %H:%M:%S.%f')

            id_encrypted = encode(str(row[0]))
            username_encrypted = encode(data["username"])
            date_encrypted = encode(str(date_time_obj))
            detail_encrypted = encode(str(error))

            # Insert the error
            cursor = database.execute(errors.insert.format(id_encrypted, username_encrypted, date_encrypted,
                                                           detail_encrypted))

            database.commit()
            database.close()

            message = {}
            message["message"] = str(error)
            message["status"] = 500

            return message

    def update(self, id, data):
        try:
            database = SQL()

            #Get consecutive by ID
            cursor = database.execute(consecutive.consecutive.format(encode(id)))

            row = cursor.fetchone()

            if not row:
                message = {}
                message["message"] = "The consecutive doesn't exits"
                message["status"] = 404

                return message


            if 'prefix' in data:

                has_prefix = decode(row[3])

                if has_prefix == "true":
                    #update the prefix
                    cursor = database.execute(consecutive.update_prefix_value.format(encode(id), encode(data["prefix"])))
                else:
                    message = {}
                    message["message"] = "The consecutive prefix cannot be changed because the value has_prefix is false"
                    message["status"] = 400

                    return message


            if 'has_prefix' in data:

                has_prefix = decode(row[3])
                prefix = decode(row[4])
                actual_consecutive = decode(row[8])

                if data['has_prefix'] in ("true", "false"):

                    if 'has_prefix' == "false" and len(prefix) < 0:
                        message = {}
                        message["message"] = "The consecutive has_prefix cannot be changed because the value prefix has a value"
                        message["status"] = 400

                        return message

                    if 'has_prefix' == 'true' and len(prefix) < 0:
                        #update the has_prefix
                        cursor = database.execute(consecutive.update_has_prefix_value.format(encode(id), encode(data["has_prefix"])))

                        
            if 'has_range' in data:

                if data['has_range'] == "false":
                    #Update the has_range value
                    cursor = database.execute(consecutive.update_range.format(encode(id), encode(data['has_range'])))
                    cursor = database.execute(consecutive.update_ranges.format(encode(id), encode("null"), encode("null")))

                if data['has_range'] == "true":

                    if 'initial' not in data or 'final' not in data:
                        message = {}
                        message["message"] = "Please select the initial and the final value when the has_range is true"
                        message["status"] = 400

                        return message

                    if 'initial' in data or 'final' in data:

                        if int(actual_consecutive) > int(data['final']) and int(data['initial'] < int(data['final'])):
                            #Update the has_range value
                            cursor = database.execute(consecutive.update_range.format(encode(id), encode(data['has_range'])))
                            cursor = database.execute(consecutive.update_ranges.format(encode(id), encode(data['initial']), encode(data['final'])))

                database.commit()
                database.close()

                message = {}
                message["message"] = "The consecutive has been updated"
                message["status"] = 201

                return message


        except Exception as error:

            database = SQL()

            # Get next error value
            cursor = database.execute(errors.nextID)
            row = cursor.fetchone()

            date_time_str = '2018-06-29 08:15:27.243860'
            date_time_obj = datetime.datetime.strptime(
                date_time_str, '%Y-%m-%d %H:%M:%S.%f')

            id_encrypted = encode(str(row[0]))
            username_encrypted = encode(data["username"])
            date_encrypted = encode(str(date_time_obj))
            detail_encrypted = encode(str(error))

            # Insert the error
            cursor = database.execute(errors.insert.format(id_encrypted, username_encrypted, date_encrypted,
                                                           detail_encrypted))

            database.commit()
            database.close()

            message = {}
            message["message"] = str(error)
            message["status"] = 500

            return message

    def increase(self, id, data):

        try:
            pass
        except Exception as error:

            database = SQL()

            # Get next error value
            cursor = database.execute(errors.nextID)
            row = cursor.fetchone()

            date_time_str = '2018-06-29 08:15:27.243860'
            date_time_obj = datetime.datetime.strptime(
                date_time_str, '%Y-%m-%d %H:%M:%S.%f')

            id_encrypted = encode(str(row[0]))
            username_encrypted = encode(data["username"])
            date_encrypted = encode(str(date_time_obj))
            detail_encrypted = encode(str(error))

            # Insert the error
            cursor = database.execute(errors.insert.format(id_encrypted, username_encrypted, date_encrypted,
                                                           detail_encrypted))

            database.commit()
            database.close()

            message = {}
            message["message"] = str(error)
            message["status"] = 500

            return message`