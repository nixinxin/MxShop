#!/usr/bin/python
# -*- coding:utf-8 -*-
from django.db.models import Q

__author__ = "xin nix"
from rest_framework import serializers
from goods.models import Goods, GoodsCategory, GoodsImage, Banner, GoodsCategoryBrand, IndexAd, HotSearchWords


# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()
#     def create(self, validated_data):
#         """
#         create and retturn a new Goods instance, given the validated data.
#         :param validated_data:
#         :return:
#         """
#         return Goods.objects.create(**validated_data)

class CategorySerializer3(serializers.ModelSerializer):
    """
    商品类别序列化
    """
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    """
    商品类别序列化
    """
    sub_cat = CategorySerializer3(many=True)  # 自嵌套

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    商品类别序列化
    """
    sub_cat = CategorySerializer2(many=True)  # 自嵌套

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image", )


class GoodsSerializer(serializers.ModelSerializer):

    # 直接省略所有字段和方法
    category = CategorySerializer()
    images = GoodsImageSerializer(many=True)  # 一个goods会有多个image

    class Meta:
        model = Goods
        # fields = ('name', 'click_num', 'market_price', 'add_time')
        fields = "__all__"


class HotWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotSearchWords
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = "__all__"


class BrandsSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsCategoryBrand
        fields = "__all__"


class IndexGoodsSerializer(serializers.ModelSerializer):

    #
    images = GoodsImageSerializer(many=True)  # 一个goods会有多个image

    class Meta:
        model = Goods
        fields = ("id", 'goods_front_image', 'images')


class IndexGategorySerializer(serializers.ModelSerializer):
    brands = BrandsSerializer(many=True)
    goods = serializers.SerializerMethodField()
    sub_cat = CategorySerializer2(many=True)
    ad_goods = serializers.SerializerMethodField()

    def get_ad_goods(self, obj):
        goods_json = {}
        ad_goods = IndexAd.objects.filter(category_id=obj.id)
        if ad_goods:
            goods_ins = ad_goods[0].goods
            # serializer嵌套serializer会出现破图，需要image 加域名， 通过content加域名
            goods_json = IndexGoodsSerializer(goods_ins, many=False, context={'request': self.context['request']}).data
        return goods_json

    def get_goods(self, obj):
        all_goods = Goods.objects.filter(Q(category_id=obj.id) | Q(category__parent_category_id=obj.id) | Q(
            category__parent_category__parent_category_id=obj.id))
        goods_serializer = GoodsSerializer(all_goods, many=True, context={'request': self.context['request']}).data
        return goods_serializer

    class Meta:
        model = GoodsCategory
        fields = "__all__"
