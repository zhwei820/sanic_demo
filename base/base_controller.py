#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/7/20 13:54
# @Author  : otfsenter
# @File    : base_controller.py

import traceback
from base.exception import BusinessError
from util.http_util import return_ok, return_failed


class ServiceContoller():
    __name__ = ""

    def __init__(self, schema_cls, service_cls):
        '''
        路由控制
        比如：/*/create
            会解析到service_cls的create方法进行处理
        :param schema_cls:
                校验请求数据格式的json schema 类,请求上例子create方法，请求数据会由shema_cls的CREATE方法进行校验
        :param service_cls:
                处理请求的service类,用户实例成处理业务逻辑的service对象,由service对象实际完成业务逻辑处理
        '''
        self.schema_cls = schema_cls
        self.service_cls = service_cls

    async def __call__(self, request, method):
        '''
        实例化service_cls,并路由到service对象不对的方法对处理业务
        :param request: django默认的请求request对象
        :return:
        '''
        try:
            if hasattr(self.service_cls, 'service_from_request'):
                service = getattr(self.service_cls, 'service_from_request')(request)
            else:
                raise BusinessError('0287', "服务没有实现service_from_request方法")
            data = getattr(self.service_cls, 'param_from_request')(request, method, self.schema_cls)
            if isinstance(data, list):
                # 列表直接传
                ret = await getattr(service, method.lower())(data)
                return return_ok(ret)
            else:
                # 字典解析出来传
                ret = await getattr(service, method.lower())(**data)
                return return_ok(ret)
        except BusinessError as e:
            return return_failed(e.errcode, e.msg)
        except Exception as e:
            # if settings.CONFIG['DEBUG']:
            traceback.print_exc()
            return return_failed(-1, "未知错误")
