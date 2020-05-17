#!/usr/bin/env python
# -*- coding:utf-8 -*-

from handler_email.get_email import OperateEmail
from handler_email.push_file import push_file
import sys
import os

if __name__ == '__main__':
    # 命令行输入三个参数，第1个参数 sys.argv[0] 是脚本名称，第2个是邮箱用户名，第3个是邮箱密码, 第4个是token
    user = sys.argv[1]
    pw = sys.argv[2]
    token = sys.argv[3]

    imeixi_dir = 'email_imeixi'
    time_diary_dir = 'email_timediary'

    operate_email = OperateEmail(user, pw)
    print("Check email and save attachment.....\n")
    operate_email.rec_email_by_pop3(imeixi_dir, time_diary_dir)
    print("Check email and save attachment.....have done\n")

    print('-' * 80)

    print("Push file to imeixi.cn Github pages.....\n")
    for root, dirs, files in os.walk(imeixi_dir, topdown=True):
        for name in files:
            url_imeixi = 'https://api.github.com/repos/imeixi/blog/contents/source/_posts/' + name
            file = os.path.join(root, name)
            print(file)
            push_file(url_imeixi, tokens=token, fn=file)
        for name in dirs:
            print(os.path.join(root, name))
    print("Push files to imeixi.cn Github pages.....have done\n")

    print('-' * 80)

    print("Push files to timediary.top Github pages.....\n")
    for root, dirs, files in os.walk(time_diary_dir, topdown=False):
        for name in files:
            url_time_diary = 'https://api.github.com/repos/imeixi/timediary/contents/source/_posts/' + name
            file = os.path.join(root, name)
            print(file)
            push_file(url_time_diary, tokens=token, fn=file)
        for name in dirs:
            print(os.path.join(root, name))
    print("Push files to timediary.top Github pages.....have done\n")
    print('-' * 80)
