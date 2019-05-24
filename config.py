#!/usr/bin/env python
# -*- coding: utf-8 -*-

class config:

    db_host = "34.73.78.37"
    db_user = "SA"
    db_passw = "Ulacit123456789"
    db_name = "ulacit"

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

    increase_consecutive = "exec dba.increase_consecutive @ID = '{}', @Consecutive = '{}';"
    get_actual_consecutive = "exec dba.get_actual_consecutive @ID = '{}';"
    insert_role = "exec dba.insert_role @ID = '{}', @Name = '{}';"

    insert_user = """
    exec dba.insert_user @ID = '{}', @Username = '{}', @Email = '{}', @Password = '{}',
    @Security_Question = '{}', @Security_Answer = '{}';
    """

    change_user_password = "exec dba.change_password @Username = '{}', @NewPassword = '{}';"

    get_user_by_username = "exec dba.get_user_by_username @Username = '{}';"
    get_user_by_email = "exec dba.get_user_by_email @Email = '{}';"


    insert_grant = "exec dba.insert_grant @ID = '{}', @User = '{}', @Role = '{}';"
    remove_grant = "exec dba.remove_grant @User = '{}', @Role = '{}';"




class sequences:
    consecutive_type = "exec dba.get_consecutives_types_sequence;"
    consecutive = "exec dba.get_consecutives_sequence;"
    role = "exec dba.get_roles_sequence;"
    user = "exec dba.get_users_sequence;"
    grant = "exec dba.get_grants_sequence;"


class views:
    gets_consecutives_types = "select * from dba.get_consecutives_types;"
    gets_consecutives = "select * from dba.get_consecutives;"
    get_roles = "select * from dba.get_roles;"
    get_users = "select * from dba.users;"
    get_grants = "select * from dba.get_grants;"












