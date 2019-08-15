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
    @ID varchar(800),
    @Name varchar(5000)
as
insert into dbo.roles
    (ID, name)
values
    (@ID, @Name);
GO;

----------------------------------------------------------------
----------------------------------------------------------------

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

----------------------------------------------------------------
----------------------------------------------------------------


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

----------------------------------------------------------------
----------------------------------------------------------------


create sequence dbo.users_sequence start with 1 increment by 1;
GO;

create procedure dbo.get_users_sequence
as
select next value for dbo.users_sequence;
GO;
create view dbo.get_users
as
    select ID, username, email, question
    from dbo.users;
GO;
create procedure dbo.get_user
    @Username varchar(8000)
as
select ID, username, [password], email, question
from dbo.users
where username = @Username;
GO;

create procedure dbo.insert_user
    @ID varchar(900),
    @Username varchar(900),
    @Email varchar(8000),
    @Password varchar(8000),
    @Question varchar(8000),
    @Answer varchar(8000)
as
insert into dbo.users
    (ID, username, email, password, question, answer)
values
    (@ID, @Username, @Email, @Password, @Question, @Answer);
GO;

create procedure dbo.update_password
    @Username varchar(900),
    @Password varchar(900)
as
UPDATE dbo.users SET password= @Password WHERE username= @Username;
GO;

create procedure dbo.delete_user
    @Username varchar(900)
as
DELETE FROM dbo.users WHERE username = @Username;
GO;


----------------------------------------------------------------
----------------------------------------------------------------

create sequence dbo.consecutives_types_sequence start with 1 increment by 1;
GO;

create procedure dbo.get_consecutives_types_sequence
as
select next value for dbo.consecutives_types_sequence;
GO;

create view dbo.get_consecutives_types
as
    select *
    from dbo.consecutive_types;
GO;

create procedure dbo.insert_consecutive_type
    @ID varchar(900),
    @Name varchar(8000)
as
insert into dbo.consecutive_types
    (ID, name)
values
    (@ID, @Name);
GO;

----------------------------------------------------------------
----------------------------------------------------------------

create sequence dbo.consecutives_sequence start with 1 increment by 1;
GO;

create procedure dbo.get_consecutives_sequence
as
select next value for dbo.consecutives_sequence;
GO;

create view dbo.get_consecutives
as
    select dbo.consecutives.ID, dbo.consecutive_types.name, dbo.consecutives.description, dbo.consecutives.has_prefix, dbo.consecutives.prefix, dbo.consecutives.has_range, dbo.consecutives.initial, dbo.consecutives.[final]
    from dbo.consecutives
        inner join dbo.consecutive_types on dbo.consecutives.[type] = dbo.consecutive_types.ID;
GO;

create procedure dbo.insert_consecutive
    @ID varchar(900),
    @Type varchar(900),
    @Description varchar(8000),
    @HasPrefix	varchar(8000),
    @Prefix varchar(8000),
    @HasRange varchar(8000),
    @Initial varchar(8000),
    @Final varchar(8000)
as
insert into dbo.consecutives
    (ID, [type], description, has_prefix, prefix, has_range, initial, [final])
values
    (@ID, @Type, @Description , @HasPrefix, @Prefix, @HasRange, @Initial, @Final);
GO;


----------------------------------------------------------------
----------------------------------------------------------------
create sequence dbo.clients_sequence start with 1 increment by 1;
GO;

create procedure dbo.get_clients_sequence
as
select next value for dbo.clients_sequence;
GO;

create view dbo.get_clients
as
    select dbo.clients.ID, dbo.consecutive_types.name as "consecutive", dbo.clients.fist_name, dbo.clients.last_name, dbo.clients.username, dbo.clients.email, dbo.clients.sub, dbo.clients.aud
       from dbo.clients
       inner join dbo.consecutives on dbo.clients.consecutive = dbo.consecutives.ID
       inner join dbo.consecutive_types on dbo.consecutives.[type] = dbo.consecutive_types.ID;
GO;

create procedure dbo.insert_client
    @ID varchar(900),
    @Consecutive varchar(900),
    @First varchar(8000),
    @Last	varchar(8000),
    @Username varchar(8000),
    @Email varchar(8000),
    @Sub varchar(8000),
    @Aud varchar(8000)
as
insert into dbo.clients
    (ID, consecutive, fist_name, last_name, username, email, sub, aud)
values
    (@ID, @Consecutive, @First , @Last, @Username, @Email, @Sub, @Aud);
GO;


create procedure dbo.get_client
    @Sub varchar(8000)
as
select ID, email, sub, aud
from dbo.clients
where aud = @Sub;
GO;

