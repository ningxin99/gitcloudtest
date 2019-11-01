# coding:utf-8
import random
import string
str_c = string.digits+string.uppercase


def get_uuid():
    data = ""
    for i in range(15):
        index = random.randint(0, 35)
        data += str_c[index]
    return data


def get_group_name():
    print("get group name")
    data = ""
    for i in range(3):
        index = random.randint(0, 35)
        data += str_c[index]
    return data
