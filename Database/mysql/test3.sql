select count(*) as 男性人数 from students where gender="male";

select max(age) from students;

select round(avg(age), 2) from students;

select gender from students group by gender;

select gender, count(*) from students group by gender;

select gender, group_concat(name) from students group by gender;

select gender, count(*) from students where gender=1 group by gender;

select gender, group_concat(name, '_', age, id) from students where gender=1 group by gender;

select gender, group_concat(name) from students group by gender having avg(age) > 18;

select gender, group_concat(name) from students group by gender having count(*) > 2;