# coding:utf-8
"""
@author: Tracy
@mail: wanghongyu@ruijie.com.cn
@date: 2019.05.15
"""
from selenium import webdriver
from Common.com_function import *
from Data.basic_data import *
from Page.basic_page import *
import datetime
from Common.driver import Pyse
from Common.login import Login
import unittest


class BasicOperateCheck(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        # self.operate = ComFunction(self.driver)
        # self.driver.get(login_url)

        # 登陆
        cls.driver = Pyse("chrome")
        Login(cls.driver, login_url_cloud).login()
        cls.operate = ComFunction(cls.driver)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



    def test01_add_ssid(self):
        print("验证SSID")
        u"""验证SSID"""
        # configuration/basic
        time.sleep(10)
        self.operate.click_elem(configuration_page_xpath)# 没有等60s
        self.operate.click_elem(configuration_basic_xpath)
        # 初始化分组为空一个SSID，一个设备，添加SSID
        time.sleep(60)
        self.operate.click_elem(delet_SSID_config)
        self.operate.click_elem(delet_SSID_confirm)
        self.operate.click_elem(add_group_xpath)
        self.operate.elem_send_keys(add_SSID_name, add_SSID_ssid_name)
        self.operate.click_elem(add_SSID_save_ssid)
        # 配置安全密码
        # self.operate.click_elem(add_SSID_security)
        # self.operate.elem_send_keys(add_SSID_security_web_password, add_SSID_web_password)
        # self.operate.elem_send_keys(add_SSID_security_telnet_password, add_SSID_telnet_password)
        # 保存
        self.operate.click_elem(add_SSID_save)
        print ('SSID:'+add_SSID_ssid_name + ' start config ,   the start time is' + now_time)
        time.sleep(15)


    def test02_add_device(self):
        print ("验证设备")
        u"""验证设备"""
        # monitoring/access point
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        time.sleep(10)
        # 添加AP
        self.operate.click_elem(add_device_add_access_point)
        self.operate.click_elem(add_device_alert_add_access_point)
        self.operate.elem_send_keys(add_device_alert_sn, add_device_alert_input_sn)
        self.operate.click_elem(add_device_alert_save)
        time.sleep(10)
        # 添加Switch
        self.operate.click_elem(add_device_switch)
        self.operate.click_elem(add_device_add_switch)
        self.operate.click_elem(add_device_alert_add_access_point)
        self.operate.elem_send_keys(add_device_alert_sn_switch, add_device_alert_input_sn_switch)
        self.operate.click_elem(add_device_alert_save_switch)
        time.sleep(10)
        # 添加EG
        self.operate.click_elem(add_device_gateway)
        self.operate.click_elem(add_device_add_gateway)
        self.operate.elem_send_keys(add_device_alert_sn_gateway, add_device_alert_input_sn_gateway)
        self.operate.elem_send_keys(add_device_alert_password, add_device_alert_input_password)
        self.operate.click_elem(add_device_alert_save_gateway)
        time.sleep(10)


    def test03_check_device(self):
        u"""验证设备"""
        print ("验证设备")
        self.operate.click_elem(add_device_gateway)
        if self.operate.find_elems(add_device_online, By.XPATH, 600) != 0:
            print ("EG online")
        self.operate.click_elem(add_device_switch)
        if self.operate.find_elems(add_device_online, By.XPATH, 600) != 0:
            print ('SW online')




    def test04_check_ssid(self):
        print("验证SSID")
        u"""验证SSID"""
        self.operate.click_elem(add_device_access_point)
        # time.sleep(70)
        print ('the state of device is Syncing or not Synced,please wait!')
        try:
            if self.operate.find_elems(add_device_online, By.XPATH, 600) != 0 and self.operate.find_elem(add_device_synced, By.XPATH, 2400) != 0:
                self.operate.click_elem(add_device_device_info.format(add_device_alert_input_sn))
                print ('configuration synchronized end,the end time is' + now_time)
                # print ((now_time_end-now_time_start).days)
        except:
            print ("SSID config lose in 40 mins")
            self.operate.click_elem(view_log_maintenance)
            self.operate.click_elem(view_log_config_log)
            print ('config log start time is'+self.operate.find_elem(view_log_config_log_start_time).text)
            print ('config log end time is'+self.operate.find_elem(view_log_config_log_end_time).text)
            print ('\n')
        else:
            try:
                ssid_text = self.operate.find_elem(add_device_device_info_SSID, By.XPATH, 10).text
            except:
                self.operate.click_elem(add_device_device_info_close)
                print ('did not get the ssid name')
            else:
                if ssid_text == add_SSID_ssid_name:
                    print ('SSID:' + ssid_text + " config complete successful")
                    print('\n')
                self.operate.click_elem(add_device_device_info_close)


if __name__ == '__main__':
    unittest.main()









