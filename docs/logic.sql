-----------------------------------------------------------
create sequence dba.consecutives_types_sequence
start with 1
increment by 1;

----------------------------------------------------
create view dba.get_consecutives_types 
as
select * from dba.consecutives_types;

-----------------------------------------------------
create procedure dba.get_consecutives_types_sequence
as
select next value for dba.consecutives_types_sequence;

--------------------------------------------------------
create procedure dba.insert_consecutive_type @ID varchar(1700), @Name varchar(8000)
as
insert into dba.consecutives_types(ID, name) values (@ID, @Name);






----------------------------- CONSECUTIVES --------------------------------------
create sequence dba.consecutives_sequence
start with 1
increment by 1;

---------------------------------------------------------------
create view dba.get_consecutives
as
select consecutives.id, consecutives_types.name, consecutives.description, consecutives.has_prefix, consecutives.prefix, consecutives.has_range, consecutives.initial, consecutives.final, consecutives.consecutive
from dba.consecutives
inner join dba.consecutives_types
on dba.consecutives.type = dba.consecutives_types.id 

--------------------------------------------------------------
create procedure dba.get_consecutives_sequence
as
select next value for dba.consecutives_sequence;
----------------------------------------------------------------

create procedure dba.insert_consecutive @ID varchar(1700), @Type varchar(1700), @Description varchar(8000),
    @HasPrefix varchar(8000), @Prefix varchar(8000), @HasRange varchar(8000), @Initial varchar(8000),
    @Final varchar(8000), @Consecutive varchar(8000)
as
insert into dba.consecutives(ID, type, description, has_prefix, prefix, has_range, initial, final, consecutive)
values (@ID, @Type, @Description, @HasPrefix, @Prefix, @HasRange, @Initial, @Final, @Consecutive);

----------------------------------------------------------------
create procedure dba.increase_consecutive @ID varchar(1700), @Consecutive varchar(8000)
as
update dba.consecutives set consecutive = @Consecutive where id = @ID;

----------------------------------------------------------------

create procedure dba.get_actual_consecutive @ID varchar(1700)
as
select has_prefix, prefix, has_range, initial, final, consecutive from dba.consecutives where ID = @ID;


----------------------------------------------------------------

create procedure dba.update_final_consecutive_value @ID varchar(1700), @Final varchar(1700)
as
update dba.consecutives set final = @Final where id = @ID;


create procedure dba.update_has_range_consecutive_value @ID varchar(1700), @hasRange varchar(1700)
as 
update dba.consecutives set has_range = @hasRange where id = @ID;

------------------------

create procedure dba.update_ranges_consecutive_value @ID varchar(1700), @Initial varchar(8000), @Final varchar(8000)
as
update dba.consecutives set initial = @Initial, final = @Final where id = @ID;

    




----------------------------- Roles --------------------------------------
create sequence dba.roles_sequence
start with 1
increment by 1;
---------------------------------------------------------------
create view dba.get_roles
as
select * from dba.roles;
--------------------------------------
create procedure dba.get_roles_sequence
as
select next value for dba.roles_sequence;
----------------------------------------
create procedure dba.insert_role @ID varchar(1700), @Name varchar(8000)
as
insert into dba.roles(ID, name) values (@ID, @Name);




----------------------------- Users --------------------------------------
create sequence dba.users_sequence
start with 1
increment by 1;
---------------------------------------------------------------

create view dba.get_users
as
select * from dba.users;
--------------------------------------

create procedure dba.get_users_sequence
as
select next value for dba.users_sequence;
----------------------------------------

create procedure dba.insert_user @ID varchar(1700), @Username varchar(8000), @Email varchar(8000), @Password varchar(8000),
    @Security_Question varchar(8000), @Security_Answer varchar(8000)
as
insert into dba.users(ID, username, email, password, security_question, security_answer)
values (@ID, @Username, @Email, @Password, @Security_Question, @Security_Answer);
---------------------------------------

create procedure dba.get_user_by_username @Username varchar(8000)
as
select * from dba.users where username = @Username;

