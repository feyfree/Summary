create database python_test charset=utf8;

use python_test

select s.name, s.age from students as s;

select * from students;

select distinct gender from students;

--条件查询
select * from students where age=18;

select * from students where age>18 and age < 20;

select * from students where age>18 and gender='female';

select * from students where height>=180;

--模糊查询
select name from students where name like 't%';

select name from students where name like '%t%';

select name from students where name like '__';

select name from students where name like '__%';

select name from students where name rlike '^z.*$';

select name from students where name rlike '^z.*z$';

select name, age from students where age not in (18,19);

select name, age from students where age between 18 and 20;

select name, age from students where not age between 18 and 20;

select * from students where height is not null;

select * from students order by age desc;

select * from students where age between 18 and 20 and gender="male" order by age desc, id desc;