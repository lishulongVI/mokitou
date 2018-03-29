# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/29 上午11:52
"""
from mokitou.dao.orm.orm import ORM


class Article(ORM):
    def __init__(self, name, content):
        self.article_name = name
        self.article_content = content


if __name__ == '__main__':
    a = Article('a', 'v')

    print(a.save_obj)
    ab = Article('as', 'vs')
    print(ab.save_obj)

    print(Article.find_all())


