create view dev2.getConsecutiveTypes
AS
select * from dev2.consecutives_types;






create view dev2.getConsecutives
AS
select dev2.consecutives.ID, dev2.consecutives.type, dev2.consecutives_types.name
from dev2.consecutives
inner join dev2.consecutives_types on dev2.consecutives.type = dev2.consecutives_types.ID;





