create database jing_dong charset=utf8;

user jing_dong

create table goods(
	id int unsigned primary key auto_increment not null,
	name varchar(150) not null,
	cata_name varchar(40) not null,
	brand_name varchar(40) not null,
	price decimal(10, 3) not null default 0,
	is_show bit not null default 1,
	is_saleoff bit not null default 0
);


insert into goods values(0,'r510vc 15.6英寸笔记本','笔记本','华硕','3399',default,default); 
insert into goods values(0,'y400n 14.0英寸笔记本电脑','笔记本','联想','4999',default,default);
insert into goods values(0,'g150th 15.6英寸游戏本','游戏本','雷神','8499',default,default); 
insert into goods values(0,'x550cc 15.6英寸笔记本','笔记本','华硕','2799',default,default); 
insert into goods values(0,'x240 超极本','超级本','联想','4880',default,default); 
insert into goods values(0,'u330p 13.3英寸超极本','超级本','联想','4299',default,default); 
insert into goods values(0,'svp13226scb 触控超极本','超级本','索尼','7999',default,default); 
insert into goods values(0,'ipad mini 7.9英寸平板电脑','平板电脑','苹果','1998',default,default);
insert into goods values(0,'ipad air 9.7英寸平板电脑','平板电脑','苹果','3388',default,default); 
insert into goods values(0,'ipad mini 配备 retina 显示屏','平板电脑','苹果','2788',default,default); 

--------主键可以为0，但是非逐渐需要default

select cata_name, group_concat(name) from goods group by cata_name;

select round(avg(price), 2) from goods;

select cata_name, max(price), min(price), avg(price) from goods group by cata_name;

select * from goods where price>(select avg(price) from goods);

select cata_name, max(price) from goods group by cata_name;

select * from (
	select cata_name, max(price) as max_price from goods group by cata_name
) as g_new left join goods as g on g_new.cata_name=g.cata_name and g_new.max_price=g.price order by g_new.cata_name;

create table if not exists goods_catas(id int unsigned primary key auto_increment, name varchar(40) not null);

insert into goods_catas (name) select cata_name from goods group by cata_name;

update goods as g inner join goods as c on g.cata_name=c.name set g.cata_name=c.id;

alter table goods change cata_name cata_id int unsigned not null;

alter table goods add foreign key (cate_id) references goods_catas(id);

insert into goods values(0,'黑白打印机',12, '惠普',2300,default,default);

alter table goods add foreign key (cata_id) references goods_catas(id);

create table if not exists suppliers (id int unsigned auto_increment primary key, name varchar(40) not null);

---创建表和插入表可以同时进行

----删除外键
alter table goods drop foreign key goods_ibfk_1