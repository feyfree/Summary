-----关联查询
select * from areas as province inner join areas as city where province.areano=city.parentno having province.areaname='江苏省';
----子查询
select * from students where height=188;

select * from students where height = (select max(height) from students);

select * from areas where parentno=(select areano from areas where areaname='江苏省');

select count(*) from areas where parentno=(select areano from areas where areaname='江苏省');