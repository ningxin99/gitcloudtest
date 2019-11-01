# coding:utf-8

import unittest
from utils.log import logger1
from selenium import webdriver
from config import *
from utils.HTMLTestRunner import HTMLTestRunner
from Common.com_function import *
from Data.basic_data import *
from Page.basic_page import *
from Common.add_group import AddGroup
from Common.login import Login
from Common.uuid import get_group_name
import re


class TestDeviceConfig(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.operate = ComFunction(self.driver)
        # self.driver.maximize_window()
        # self.driver.get(login_url_cloud)
        # 登陆
        # self.operate = ComFunction()
        # self.operat.get("https://cloud-as.ruijienetworks.com")
        # self.driver = ComFunction(Browser("chrome").get("https://cloud-as.ruijienetworks.com")).driver
        # self.operate.elem_send_keys(user_name_xpath, login_user_name_data_11)
        # self.operate.elem_send_keys(password_xpath, login_password_data_11)
        # self.operate.click_elem(login_btn_xpath)
        Login(self.driver, login_url_cloud).login()
        AddGroup(self.driver).add_group()

    # @classmethod
    # def tearDown(self):
    #     self.driver.quit()

    def test_device_config(self):
        u'''验证命令下发的正确性'''
        # time.sleep(20)
        # self.operate.click_elem(add_device_monitoring)
        # self.operate.click_elem(add_device_access_point)
        # self.operate.click_elem(device_select)
        # self.operate.click_elem(device_more)
        # self.operate.click_elem(device_diagnosis)
        # self.operate.click_elem(device_running_config)
        # time.sleep(10)
        # js1 = 'return $("#cli_result").val();'
        # # print(self.driver.execute_script(js1))
        # self.assertIn("!",
        #               self.driver.execute_script(js1),
        #               "配置下发不成功")
        f = open(os.path.join(CONFIG_PATH, 'cmd.text'), 'r+')
        # f.write(self.driver.execute_script(js1))
        f.seek(0, 0)
        text = f.read()
        f.close()
        t = re.search('interface BVI 1[\S\s]*ip address dhcp', text)
        print(t.group())
        self.assertIsNotNone(t, u"jjj配置下发不成功")
        self.assertIn('interface BVI 1', text, u"配置下发不成功")
        self.assertIn('ip address dhcp', text, u"配置下发不成功")

        # print (text)

        # while True:
        #     text = f.readline()
        #     if not text:
        #         break
        #     print (text)





if __name__ == '__main__':
    unittest.main()
