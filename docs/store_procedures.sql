
---------------------- ROLES ---------------------------------
create sequence dbo.roles_sequence start with 1 increment by 1;
GO;

create view dbo.get_roles
as
    select *
    from dbo.roles;
GO;

create procedure dbo.get_roles_sequence
as
select next value for dbo.roles_sequence;
GO;

create procedure dbo.insert_role
    @ID varchar(900),
    @Name varchar(8000)
as
insert into dbo.roles
    (ID, name)
values
    (@ID, @Name);
GO;

create procedure dbo.get_role_by_name
    @Name varchar(8000)
as
select * from dbo.roles where name=@Name;

---------------------- ROLES ---------------------------------



---------------------- LOGS ---------------------------------
create sequence dbo.logs_sequence start with 1 increment by 1;
GO;
create view dbo.get_logs
as
    select *
    from dbo.logs;
GO;
create procedure dbo.get_logs_sequence
as
select next value for dbo.logs_sequence;
GO;
create procedure dbo.insert_log
    @ID varchar(900),
    @Username varchar(8000),
    @Code varchar(8000),
    @Date varchar(8000),
    @Detail varchar(8000)
as
insert into dbo.logs
    (ID, username, code, [date], detail)
values
    (@ID, @Username, @Code, @Date, @Detail);
GO;
---------------------- LOGS ---------------------------------


---------------------- ERRORS ---------------------------------
create sequence dbo.errors_sequence start with 1 increment by 1;
GO;

create view dbo.get_errors
as
    select *
    from dbo.errors;
GO;
create procedure dbo.get_errors_sequence
as
select next value for dbo.errors_sequence;
GO;
create procedure dbo.insert_error
    @ID varchar(900),
    @Username varchar(8000),
    @Date varchar(8000),
    @Detail varchar(8000)
as
insert into dbo.errors
    (ID, username, [date], detail)
values
    (@ID, @Username, @Date, @Detail);
GO;
---------------------- ERRORS ---------------------------------


---------------------- USERS ---------------------------------
create sequence dbo.users_sequence start with 1 increment by 1;
GO;

create procedure dbo.get_users_sequence
as
select next value for dbo.users_sequence;
GO;

create view dbo.get_users
as
    select ID, username, email, security_question
    from dbo.users;
GO;
create procedure dbo.get_user
    @Username varchar(8000)
as
select ID, username, [password], email, security_question
from dbo.users
where username = @Username;
GO;

create procedure dbo.insert_user
    @ID varchar(900),
    @Username varchar(900),
    @Email varchar(8000),
    @Password varchar(8000),
    @Security_Question varchar(8000),
    @Security_Answer varchar(8000)
as
insert into dbo.users
    (ID, username, email, password, security_question, security_answer)
values
    (@ID, @Username, @Email, @Password, @Security_Question, @Security_Answer);
GO;
create procedure dbo.update_password
    @Username varchar(900),
    @Password varchar(900)
as
UPDATE dbo.users SET password= @Password WHERE username= @Username;
GO;
create procedure dbo.check_security_password
    @Username varchar(900)
as
SELECT security_answer
FROM dbo.users
WHERE username= @Username;
GO;

create procedure dbo.delete_user
    @Username varchar(900)
as
DELETE FROM ulacit.dbo.users WHERE username = @Username;


---------------------- USERS ---------------------------------




---------------------- GRANT ---------------------------------
create sequence dbo.grants_sequence start with 1 increment by 1;
GO;

create procedure dbo.get_grants_sequence
as
select next value for dbo.grants_sequence;
GO;

create procedure dbo.get_grant
    @Username varchar(8000)
as
select dbo.grants.id, dbo.roles.name, dbo.users.username
from dbo.grants
    inner join dbo.roles on dbo.grants.role_ID = dbo.roles.ID
    inner join dbo.users on dbo.grants.user_ID = dbo.users.ID
where dbo.users.username = @Username;
GO;

create procedure dbo.remove_grant
    @User varchar(900),
    @Role varchar(900)
as
delete from dbo.grants where role_ID = @Role and user_ID = @User;
GO;

create procedure dbo.insert_grant
    @ID varchar(900),
    @User varchar(900),
    @Role varchar(900)
as
insert into dbo.grants
    (ID, user_ID, role_ID)
values
    (@ID, @User, @Role);
GO;
---------------------- GRANT ---------------------------------






---------------------- CONSECUTIVES_TYPES ---------------------------------
create sequence dbo.consecutives_types_sequence start with 1 increment by 1;
GO;

