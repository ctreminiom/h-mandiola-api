--------------------- CONSECUTIVE TYPES --------------------------------------
create sequence dba.consecutives_types_sequence
start with 1
increment by 1;

create view dba.get_consecutives_types 
as
select * from dba.consecutives_types;

create procedure dba.get_consecutives_types_sequence
as
select next value for dba.consecutives_types_sequence;

create procedure dba.insert_consecutive_type @ID varchar(1700), @Name varchar(8000)
as
insert into dba.consecutives_types(ID, name) values (@ID, @Name);


--------------------- ERROR --------------------------------------
create sequence dba.errors_sequence
start with 1
increment by 1;

create view dba.get_errors
as
select * from dba.Errors;

create procedure dba.get_errors_sequence
as
select next value for dba.errors_sequence;

create procedure dba.insert_error @ID varchar(1700), @Username varchar(8000), @Date varchar(8000), @Detail varchar(8000)
as
insert into dba.Errors(ID, username, date, detail) values (@ID, @Username, @Date, @Detail) 



--------------------- LOGS. --------------------------------------
create sequence dba.logs_sequence
start with 1
increment by 1;

create view dba.get_logs
as
select * from dba.Logs;

create procedure dba.get_logs_sequence
as
select next value for dba.logs_sequence;

create procedure dba.insert_log @ID varchar(1700), @Username varchar(8000), @Date varchar(8000), @Code varchar(8000), @Detail varchar(8000)
as
insert into dba.Logs(ID, username, date, code, detail) values (@ID, @Username, @Date, @Code, @Detail);


----------------------------- CONSECUTIVES --------------------------------------
create sequence dba.consecutives_sequence
start with 1
increment by 1;

create view dba.get_consecutives
as
select consecutives.ID, consecutives_types.name, consecutives.description, consecutives.has_prefix, consecutives.prefix, consecutives.has_range, consecutives.initial, consecutives.final, consecutives.consecutive
from dba.consecutives
inner join dba.consecutives_types
on dba.consecutives.consecutive_type = dba.consecutives_types.id;

create procedure dba.get_consecutives_sequence
as
select next value for dba.consecutives_sequence;

create procedure dba.insert_consecutive @ID varchar(1700), @Type varchar(1700), @Description varchar(8000),
    @HasPrefix varchar(8000), @Prefix varchar(8000), @HasRange varchar(8000), @Initial varchar(8000),
    @Final varchar(8000), @Consecutive varchar(8000)
as
insert into dba.consecutives(ID, consecutive_type, description, has_prefix, prefix, has_range, initial, final, consecutive)
values (@ID, @Type, @Description, @HasPrefix, @Prefix, @HasRange, @Initial, @Final, @Consecutive);

create procedure dba.increase_consecutive @ID varchar(1700), @Consecutive varchar(8000)
as
update dba.consecutives set consecutive = @Consecutive where id = @ID;

create procedure dba.get_actual_consecutive @ID varchar(1700)
as
select has_prefix, prefix, has_range, initial, final, consecutive from dba.consecutives where ID = @ID;

create procedure dba.update_final_consecutive_value @ID varchar(1700), @Final varchar(1700)
as
update dba.consecutives set final = @Final where id = @ID;

create procedure dba.update_has_range_consecutive_value @ID varchar(1700), @hasRange varchar(1700)
as 
update dba.consecutives set has_range = @hasRange where id = @ID;

create procedure dba.update_ranges_consecutive_value @ID varchar(1700), @Initial varchar(8000), @Final varchar(8000)
as
update dba.consecutives set initial = @Initial, final = @Final where id = @ID;

create procedure dba.update_prefix_value @ID varchar(1700), @Prefix varchar(8000)
as
update dba.consecutives set prefix = @Prefix where id = @ID;

create procedure dba.update_has_prefix_value @ID varchar(1700), @HasPrefix varchar(8000)
as
update dba.consecutives set has_prefix = @HasPrefix where id = @ID;














----------------------------- CONSECUTIVES --------------------------------------
create sequence dba.consecutives_sequence
start with 1
increment by 1;
---------------------------------------------------------------
create view dba.get_consecutives
as
select consecutives.ID, consecutives_types.name, consecutives.description, consecutives.has_prefix, consecutives.prefix, consecutives.has_range, consecutives.initial, consecutives.final, consecutives.consecutive
from dba.consecutives
inner join dba.consecutives_types
on dba.consecutives.consecutive_type = dba.consecutives_types.id 
--------------------------------------------------------------
create procedure dba.get_consecutives_sequence
as
select next value for dba.consecutives_sequence;
----------------------------------------------------------------
create procedure dba.insert_consecutive @ID varchar(1700), @Type varchar(1700), @Description varchar(8000),
    @HasPrefix varchar(8000), @Prefix varchar(8000), @HasRange varchar(8000), @Initial varchar(8000),
    @Final varchar(8000), @Consecutive varchar(8000)
as
insert into dba.consecutives(ID, consecutive_type, description, has_prefix, prefix, has_range, initial, final, consecutive)
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