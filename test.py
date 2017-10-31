#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "xin nix"
import requests

url = "http://127.0.0.1:8000/userfavs/11"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\nxinnix\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n1993930ni\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'authorization': "JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IiIsImV4cCI6MTUwODU3MTAxNCwidXNlcl9pZCI6MywidXNlcm5hbWUiOiJ4aW5uaXgifQ.ire1-eloxZzwfNTsSCQD5vUIVAlaBxFlFEedoMMJNI4",    'cache-control': "no-cache",
    'postman-token': "e0c61ba1-5f45-3334-381b-506db0944779"
    }

response = requests.request("DELETE", url, data=payload, headers=headers)

print(response.text)

# url = "http://127.0.0.1:8000/userfavs/10"
#
#
#
# response = requests.request("DELETE", url)
#
# print(response.text)