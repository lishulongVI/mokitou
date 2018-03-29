# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/28 下午2:12
"""
import pymysql


class MysqlTemplate(object):
    """
    数据库模板
    """

    def __init__(self, **kwargs):
        """
        初始化变量
        :param kwargs:
        """
        self.host = kwargs.get('host')
        self.user = kwargs.get('user')
        self.password = kwargs.get('password')
        self.db_name = kwargs.get('db_name')
        self.db = None
        self.cursor = None

    def connect(self):
        """
        数据库连接
        :return:
        """
        self.db = pymysql.connect(
            host=self.host, user=self.user,
            passwd=self.password, db=self.db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.db.cursor()

    def close(self):
        """
        关闭链接
        :return:
        """
        if self.cursor is not None:
            self.cursor.close()
        if self.db is not None:
            self.db.close()

    def get_one(self, sql):
        """
        查询单条记录
        :param sql:
        :return:
        """
        res = None

        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print(e)

        return res

    def get_all(self, sql):
        """
        查询多条记录
        :param sql:
        :return:
        """
        res = None

        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print(e)

        return res

    def find_list(self, sql, table_name, *args):
        """
        查询格式化的数据
        :param sql:
        :param table_name:
        :param args:
        :return:
        """

        pass

    def upsert_record(self, sql):
        """
        增 删 改
        :param sql:
        :return:
        """
        count = 0

        try:
            self.connect()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except Exception as e:
            print(e)
            self.db.rollback()

        return count
