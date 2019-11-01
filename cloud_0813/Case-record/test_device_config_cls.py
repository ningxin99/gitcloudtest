# coding:utf-8

import unittest
from utils.log import logger1
from selenium import webdriver
from config import *
from utils.HTMLTestRunner import HTMLTestRunner
from Common.com_function import *
from Data.basic_data import *
from Page.basic_page import *
from Common.driver import Pyse
from Common.login import Login


class TestDeviceConfig(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.operate = ComFunction(self.driver)
        self.driver.get(login_url)

        # 登陆
        # cls.driver = Pyse("chrome")
        # Login(cls.driver, login_url).login()
        # cls.operate = ComFunction(cls.driver)


    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    def test_device_config(self):
        u'''验证命令下发的正确性'''
        time.sleep(10)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        self.operate.click_elem(device_select)
        self.operate.click_elem(device_more)
        self.operate.click_elem(device_diagnosis)
        self.operate.click_elem(device_running_config)
        time.sleep(10)
        js1 = 'return $("#cli_result").val();'
        print(self.driver.execute_script(js1))
        self.assertIn("!",
                      self.driver.execute_script(js1),
                      "配置下发不成功")



if __name__ == '__main__':
    unittest.main()
