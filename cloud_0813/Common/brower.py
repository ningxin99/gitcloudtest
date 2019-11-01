# coding:utf-8
"""
@author: Tracy
@mail: wanghongyu@ruijie.com.cn
@date: 2019.05.28
"""
import  time
import os
from selenium import webdriver
from config import *

# IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'
# PHANTOMJSDRIVER_PATH = DRIVER_PATH + '\phantomjs.exe'
# CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
#
# TYPES = {'firefox': webdriver.firefox(), 'chrome': webdriver.Chrome(), 'ie': webdriver.ie, 'phantomjs': webdriver.phantomjs}
# EXECUTABLE_PATH = {'firefox': 'wires', 'chrome': CHROMEDRIVER_PATH, 'ie': IEDRIVER_PATH,
#                    'phantonjs': PHANTOMJSDRIVER_PATH
#                    }


class Browser(object):
    # def __init__(self, browser_type='chrome'):
    #     self._type = browser_type.lower()
    #     if self._type in TYPES:
    #         self.browser = TYPES[self._type]
    #     else:
    #         pass
    #     self.driver = None
    def __init__(self, browser_type='chrome'):
        if browser_type == "firefox" or browser_type == "ff":
            self.driver = webdriver.Firefox()
        elif browser_type == "chrome":
            self.driver = webdriver.Chrome()
        elif browser_type == "internet explorer" or browser_type == "ie":
            self.driver = webdriver.Ie()
        else:
            raise NameError(u"输入的浏览器名称有误")




    def get(self, url, maximize_window=True, implicitly_waite=30):
        # self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_waite)
        return self









