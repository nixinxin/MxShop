#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "xin nix"

import re
from datetime import timedelta, datetime

from rest_framework.validators import UniqueTogetherValidator

from MxShop.settings import REGEX_MOBILE
from user_operation.models import UserFav, UserLeavingMessage, UserAddress

from rest_framework import serializers
from goods.serializers import GoodsSerializer


class UserFavDetailSerializer(serializers.Serializer):
    goods = GoodsSerializer()  # goods本身是一个外键，它对应一个对象而不是一对多的关系，不用加many

    class Meta:
        model = UserFav
        fields = ('goods', 'id')


class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav

        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=("user", 'goods'),
                message="已经收藏"  # 不在指出具体字段的错误
            )
        ]

        fields = ("user", 'goods', 'id')


class LeavingMessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserLeavingMessage
        fields = ("user", "message_type", "subject", "message", "file", 'id', 'add_time')


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    # 验证函数取名方法： validate + model中验证字段的名字
    def validate_signer_mobile(self, mobile):
        """
        验证手机号码
        :param moobile:
        :return:
        """
        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")
        return mobile

    class Meta:
        model = UserAddress
        fields = ('id', "user", "province", "city", "district", "address", 'signer_name', 'signer_mobile', 'add_time')
