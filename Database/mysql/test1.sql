create table students(
	id int unsigned not null auto_increment primary key,
	name varchar(30),
	age tinyint unsigned,
	height decimal(5,2),
	gender enum('male', 'female', 'secret') default 'secret',
	cls_id int unsigned
);

insert into students values(0, 'wang', 18, 180.00, 'secret', 0)



create table classes(
	id int unsigned not null auto_increment primary key,
	name varchar(30) not null
);

alter table students add birthday datetime;

alter table students modify birthday date;

alter table students change birthday birth date;

alter table students drop height;

--少做减法，多做加法

drop table --name---
drop database ---name---

show create table students

insert into students values(1, 'li', 18, 2, 0, '1990-11-11')
insert into students (name, gender) values ('qiao', 2)
insert into students (name, gender) values ('haha', 2), ('wowo', 2)


update students set gender=2 where id=1;

select * from students where name='li';

select name as 姓名 from students;

delete from students;   -----删除所有数据

alter table students add is_delete bit default 0;	