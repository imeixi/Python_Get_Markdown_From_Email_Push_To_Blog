#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import base64
import json
import sys
import os
from hashlib import sha1


# 文件base64 加密
def file_base64(filename):
    with open(filename, 'rb') as f:
        fn_b64 = base64.b64encode(f.read()).decode('utf-8')
    return fn_b64


def get_blob_sha(s):
    # s是个字符串，也就是文件里的内容。
    sha1_obj = sha1()
    content = s.encode('ascii')	# 以二进制编码
    content = b'blob %d\0' % len(content) + content
    sha1_obj.update(content)
    return sha1_obj.hexdigest()


def push_file(url, tokens, fn):
    # 准备put的json数据，其中content是经过base64位编码后的 文件字节流
    data = {
        "message": "my commit message",
        "committer": {
            "name": "email_imeixi",
            "email": "zheng.ah.r@gmail.com"
        },
        "content": file_base64(fn),
        "sha": get_blob_sha(file_base64(fn))
    }
    # token 授权
    headers = {"Authorization": 'token ' + tokens}
    # put方法将文件推送到服务端
    res = requests.put(url, data=json.dumps(data), headers=headers)
    if res.status_code == 201:
        print('success')
        print('response code: ' + str(res.status_code))
        print('response message: ' + str(res.text))
    else:
        print('response code: ' + str(res.status_code))
        print('response message: ' + str(res.text))
