# -*- coding: utf-8 -*-
# File  : main.py
# Author: Kai
from flask import Flask, request
from api import *
app = Flask(__name__)
@app.route('/', methods=["POST"])
def post_data():
    '下面的request.get_json().get......是用来获取关键字的值用的，关键字参考上面代码段的数据格式'
    if request.get_json().get('message_type') == 'group':  # 如果是群聊信息
        gid = request.get_json().get('group_id')  # 获取群号
        uid = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
        message = request.get_json().get('raw_message')
        # print(request.get_json().get('raw_message'), 'group: ',gid,'user: ',uid)
        gid=950128534
        if (gid==gid):
            dingqun(gid)
            print(message)
            if (re.search(r'吃啥',message)):
               eat_what(gid)
            search_jx3(message)
    return 'yes'
if __name__ =='__main__':
    app.run(debug=True, host='127.0.0.1', port=5701)  # 此处的 host和 port对应上面 yml文件的设置