---------------------------------------
create procedure dba.change_password @Username varchar(8000), @NewPassword varchar(8000)
as
update dba.users set password = @NewPassword where username = @Username;

---------------------------------------
create procedure dba.get_user_by_email @Email varchar(8000)
as
select * from dba.users where email = @Email;




----------------------------- Grants --------------------------------------
create sequence dba.grants_sequence
start with 1
increment by 1;
---------------------------------------------------------------

create view dba.get_grants
as
select dba.grants.id, dba.roles.name, dba.users.username
from dba.grants
inner join dba.roles on grants.roleID = roles.ID
inner join dba.users on grants.userID = users.ID;
--------------------------------------

create procedure dba.get_grants_sequence
as
select next value for dba.grants_sequence;
----------------------------------------

create procedure dba.insert_grant @ID varchar(1700), @User varchar(1700), @Role varchar(1700)
as
insert into dba.grants(ID, userID, roleID)  values (@ID, @User, @Role);


create procedure dba.remove_grant @User varchar(1700), @Role varchar(1700)
as
delete from dba.grants where userID = @User and roleID = @Role;



----------------------------- Activities --------------------------------------
create sequence dba.activities_sequence
start with 1
increment by 1;
---------------------------------------------------------------

create view dba.get_activities
as
select activities.id, dba.consecutives_types.name as consecutive, activities.name, activities.description, activities.image_path
from dba.activities
inner join dba.consecutives on activities.consecutive = dba.consecutives.id
inner join dba.consecutives_types on dba.consecutives.type = dba.consecutives_types.id;
--------------------------------------

create procedure dba.get_activities_sequence
as
select next value for dba.activities_sequence;
----------------------------------------

create procedure dba.insert_activity @ID varchar(1700), @Consecutive varchar(1700), @Name varchar(8000), @Description varchar(8000), @ImagePath varchar(8000)
as
insert into dba.activities(ID, consecutive, name, description, image_path) 
values (@ID, @Consecutive, @Name, @Description, @ImagePath);
----------------------------------------

create procedure dba.remove_activity @ID varchar(1700)
as
delete from dba.activities where ID = @ID;
----------------------------------------


create procedure dba.get_activity_by_ID @ID varchar(1700)
as
select * from dba.activities where ID = @ID;
----------------------------------------

create procedure dba.update_activity_name @ID varchar(1700), @Name varchar(8000)
as
update dba.activities set name = @Name where id = @ID;
----------------------------------------

create procedure dba.update_activity_description @ID varchar(1700), @Description varchar(8000)
as
update dba.activities set description = @Description where id = @ID;

----------------------------------------
create procedure dba.update_activity_image @ID varchar(1700), @Image varchar(8000)
as
update dba.activities set image_path = @Image where id = @ID;























create view dev2.getConsecutiveTypes
AS
select * from dev2.consecutives_types;



create procedure addConsecutiveType
    @ID varchar(1700),
    @Name varchar(8000)
AS
insert into dev2.consecutives_types(ID, name) values (@ID, @Name);


create sequence dev2.consecutives_types_sequence
start with 1
increment by 1;

create procedure getNextValueConsecutivesypes
AS
select next value for dev2.consecutives_types_sequence;

/////////////////////////////////////

create procedure addConsecutive
    @ID varchar(1700),
    @ConsecutiveType varchar(1700),
    @Description varchar(8000),
    @HasPrefix varchar(8000),
    @Prefix varchar(8000),
    @HasRange varchar(8000),
    @Initial varchar(8000),
    @Final varchar(8000),
    @Consecutive varchar(8000)
    
AS
INSERT INTO [dev2].[consecutives] ([ID], [type], [description], [has_prefix], [prefix], [has_range], [initial], [final], [consecutive])
 VALUES (@ID, @ConsecutiveType, @Description, @HasPrefix, @Prefix, @HasRange, @Initial, @Final, @Consecutive);

create sequence dev2.consecutives_sequence
start with 1
increment by 1;

create procedure getNextValueConsecutives
AS
select next value for dev2.consecutives_sequence;


/////////////////////////////////////////