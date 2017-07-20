#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/7/20 19:02
# @Author  : otfsenter
# @File    : product_service.py

from base.base_service import BaseService


class ProductService(BaseService):
    async def get_list(self):
        return [{'my': 'blueprint11'}]
