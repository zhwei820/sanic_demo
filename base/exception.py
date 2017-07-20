#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/7/20 14:33
# @Author  : otfsenter
# @File    : exception.py


class error_info():
    def __init__(self, errcode, msg):
        self.errcode = errcode
        self.msg = msg


class BusinessError(Exception):
    def __init__(self, errcode, msg=''):
        if isinstance(errcode, error_info):
            self.errcode = errcode.errcode
            self.msg = errcode.msg
        elif isinstance(errcode, dict):
            self.errcode = errcode['code']
            self.msg = errcode['message']
        else:
            self.errcode = errcode
            self.msg = msg
        super(BusinessError, self).__init__(errcode, msg)