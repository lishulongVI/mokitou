# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/29 上午11:52
"""
from mokitou.dao.mysql.mysql_template import MysqlTemplate


class ORM():
    def data_received(self, chunk):
        pass

    # @property
    def save_obj(self):
        table_name = self.__class__.__name__.lower()
        bean = self.__dict__
        keys = ''
        values = ''
        for i in bean:
            keys += '{},'.format(i)
            values += '"{}",'.format(str(bean[i])) if isinstance(bean[i], str) else "{},".format(bean[i])

        sql = 'insert into {} ({}) value ({})'.format(table_name, keys[:-1], values[:-1])

        print(sql)

        # db = MysqlTemplate(**mysql_master)
        # print(id(db))
        # db = MysqlTemplate(**mysql_master)
        # print(id(db))

        # print(id(MysqlTemplate.db()))
        # print(id(MysqlTemplate.db()))
        # print(id(MysqlTemplate.db()))
        re = MysqlTemplate.db().upsert_record(sql=sql)
        return re

    @classmethod
    def find_all(cls):
        table_name = cls.__name__.lower()
        sql = 'select * from {}'.format(table_name)
        re = MysqlTemplate.db().get_all(sql=sql)
        return re
