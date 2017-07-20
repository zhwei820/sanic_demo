#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time    : 2017/7/20 19:21
# @Author  : otfsenter
# @File    : product.py


from sanic import Blueprint
from base.base_controller import ServiceContoller
from service.product.product_service import ProductService
controller = ServiceContoller(None, ProductService)

pro_bp = Blueprint('pro_bp', url_prefix='/index/product')
pro_bp.add_route(controller, "/<method>", methods=['GET', 'POST'])

pro_bp_v1 = Blueprint('pro_bp', url_prefix='/v1/index/product')
pro_bp_v1.add_route(controller, "/<method>", methods=['GET', 'POST'])

