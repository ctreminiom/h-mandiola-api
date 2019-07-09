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
select ID, username, email, security_question
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
