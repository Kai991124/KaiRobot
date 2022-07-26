# -*- coding: utf-8 -*-
# File  : api.py
# Author: Kai
# Date  : 2022/3/27
import requests
import re
import pandas as pd
import random


def search_jx3(command, gid):
    # command search
    # 开服
    if (re.search(r'开服', command)):
        if (requests.get('https://www.jx3api.com/app/check?server=唯我独尊').json()['data']['status'] == 1):
            send_msg('唯满侠开服了！快上线练手法！！！！！')
        else:
            send_msg('查什么查，还没开服呢！', gid)
    # 金价
    if (re.search(r'金价', command)):
        jj = requests.get('https://www.jx3api.com/app/demon?server=唯我独尊').json()
        reply = '万宝楼：' + str(jj['data'][0]['wanbaolou']) + '\n' + '贴吧：' + str(jj['data'][0]['tieba'])
        send_msg(reply, gid)
    # 家具
    map_search = re.search(r'宠物游历 ([\u4e00-\u9fa5]+)', command)
    if (map_search):
        map = map_search.group(1)
        map_requests = requests.get('https://www.jx3api.com/app/travel?name=' + map).json()
        if (map_requests['msg'] == 'success'):
            data = map_requests['data']
            for i in range(len(data)):
                send_msg('家具名：{0}\n家具属性：\n-观赏分：{1}，实用分：{2}，坚固分：{3}，风水分：{4}，趣味分：{5}'.format(data[i]['name'],
                                                                                           data[i]['view_score'],
                                                                                           data[i]['practical_score'],
                                                                                           data[i]['hard_score'],
                                                                                           data[i]['geomantic_score'],
                                                                                           data[i][
                                                                                               'interesting_score']),
                         gid)
        else:
            send_msg('你看看你输入的啥，我可不认识这个地图！', gid)
    # 小药
    medicine_search = re.search(r'小药 ([\u4e00-\u9fa5]+)', command)
    if (medicine_search):
        medicine = medicine_search.group(1)
        medicine_requests = requests.get('https://www.jx3api.com/app/heighten?name=' + medicine).json()
        if (medicine_requests['msg'] == 'success'):
            data = medicine_requests['data']
            send_msg('推荐小药-{0}，{1}，{2}，{3}'.format(data['heighten_food'], data['auxiliary_food'], data['heighten_drug'],
                                                   data['auxiliary_drug'], gid))
        else:
            send_msg('你看看你输入的啥，我可不认识这个门派！')
    # 日常
    daily_search = re.search(r'日常', command)
    if (daily_search):
        daily_requests = requests.get('https://www.jx3api.com/app/daily?server=唯我独尊').json()
        if (daily_requests['msg'] == 'success'):
            data = daily_requests['data']
            send_msg('日期：{0}\n周{1}\n大战：{2}\n战场：{3}\n矿车：{4}\n美人图：{5}\n'.format(data['date'], data['week'],
                                                                              data['war'], data['battle'],
                                                                              data['camp'],
                                                                              data['draw']), gid)


def send_msg(message, gid):
    requests.get(url='http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'.format(gid, message))


def eat_what(gid):
    eat_file_path = '不知道吃什么就打开.xlsx'
    df = pd.read_excel(eat_file_path)
    food_list = df['都是档口啊'].to_list()
    res = random.sample(range(0, len(food_list)), 3)
    reply = '吃点什么呢？考虑一下这几个？\n'
    for i in range(3):
        reply = reply + '-' * 4 + food_list[res[i]] + '\n'
    send_msg(reply, gid)


def dingqun(gid):
    sort = random.randint(1, 100)
    if (sort >= 0 and sort <= 60):
        send_msg(requests.get('https://www.jx3api.com/app/random').json()['data']['text'], gid)
