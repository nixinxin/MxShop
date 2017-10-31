#!/usr/bin/python
# -*- coding:utf-8 -*-
from goods.models import Goods

__author__ = "xin nix"

import django_filters
from django.db.models import Q


# 继承django_filters.FilterSet没有提交按钮
class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品过滤类
    """
    pricemin = django_filters.NumberFilter(name='shop_price', lookup_expr='gte', help_text="最低价格")
    pricemax = django_filters.NumberFilter(name='shop_price', lookup_expr='lte', help_text="最高价格")
    # name = django_filters.CharFilter(name='name', lookup_expr='icontains')  # 模糊查询
    top_category = django_filters.NumberFilter(method='top_category_filter', help_text="父级类别")

    def top_category_filter(self, queryset, name, value):
        queryset_filter = queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))
        return queryset_filter

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax', 'is_hot', 'is_new']
