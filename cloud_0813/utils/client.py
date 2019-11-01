# coding=utf-8
"""
@author: Tracy
@mail: wanghongyu@ruijie.com.cn
@date: 2019.06.03
"""
"""
对于HTTP接口添加HTTP Client,发送http请求
"""

import requests
from utils.log import logger1

METHODS = ['GET', 'POST', 'HEAD', 'TRACE', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']



class HTTPClient(object):
    def __init__(self, url, method='GET', headers=None, cookies=None):
        self.url = url
        self.session = requests.session()
        self.method = method.upper()
        if self.method not in METHODS:
            raise NameError(u"不支持的method:{0}".format(self.method))
        self.set_headers(headers)
        self.set_cookies(cookies)

    def set_header(self, headers):
        if headers:
            self.session.headers.update(headers)

    def set_cookies(self, cookies):
        if cookies:
            self.session.cookies.update(cookies)

    def send(self, params=None, data=None, **kwargs):
        response = self.session.request(meathod=self.method,
                                        url=self.url,
                                        params=params,
                                        data=data,
                                        **kwargs
                                        )
        response.encoding("utf-8")
        logger1.debug('{0} {1}'.format(self.method, self.url))
        logger1.debug("请求成功：{0}\n{1}".format(response, response.text))
        return response
        




