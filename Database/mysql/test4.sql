select * from students where gender='male' limit 2;

--- limit 限制为第几个n

select * from students where gender='male' limit 0, 5;   --第一页
select * from students where gender='male' limit 5, 5;   --第二页
select * from students where gender='male' limit 10, 5;   --第三页

select * from students where gender=1 order by height desc limit 2;


----内连接，对应的数据能相连在一起.  on 后面的条件对的上的话，就显示


select * from students inner join classes on students.cls_id = classes.id;

select students.*, classes.name from students inner join classes on students.cls_id = classes.id;

select s.*, c.name from students as s inner join classes as c on s.cls_id = c.id;

select s.name, c.name from students as s inner join classes as c on s.cls_id = c.id;

select c.name as 班级, s.name from students as s inner join classes as c on s.cls_id = c.id order by c.name, s.id;

select * from students as s left join classes as c on s.cls_id=c.id;

select * from students as s left join classes as c on s.cls_id=c.id having c.id is null;

select * from students as s left join classes as c on s.cls_id=c.id where c.id is null;


