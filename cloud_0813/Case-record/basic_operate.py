# coding:utf-8
"""
@author: zhouxihong
@mail: zhouxihong@ruijie.com.cn
@date: 2019.04.29
"""
from selenium import webdriver
from Common.com_function import *
from Data.basic_data import *
from Page.basic_page import *
from Common.driver import Pyse
from Common.login import Login
import unittest


class BasicOperateCheck(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 登陆
        cls.driver = Pyse("chrome")
        Login(cls.driver, login_url_cloud).login()
        cls.operate = ComFunction(cls.driver)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test02_add_group(self):
        time.sleep(30)
        print ("添加分组")
        # 添加分组
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(groups_page_xpath)
        time.sleep(7)  # 延时30s,让页面加载出来 - 还有更好的实现方式
        self.operate.click_elem(add_groups_xpath)  # 点一次可能不生效, 多点几次

        self.operate.elem_send_keys(add_groups_input_name_xpath, add_groups_input_name_data)
        self.operate.click_elem(add_groups_next_page_xpath)
        self.operate.click_elem(add_groups_apply_xpath)
        # self.operate.elem_send_keys(add_device_input_sn_xpath, add_device_input_sn_data)
        self.operate.click_elem(add_device_apply_xpath)
        time.sleep(8)  # 还有更好的实现方式
        self.operate.click_elem(add_device_close_xpath)


    def test03_add_ssid(self):
        print ("添加SSID")
        # 将滚动条移动到页面底部
        js = "var q=document.getElementById('svgBlockDiv').scrollTop=100000"
        self.driver.execute_script(js)
        time.sleep(3)
        # 找到分组点击配置
        self.operate.click_elem(select_group_xpath_2.format(add_groups_input_name_data))
        self.operate.click_elem(select_setting_btn_xpath)
        time.sleep(10)
        # 断言
        print(add_groups_input_name_data+u"分组创建成功")
        # 添加SSID
        # add SSID 存在点击不到的情况，需要点击2次
        self.operate.click_elem(add_group_xpath)
        self.operate.elem_send_keys(add_SSID_name, add_SSID_ssid_name)
        self.operate.click_elem(add_SSID_enable_auth)
        self.operate.click_elem(add_SSID_one_click_login)
        self.operate.click_elem(add_SSID_save_ssid)
        # 配置安全密码
        self.operate.click_elem(add_SSID_security)
        self.operate.elem_send_keys(add_SSID_security_web_password, add_SSID_web_password)
        self.operate.elem_send_keys(add_SSID_security_telnet_password, add_SSID_telnet_password)
        # 保存
        self.operate.click_elem(add_SSID_save)
        time.sleep(10)
        # 断言

        ssid_field = self.operate.find_elems(add_SSID_field)
        self.assertEqual(len(ssid_field), 2)
        # if len(ssid_field) == 2:
        #     print(ssid_field)
        #     print("SSID:" + add_groups_input_name_data + u"添加成功")
        #     print ("SSID:" + add_SSID_ssid_name + u"添加成功")

    def test04_add_device(self):
        print ("添加设备")
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        time.sleep(10)
        self.operate.click_elem(add_device_add_access_point)
        self.operate.click_elem(add_device_alert_add_access_point)
        self.operate.elem_send_keys(add_device_alert_sn, add_device_alert_input_sn)
        self.operate.click_elem(add_device_alert_save)

        time.sleep(5)
        # 断言
        device_field = self.operate.find_elems(add_device_field)
        self.assertNotEqual(device_field, 0)
        # if device_field != 0:
        #     print(u"SN:"+add_device_alert_input_sn+u"添加成功")

        if self.operate.find_elems(add_device_online, By.XPATH, 600) != 0and self.operate.find_elem(add_device_synced, By.XPATH, 2400) != 0:
                try:
                    self.operate.click_elem(add_device_device_info.format(add_device_alert_input_sn))
                    ssid_text_0 = self.operate.find_elems(add_device_device_info_SSID, By.XPATH, 10)[0].text
                    ssid_text_1 = self.operate.find_elems(add_device_device_info_SSID, By.XPATH, 10)[1].text
                    print(ssid_text_0)
                    print(ssid_text_1)

                except Exception as e:
                    self.operate.click_elem(add_device_device_info_close)
                    time.sleep(10)
                else:
                    self.assertEqual(ssid_text_0, add_groups_input_name_data)
                    self.assertEqual(ssid_text_1, add_SSID_ssid_name)
                    # if ssid_text_0 == add_groups_input_name_data and ssid_text_1 == add_SSID_ssid_name:
                    #     a = u"SSID:"+ssid_text_0+" "+ssid_text_1+u"配置下发成功"
                    #     print(a)


if __name__ == '__main__':
    unittest.main()

