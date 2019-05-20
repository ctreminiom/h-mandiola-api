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



class insertProcedures:
    consecutive_type = "exec addConsecutiveType @ID = '{}', @Name = '{}';"
    consecutive = """
    exec addConsecutive @ID = '{}', @ConsecutiveType = '{}', @Description = '{}', @HasPrefix = '{}',
    @Prefix = '{}', @HasRange = '{}', @Initial = '{}', @Final = '{}', @Consecutive = '{}';
    """





class sequences:
    consecutive_type = "exec getNextValueConsecutivesypes2;"
    consecutive = "exec getNextValueConsecutives;"



class selectViews:
    consecutive_type = "select * from dev2.getConsecutiveTypes;"