create procedure dbo.get_consecutives_types_sequence
as
select next value for dbo.consecutives_types_sequence;
GO;

create view dbo.get_consecutives_types
as
    select *
    from dbo.consecutives_types;
GO;

create procedure dbo.insert_consecutive_type
    @ID varchar(900),
    @Name varchar(8000)
as
insert into dbo.consecutives_types
    (ID, name)
values
    (@ID, @Name);
GO;
---------------------- CONSECUTIVES_TYPES ---------------------------------





---------------------- CONSECUTIVES--------------------------------
create sequence dbo.consecutives_sequence start with 1 increment by 1;
GO;

create procedure dbo.get_consecutives_sequence
as
select next value for dbo.consecutives_sequence;
GO;

create view dbo.get_consecutives
as
    select dbo.consecutives.ID, dbo.consecutives_types.name, dbo.consecutives.description, dbo.consecutives.has_prefix, dbo.consecutives.prefix, dbo.consecutives.has_range, dbo.consecutives.initial, dbo.consecutives.[final]
    from dbo.consecutives
        inner join dbo.consecutives_types on dbo.consecutives.consecutive_type_ID = dbo.consecutives_types.ID;
GO;

create procedure dbo.insert_consecutive
    @ID varchar(900),
    @ConsecutiveType varchar(900),
    @Description varchar(8000),
    @HasPrefix	varchar(8000),
    @Prefix varchar(8000),
    @HasRange varchar(8000),
    @Initial varchar(8000),
    @Final varchar(8000)
as
insert into dbo.consecutives
    (ID, consecutive_type_ID, description, has_prefix, prefix, has_range, initial, [final])
values
    (@ID, @ConsecutiveType, @Description , @HasPrefix, @Prefix, @HasRange, @Initial, @Final);
GO;

create procedure dbo.update_has_prefix
    @ID varchar(900),
    @HasPrefix varchar(8000)
as
update dbo.consecutives set has_prefix = @HasPrefix where ID = @ID;
GO;


create procedure dbo.get_consecutive
    @ID varchar(900)
as
select dbo.consecutives.ID, dbo.consecutives_types.name, dbo.consecutives.description, dbo.consecutives.has_prefix, dbo.consecutives.prefix, dbo.consecutives.has_range, dbo.consecutives.initial, dbo.consecutives.[final]
from dbo.consecutives
    inner join dbo.consecutives_types on dbo.consecutives.consecutive_type_ID = dbo.consecutives_types.ID
where dbo.consecutives.ID = @ID;



---------------------- CONSECUTIVES--------------------------------


---------------------- ACTIVITIES--------------------------------
create sequence dbo.activities_sequence start with 1 increment by 1;
GO;
create procedure dbo.get_activities_sequence
as
select next value for dbo.activities_sequence;
GO;

create view dbo.get_activities
as
    select dbo.activities.ID, dbo.consecutives_types.name as "consecutive", dbo.consecutives.prefix, dbo.activities.consecutive_num, dbo.activities.name, dbo.activities.description, dbo.activities.image_path
    from dbo.activities
        inner join dbo.consecutives on dbo.activities.consecutive_ID = dbo.consecutives.ID
        inner join dbo.consecutives_types on dbo.consecutives.consecutive_type_ID = dbo.consecutives_types.ID;
GO;


create procedure dbo.insert_activity
    @ID varchar(900),
    @Consecutive varchar(900),
    @ConsecutiveKey varchar(8000),
    @ConsecutiveNum	varchar(8000),
    @Name varchar(8000),
    @Description varchar(8000),
    @ImagePath varchar(8000)
as
insert into dbo.activities
    (ID, consecutive_ID, consecutive_key, consecutive_num, name, description, image_path)
values
    (@ID, @Consecutive, @ConsecutiveKey , @ConsecutiveNum, @Name, @Description, @ImagePath);
GO;
---------------------- ACTIVITIES--------------------------------


----------------PRODUCT TYPE----------------
create sequence dbo.product_type_sequence start with 1 increment by 1;
GO;
create procedure dbo.get_product_type_sequence
as
select next value for dbo.product_type_sequence;
GO;

create view dbo.get_product_types
as
    select *
    from dbo.products_types;
GO;

create procedure dbo.insert_product_type
    @ID varchar(900),
    @Name varchar(8000)
as
insert into dbo.products_types
    (ID, name)
values
    (@ID, @Name);
GO;




