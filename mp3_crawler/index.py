# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/21 上午11:13
"""

import requests
import os
from pyquery import PyQuery as pq

from multiprocessing.pool import ThreadPool

url = 'http://m.tingge123.com/qqmusic/?key={}'


def get_request(url: str):
    reson = requests.get(url=url)
    return reson.content.decode(encoding='utf-8')


def crawler_resolving_index_page(want_name='春天里', author_name=''):
    song_url = url.format(want_name)
    content = get_request(url=song_url)
    qq = pq(content)

    table = qq('table')

    orig_songs, want_song = {}, {}

    for i, k in enumerate(table.items()):
        if i == 1:
            a = k('a')
            for j in a.items():
                orig_songs[j.text()] = j.attr('href')
                pass
            pass
        pass

    song_names = orig_songs.keys()
    want_name = want_name + '.mp3'
    for name in song_names:
        if name.find(want_name) >= 0 and name.find(author_name) >= 0:
            want_song[name] = orig_songs.get(name)

    return want_song


base_path = os.path.dirname(__file__)


def get_down_url_download(file_name, down_index_page_url='http://m.tingge123.com/qqmusic/p22459.html'):
    response = requests.get(down_index_page_url)

    content = response.content.decode(encoding='utf-8')
    qq = pq(content)
    cc = qq('#show').attr('value')
    res = requests.get(cc)

    target_path = os.path.join(base_path, 'resource')

    with open(os.path.join(target_path, file_name), 'wb') as file:
        file.write(res.content)


def down_load(i):
    print("*" * 20 + i)
    if not i:
        return
    song_info = crawler_resolving_index_page(i)
    for i in song_info:
        print('开始下载歌曲：{}'.format(i))
        get_down_url_download(i, song_info.get(i))
        print('歌曲：{} 下载完毕'.format(i))


pool = ThreadPool(9)


def loop_want_songs_and_down_load():
    target_file_path = os.path.join(base_path, 'want_song/songs.txt')

    print(target_file_path)

    with open(target_file_path, 'r') as file:
        line = file.read()
        ll = line.split('\n')
        pool.map(down_load, ll)


if __name__ == "__main__":
    loop_want_songs_and_down_load()
    print('-------')
