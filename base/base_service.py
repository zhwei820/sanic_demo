#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/7/20 13:12
# @Author  : otfsenter
# @File    : base_service.py

from base.exception import BusinessError
from util.http_util import request_json_schema

import logging
_logger = logging.getLogger(__name__)

class BaseService():
    '''
    基础服务，实现服务需要集成这个类
    '''

    def __init__(self, barid, **kwargs):
        self.barid = barid

    @classmethod
    def service_from_request(cls, request):
        '''
        通过reqeust实例化服务（BaseService），这个功能时候在客户端发送请求的时候，通过request对象直接实例化服务对象
        :param request:
        :return:
        '''
        # return cls(barid=request.session['barid'])
        return cls(barid=0)


    @classmethod
    def service_from_service(cls, ohter_service):
        '''
        通过 其他服务 实例化服务（BaseService）ohter_service 里面的初始化参数必须包含 待新建的服务的所有参数
        :param ohter_service:
        :return:
        '''
        return cls(**ohter_service.__dict__)



    @classmethod
    def param_from_request(cls, request, method, schema_cls):

        data = {k: request.args[k] for k in request.args}  # 默认取url参数
        if "_" in data:
            del data['_']
        if request.method == "GET":
            pass
        elif request.method == "POST":
            if not data and schema_cls and request.content_type == "application/json":
                try:
                    schema = getattr(schema_cls, method.upper())
                    data = request_json_schema(request, schema)
                except Exception as e:
                    _logger.exception("请求出错")
                    raise BusinessError("0204", "请求出错")
            elif request.files:
                data = {"files": request.files}
        else:
            # 其余方法暂时没有实现
            raise BusinessError("8341", "方法不正确")
        return data
