#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "xin nix"

from raven import Client

client = Client('___DSN___')

try:
    1 / 0
except ZeroDivisionError:
    client.captureException()



