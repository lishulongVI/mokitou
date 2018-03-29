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