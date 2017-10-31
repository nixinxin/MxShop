#!/usr/bin/python
# -*- coding:utf-8 -*-
from utils.alipay import *

__author__ = "xin nix"
import requests
from MxShop.settings import *

alipay = AliPay(
    appid=APP_ID,
    app_notify_url=APP_NOTIFY_URL,
    app_private_key_path=ALIPAY_PRIVATE_KEY_PATH,
    alipay_public_key_path=ALIPAY_PUBLIC_KEY_PATH,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
    debug=True,  # 默认False,
    return_url=RETURN_URL
)

url = alipay.direct_pay(
        subject="测试订单2",
        out_trade_no="20170202111",
        total_amount=100,
        # return_url=RETURN_URL
    )
# for key, value in query.items():
#     processed_query[key] = value[0]
# print(alipay.verify(processed_query, ali_sign))

re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)

print(re_url)