----------------------------------------------------------------
----------------------------------------------------------------


create sequence dbo.activities_sequence start with 1 increment by 1;
GO;
create procedure dbo.get_activities_sequence
as
select next value for dbo.activities_sequence;
GO;

create view dbo.get_activities
as
select dbo.activity.ID, dbo.consecutive_types.name as "consecutive", dbo.activity.name, dbo.activity.description, dbo.activity.[image]
from dbo.activity
inner join dbo.consecutives on dbo.activity.consecutive = dbo.consecutives.ID
inner join dbo.consecutive_types on dbo.consecutives.[type] = dbo.consecutive_types.ID;
GO;

create procedure dbo.insert_activity
    @ID varchar(900),
    @Consecutive varchar(900),
    @Name varchar(8000),
    @Description varchar(8000),
    @Image varchar(8000)
as
insert into dbo.activity
    (ID, consecutive, name, description, [image])
values
    (@ID, @Consecutive,@Name, @Description, @Image);

create procedure dbo.delete_activity
    @ID varchar(900)
as
delete from dbo.activity where ID=@ID;
GO;


----------------------------------------------------------------
----------------------------------------------------------------

create sequence dbo.product_type_sequence start with 1 increment by 1;
GO;
create procedure dbo.get_product_type_sequence
as
select next value for dbo.product_type_sequence;
GO;

create view dbo.get_product_types
as
    select * from dbo.product_types;
GO;

create procedure dbo.insert_product_type
    @ID varchar(900),
    @Name varchar(8000)
as
insert into dbo.product_types
    (ID, name)
values
    (@ID, @Name);
GO;


----------------------------------------------------------------
----------------------------------------------------------------

create sequence dbo.product_sequence start with 1 increment by 1;
GO;
create procedure dbo.get_product_sequence
as
select next value for dbo.product_sequence;
GO;

create view dbo.get_products
as
select dbo.products.ID, dbo.consecutive_types.name as "consecutives", dbo.product_types.name as "type", dbo.products.name
from dbo.products
inner join dbo.product_types on dbo.products.[type] = dbo.product_types.ID
inner join dbo.consecutives on dbo.products.consecutive = dbo.consecutives.ID
inner join dbo.consecutive_types on dbo.consecutives.[type] = dbo.consecutive_types.ID;
GO;


create procedure dbo.insert_product
    @ID varchar(900),
    @Consecutive varchar(900),
    @Type varchar(900),
    @Name varchar(900)
as
INSERT INTO dbo.products
    (ID, consecutive, [type], name)
VALUES(@ID, @Consecutive, @Type, @Name);
GO;


create procedure dbo.delete_product
    @ID varchar(900)
as
delete from dbo.products where ID=@ID;
GO;


----------------------------------------------------------------
----------------------------------------------------------------

create sequence dbo.rooms_type_sequence start with 1 increment by 1;
GO;
create procedure dbo.get_rooms_type_sequence
as
select next value for dbo.rooms_type_sequence;
GO;


create view dbo.get_rooms_types
as
    select *
    from dbo.room_types;
GO;

create procedure dbo.insert_room_type
    @ID varchar(900),
    @Name varchar(8000)
as
insert into dbo.room_types
    (ID, name)
values
    (@ID, @Name);
GO;


----------------------------------------------------------------
----------------------------------------------------------------


create sequence dbo.rooms_sequence start with 1 increment by 1;
GO;
create procedure dbo.get_rooms_sequence
as
select next value for dbo.rooms_sequence;
GO;


create view dbo.get_rooms
as
    select dbo.rooms.ID, dbo.consecutive_types.name as "consecutive", dbo.room_types.name as "type", dbo.rooms.[number], dbo.rooms.description, dbo.rooms.available, dbo.rooms.[image]
from dbo.rooms
inner join dbo.room_types on dbo.rooms.[type] = dbo.room_types.ID
inner join dbo.consecutives on dbo.rooms.consecutive = dbo.consecutives.ID
inner join dbo.consecutive_types on dbo.consecutives.[type] = dbo.consecutive_types.ID;
GO;


create procedure dbo.insert_room
    @ID varchar(900),
    @Consecutive varchar(900),
    @RoomType varchar(900),
    @Number varchar(8000),
    @Description varchar(8000),
    @Available varchar(8000),
    @Image varchar(8000)
as
INSERT INTO dbo.rooms
    (ID, consecutive, [type], [number], description, available, [image])
VALUES(@ID, @Consecutive, @RoomType, @Number, @Description, @Available, @Image);
GO;

create procedure dbo.delete_room
    @ID varchar(900)
as
delete from dbo.rooms where ID=@ID;