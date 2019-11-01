# coding:utf-8
"""
@author: Tracy
@mail: wanghongyu@ruijie.com.cn
@date: 2019.07.09
"""
from Common.com_function import *
from Data.basic_data import *
from Page.basic_page import *
from Common.driver import Pyse
from Common.login import Login
from Common.string_escape import string_escape
from Common.add_group import AddGroup
import unittest
import re
from Page.device_page import *
from Page.basic_page import *
from Data.device_data import *
from PIL import Image


class DeviceEg():

    def __init__(self):
        self.driver = Pyse("chrome")
        Login(self.driver, user_cloud_local, password_cloud_local, login_url_local).login()
        self.operate = ComFunction(self.driver)



    def test01(self):
        """调试代码"""
        # 调试代码
        # time.sleep(15)
        # self.operate.click_elem(login_close_tips_xpath)
        self.operate.click_elem(configuration_page_xpath)  # 没有等60s
        self.operate.click_elem(configuration_basic_xpath)
        time.sleep(15)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        # 调试代码

    def test01_eg_list(self):
        """验证添加设备流程"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        time.sleep(15)
        self.operate.click_elem(add_device_add_gateway)
        time.sleep(5)
        self.operate.elem_send_keys(add_device_alert_sn_gateway, add_device_alert_input_sn_gateway)
        self.operate.elem_send_keys(add_device_alert_eg_alias, 'EG123')
        self.operate.elem_send_keys(add_device_alert_password, 'ruijie123')
        self.operate.click_elem(add_device_alert_save_gateway)
        time.sleep(10)
        # eg_sn = self.operate.find_elem(device_eg_un_sn).text
        # eg_alias = self.operate.find_elem(device_eg_un_alias).text
        # eg_group = self.operate.find_elem(device_eg_un_group).text
        # print (eg_sn)
        # print (eg_alias)
        # print (eg_group)
        # print (self.group_name)
        # if eg_sn == add_device_alert_input_sn_gateway and eg_alias == 'EG123' and eg_group == self.group_name:
        #     k = 1
        # else:
        #     k = 0
        # self.assertEqual(k, 1)



    '''
    def test12_eg_restart(self):
        """验证EG可成功重启"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        self.operate.click_elem(add_device_eg_info.format(add_device_alert_input_sn_gateway))
        self.operate.click_elem(device_eg_detail_more)
        self.operate.click_elem(device_eg_restart)
        self.operate.click_elem(key_OK)
        self.operate.click_elem(add_device_device_info_close)
        time.sleep(10)
        self.operate.click_elem(device_list_refresh)
        text_offline = self.operate.find_elem(eg_list_tr1_state).text
        try:
            self.operate.find_elem(add_device_online_eg, By.XPATH, 300)
        except Exception as e:
            print (e)
        else:
            self.assertNotEqual(text_offline, 'Online')
    
    def test13_eg_edit(self):
        """验证EG详情页面的描述信息可进行编辑"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        self.operate.click_elem(add_device_eg_info.format(add_device_alert_input_sn_gateway))
        self.operate.click_elem(device_eg_detail_alias_edit)
        self.operate.elem_clear_send_keys(device_eg_detail_alias_input, 'EG')
        self.operate.click_elem(device_eg_detail_alias_ok)
        self.operate.click_elem(device_eg_detail_des_edit)
        self.operate.elem_clear_send_keys(device_eg_detail_des_input, 'abc')
        self.operate.click_elem(device_eg_detail_des_ok)
        eg_alias = self.operate.find_elem(device_eg_detail_alias).text
        eg_des = self.operate.find_elem(device_eg_detail_des).text
        if eg_alias == 'EG' and eg_des == 'abc':
            flag = 1
        else:
            flag = 0
        self.operate.click_elem(add_device_device_info_close)
        self.assertEqual(flag, 1)

    def test14_eg_password_edit(self):
        """验证可成功修改EG web 密码"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        self.operate.click_elem(add_device_eg_info.format(add_device_alert_input_sn_gateway))
        self.operate.click_elem(device_eg_detail_password)
        self.operate.elem_send_keys(device_eg_detail_password_input, 'ruijie123')
        self.operate.click_elem(device_eg_detail_password_ok)
        self.operate.click_elem(add_device_device_info_close)
        self.operate.click_elem(maintenance)
        self.operate.click_elem(view_log_operation_log)
        for i in range(100):
            time.sleep(60)
            log_des = self.operate.find_elem(device_eg_operation_log_des).text
            log_result = self.operate.find_elem(device_eg_operation_log_result).text
            self.operate.click_elem(device_eg_operation_log_refresh)
            if 'password' in log_des:
                break
        self.assertEqual(log_result, 'Success')
    '''
    def test15_eg_delete(self):
        """验证EG可成功删除"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        time.sleep(10)
        self.operate.click_elem(eg_unauth_delete)
        self.operate.click_elem(key_OK)
        time.sleep(10)









if __name__ == '__main__':
    eg = DeviceEg()
    eg.test01()
    while True:
        eg.test01_eg_list()
        eg.test15_eg_delete()

















