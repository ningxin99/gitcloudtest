import pytest
from Common.com_function import *
from Data.basic_data import *
from Data.device_data import *
from Page.basic_page import *
from Common.driver import Pyse
from Common.login import Login
from Common.string_escape import string_escape
from Common.add_group import AddGroup
import unittest
import re
from Page.device_page import *
from Page.basic_page import *



class TestDemo:

    @classmethod
    def setup_class(cls):
        cls.driver = Pyse("chrome")
        Login(cls.driver, user_cloud, password_cloud, login_url_cloud).login()
        cls.operate = ComFunction(cls.driver)
        AddGroup(cls.driver, device_sn={'ap': add_device_alert_input_sn}).add_group()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


    def test_1(self):
        """验证AP别名可修改成功"""
        self.operate.click_elem(web_cli_close)
        self.operate.click_elem(add_device_access_point)
        self.operate.click_elem(device_alias)
        self.operate.elem_clear_send_keys(device_alias_input, device_ap_input_alias_data)
        self.operate.click_elem(device_alias_input_confirm)
        ap_alias = self.operate.find_elem(device_alias).text
        time.sleep(5)
        self.assertEqual(ap_alias, device_ap_input_alias_data)

