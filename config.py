#!/usr/bin/env python
# -*- coding: utf-8 -*-

class config:

    db_host = "34.73.78.37"
    db_user = "SA"
    db_passw = "Ulacit123456789"
    db_name = "test"

    encypt_key_1 = "atgwYVYMZrNSyDZvWRP6xnMqdkjEPc5LFFma4NDzpHtEgzDUB"
    encypt_key_2 = "mVJCrpg6bZQXPKLcFN9MTfyXZ8NbCYJqWETCyuRJAjnjJfNu3eLypZxDTFmfLZZWf9"
    jwt_key = "LWwP5EGuSU38VN9JgmHcvpPUtsxm9sXXqeQUJWRANzCHHLHr62Nk83NWSwuPedpk6HZKsYuVmZAHRCjmLE3MQrmcJz9j7EWWYFsy2GfKmNnqhrSgnSq"

    api_port = 5000


class procedures:
    insert_consecutive_type = "exec dba.insert_consecutive_type @ID = '{}', @Name = '{}';"

    insert_consecutive = """

    exec dba.insert_consecutive @ID = '{}', @Type = '{}', @Description = '{}', @HasPrefix = '{}',
    @Prefix = '{}', @HasRange = '{}', @Initial = '{}', @Final = '{}', @Consecutive = '{}';

    """


class sequences:
    consecutive_type = "exec dba.get_consecutives_types_sequence;"
    consecutive = "exec dba.get_consecutives_sequence;"


class views:
    gets_consecutives_types = "select * from dba.get_consecutives_types;"
    gets_consecutives = "select * from dba.get_consecutives;"


class insertProcedures:
    consecutive_type = "exec addConsecutiveType @ID = '{}', @Name = '{}';"
    consecutive = """
    exec addConsecutive @ID = '{}', @ConsecutiveType = '{}', @Description = '{}', @HasPrefix = '{}',
    @Prefix = '{}', @HasRange = '{}', @Initial = '{}', @Final = '{}', @Consecutive = '{}';
    """




