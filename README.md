1. 服务启动
2. 参数传递
3. 模板简单使用
4. 


```
mysql install by docker

docker run -p 3306:3306 --name tornado -e MYSQL_ROOT_PASSWORD=123456 -d mysql
```

pymysql 查询 元组转换为字典类型
```

self.db = pymysql.connect(
            host=self.host, user=self.user,
            passwd=self.password, db=self.db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
```

```mysql
CREATE TABLE `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `article_name` varchar(255) NOT NULL,
  `article_content` varchar(3000) DEFAULT NULL,
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1
```
##### 'latin-1' codec can't encode characters in position 67-68: ordinal not in range(256)
设置数据库的属性 为utf8
charset='utf8',

##### error ：(1366, "Incorrect string value: '\\xE5\\x86\\x85\\xE5\\xAE\\xB9' for column 'article_content' at row 1")
修改表的charset 
```mysql

mysql> show variables like 'character%' 
    -> ;
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8                       |
| character_set_connection | utf8                       |
| character_set_database   | utf8                       |
| character_set_filesystem | binary                     |
| character_set_results    | utf8                       |
| character_set_server     | latin1                     |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
8 行于数据集 (0.11 秒)

mysql> alter table article convert to character set 'utf8';
Query OK, 32 rows affected (0.19 秒)

mysql> 
```