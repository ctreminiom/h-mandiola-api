create procedure addConsecutiveType
    @ID varchar(50),
    @Name varchar(4000)
AS
insert into dev.consecutives_types(ID, name) values (@ID, @Name);


create sequence dev.consecutives_types_sequence
start with 1
increment by 1;

create procedure getNextValueConsecutivesypes
AS
select next value for dev.consecutives_types_sequence;



exec addConsecutiveType @ID = 2, @Name = 'Carlos';
exec getNextValueConsecutiveTypes;
