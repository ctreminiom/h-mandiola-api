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