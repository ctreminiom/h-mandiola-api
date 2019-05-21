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