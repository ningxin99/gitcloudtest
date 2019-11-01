# coding=utf-8
"""
@author: Tracy
@mail: wanghongyu@ruijie.com.cn
@date: 2019.06.04
"""
"""
添加自定义的断言，断言失败抛出AssertionError就OK
"""


def assert_http_code(response, code_list=None):
    res_code = response.status_code
    if not code_list:
        code_list = [200]
    if res_code not in code_list:
        raise AssertionError(u"响应code不在列表中")
    # 抛出AssertionError,unittest会自动判别用例为failure

