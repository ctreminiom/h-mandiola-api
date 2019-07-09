create sequence dbo.roles_sequence start with 1 increment by 1;
GO;
create view dbo.get_roles as select * from dbo.roles;
GO;
create procedure dbo.get_roles_sequence as select next value for dbo.roles_sequence;
GO;
create procedure dbo.insert_role @ID varchar(900), @Name varchar(8000) as insert into dbo.roles(ID, name) values (@ID, @Name);
GO;


create sequence dbo.logs_sequence start with 1 increment by 1;
GO;
create view dbo.get_logs as select * from dbo.logs;
GO;
create procedure dbo.get_logs_sequence as select next value for dbo.logs_sequence;
GO;
create procedure dbo.insert_log @ID varchar(900), @Username varchar(8000), @Code varchar(8000), @Date varchar(8000), @Detail varchar(8000)
as insert into dbo.logs(ID, username, code, [date], detail) values (@ID, @Username, @Code, @Date, @Detail);
GO;


create sequence dbo.errors_sequence start with 1 increment by 1;
GO;
create view dbo.get_errors as select * from dbo.errors;
GO;
create procedure dbo.get_errors_sequence as select next value for dbo.errors_sequence;
GO;
create procedure dbo.insert_error @ID varchar(900), @Username varchar(8000), @Date varchar(8000), @Detail varchar(8000)
as insert into dbo.errors(ID, username, [date], detail) values (@ID, @Username, @Date, @Detail);
GO;