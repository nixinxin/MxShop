#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "xin nix"

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()


# @receiver(post_save, sender=User)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         password = instance.password
#         instance.set_password(password)
#         instance.save()
#         # Token.objects.create(user=instance)
#