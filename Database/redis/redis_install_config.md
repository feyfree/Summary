### 1. Redis特点

Redis 与其他key-value缓存产品有一下特点

redis支持数据的持久化，可以将内存的数据保存在此盘里面

redis不仅仅支持简单的额key-value类型的数据， 同时还提供list，set， zset， hash等数据结构的存储

redis支持数据的备份，即master-slave的数据备份

### 2. 优势

1. 读写速度极高

2. 数据类型丰富

3. 所有操作都是原子性

4. 支持publish/subscribe

### 3. 应用场景

1. 用来做缓存

2. 某些特定应用场景下替代传统数据库

3. session共享， 购物车

### 4. 安装

1. 下载，解压

2. sudo mv ./redis.....  /usr/local/redis

3. cd /usr/local/redis

4. sudo make

5. sudo make test

6. sudo make install

7. cd /usr/local/bin

8. cp redis.conf      /etc/redis.conf 

   | redis-server | redis服务器     |
   | ------------:| ------------ |
   | redis-cli    | redis 命令行客户端 |

### 5. 配置

```bash
vim /etc/redis.conf

bind 127.0.0.1

port 6379

daemonize yes

dir /var/lib/redis

logfile /var/log/redis/redis-server.log
```


