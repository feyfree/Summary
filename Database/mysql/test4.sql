select * from students where gender='male' limit 2;

--- limit 限制为第几个n

select * from students where gender='male' limit 0, 5;   --第一页
select * from students where gender='male' limit 5, 5;   --第二页
select * from students where gender='male' limit 10, 5;   --第三页

select * from students where gender=1 order by height desc limit 2;
----内连接，对应的数据能相连在一起
select * from students inner join classes on students.cls_id = classes.id;

select students.*, classes.name from students inner join classes on students.cls_id = classes.id;

select s.*, c.name from students as s inner join classes as c on s.cls_id = c.id;
