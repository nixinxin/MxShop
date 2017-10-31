#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "xin nix"
# from django.http import HttpResponse
from django.views.generic.base import View
# from django.views.generic import ListView
from goods.models import Goods
import json
from django.http import JsonResponse


class GoodsListView(View):

    def get(self, request):
        """
        通过django的view实现商品列表页
        :param request:
        :return:
        """
        goods = Goods.objects.all()
        # json_list = []
        # for good in goods:
        #     json_dict = {'name': good.name, 'category': good.category.name, 'market_price': good.market_price}
        #     json_list.append(json_dict)
        # return HttpResponse(json.dumps(json_list), content_type='application/json')

        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)
        # return HttpResponse(json.dumps(json_list), content_type='application/json')

        from django.core import serializers
        json_list = serializers.serialize("json", goods)
        # return HttpResponse(json_list, content_type='application/json')

        json_list = json.loads(json_list)
        # 不加safe参数无法序列化非字典对象
        return JsonResponse(json_list, safe=False)
