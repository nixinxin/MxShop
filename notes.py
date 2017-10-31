#!/usr/bin/python
# -*- coding:utf-8 -*-

from settings import return_url, app_notify_url, private_key_path, ali_pub_key_path, ALIPAY_ID

__author__ = "xin nix"


"""
    笔记：pip install djangorestframework  markdown, django-filter 需要自己安装django
    mysql：pymysql,option{"init_command": "storage_engine=INNODB }
    安装出错解决方法： www.ifd.uci.edu/~gohlke/pythonlibs
    跨域访问问题: django-cors-headers
    博客源地址：projectsedu.com
    前后端分离之JWT用户认证：lion1ou,win       
    jwt :django-rest-framework-jwt
    github库： mxshop_sources
    服务器链接工具：winscp 类似于xshell`
    pip install raven --upgrade
    pip install social-auth-app-django
     yum install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel

"""

from utils.alipay import AliPay

alipays = AliPay(
    appid=ALIPAY_ID,
    app_notify_url=app_notify_url,
    app_private_key_path=private_key_path,
    alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
    debug=True,  # 默认False,
    return_url=return_url
)

url = alipays.direct_pay(
        subject="测试订单",
        out_trade_no="20170201dsf12",
        total_amount=100,
        return_url=return_url
)
re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)

print(re_url)
