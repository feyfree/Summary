------创建视图
create view v_goods_info as select g.*, c.name as cata_name, s.name as supplier_name from goods as g 
left join goods_catas as c on g.cata_id=c.id left join suppliers as s on g.supplier_id=s.id;
------视图 提高了重用性， 对数据库重构，不会创建空间存储数据， 提高了安全性，可以对不同用户，让数据更加清晰；

-- 创建索引
create index title_index on test_index(title(10));

set profilling=1
show profiles;

--grant 权限列表 on 数据库 to '用户名'@'访问主机' identified by '密码';
create user 'laowang'@'localhost' identified by '密码'；
grant select jing_dong.* to 'laowang'@'localhost';

grant all privileges on jing_dong.*.................;  

---刷新权限
FLUSH PRIVILEGES; 
select * from user;
----回收权限
REVOKE select 
ON . 
FROM ‘u1’@’localhost’;

update user set authentication_string=password('12345') where user='laowang';