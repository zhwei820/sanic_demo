#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/7/20 14:35
# @Author  : otfsenter
# @File    : http_util.py


import logging
import ujson
from sanic.response import text,json


OK_CODE = 0  # 正确

# 服务端错误码 5000 开头
UNKNOWN_SERVER = 5000  # 服务端未知错误
REDIS_SERVER = 5001  # 服务端未知错误
RETURN_INVALID = 5002  # 服务端返回结果有问题
SERVER_RESPONSE_ERROR = 5003  # 服务器在响应http请求的，处理逻辑有问题

# 客户端错误码 4000 开头
METHOD_ERROR = 4000  # 客户端请求的http方法错误
INVALID_TOKEN = 4001  # 客户端传递的url非法
PARAM_ERROR = 4002  # 客户参数错误
NONE_LOGIN = 4003  # 没有登录
FILE_SIZE_TOO_LARGE = 4005  # 文件太大了

# 回调验证失败
CALLBACK_ERROR = 3000

WARNING_CODE = -1  # 给前端一个提示, 直接显示

log = logging.getLogger("json_response")


def return_failed(error_code, message):
    data = {"code": error_code, "message": message, "data": {}}
    return json(data)


def return_ok(content):
    data = {"code": OK_CODE, "message": "", "data": content}
    return json(data)



import jsonschema
import ujson


def request_json_schema(request, schema=None):
    '''
    提取出json请求类型的body内容，并进行schema校验
    :param request:django request请求
    :param schema:json schema
    :return: 返回请求的数据
    '''
    if request.content_type != "application/json":
        raise Exception("not support content_type %s" % request.content_type)

    encoding = request.encoding if request.encoding else 'utf-8'
    body = request.body.decode(encoding)
    data = ujson.loads(body)
    if schema:
        jsonschema.validate(data, schema)
    return data
