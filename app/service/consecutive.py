#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.service.database import SQL
from app.middleware.encrypt import encode
from config import sequences, insertProcedures



class Type:

    def create(self, name):

        handler = SQL()

        try:
            cursor = handler.execute(sequences.consecutive_type)
        except:
            print("ERROR")

        cursor = handler.execute(sequences.consecutive_type)

        row = cursor.fetchone()

        id_encrypted = encode(str(row[0]))
        name_encypted = encode(name)

        print(insertProcedures.consecutive_type.format(id_encrypted, name_encypted))

        try:
            cursor = handler.execute(insertProcedures.consecutive_type.format(id_encrypted, name_encypted))
        except:
            print("ERROR")

        handler.commit()
        handler.close()






