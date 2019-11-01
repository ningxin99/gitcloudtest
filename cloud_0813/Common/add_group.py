# coding=utf-8
"""
@author: Tracy
@mail: wanghongyu@ruijie.com.cn
@date: 2019.05.27
"""

import os
from Common.com_function import *
from Data.basic_data import *
from Page.basic_page import *
from Common.uuid import get_group_name
from Page.config_page import *
from Page.basic_page import *
from Common.driver import Pyse
class AddGroup:
    def __init__(self, driver, device_sn='', sub_group=False, group_name=get_group_name(),  eg_password='ruijie123', **alias):

        self.driver = driver
        self.operate = ComFunction(self.driver)
        self.group_name = group_name
        self.device_sn = device_sn
        self.eg_password = eg_password
        self.alias = alias
        self.sub_group = sub_group


    def add_group(self):
        # 添加分组
        self.group_name = get_group_name()
        print (u'创建的分组名为：'+self.group_name)
        time.sleep(5)
        # self.driver.implicitly_wait(90)
        # self.operate.click_elem(login_close_tips_xpath)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(groups_page_xpath)
        time.sleep(15)
        # self.driver.refresh()
        # time.sleep(20)
        self.operate.click_elem(add_groups_xpath)  # 点一次可能不生效, 多点几次
        time.sleep(10)
        self.operate.elem_send_keys(add_groups_input_name_xpath, self.group_name)
        self.operate.click_elem(add_groups_next_page_xpath)
        self.operate.elem_clear_send_keys(add_groups_add_wifi_name_default, add_SSID_ssid_name_default)
        self.operate.click_elem(add_groups_apply_xpath)
        if self.sub_group is True:
            self.operate.click_elem(add_device_apply_xpath)
            time.sleep(5)
            self.operate.click_elem(add_device_close_xpath)
            time.sleep(5)
            # 将显示分组页面下拉到最后
            js = "var q=document.getElementById('svgBlockDiv').scrollTop=100000"
            self.driver.execute_script(js)
            time.sleep(5)
            self.operate.click_elem(select_group_xpath.format(self.group_name))
            self.operate.click_elem(config_group_subgroup)
            self.operate.elem_send_keys(config_group_subgroup_add, sub_group_name_data + self.group_name)
            self.operate.click_elem(config_group_subgroup_add_save)
        if 'sw' in self.device_sn and 'eg' in self.device_sn and 'ap' in self.device_sn:
            print (self.alias)
            self.operate.elem_send_keys(add_device_input_sn_xpath, self.device_sn['ap'])
            if self.alias != {}:
                self.operate.elem_send_keys(add_device_input_alias_xpath, self.alias['alias'])
            self.operate.click_elem(add_group_device_sw)
            self.operate.elem_send_keys(add_device_input_sn_sw_xpath, self.device_sn['sw'])
            if self.alias != {}:
                self.operate.elem_send_keys(add_device_input_alias_sw_xpath, self.alias['alias'])
            self.operate.click_elem(add_group_device_eg)
            self.operate.elem_send_keys(add_device_input_sn_eg_xpath, self.device_sn['eg'])
            if self.alias != {}:
                self.operate.elem_send_keys(add_device_input_alias_eg_xpath, self.alias['alias'])
            self.operate.elem_send_keys(add_device_input_password_eg_xpath, self.eg_password)
        elif 'sw' in self.device_sn:
            self.operate.click_elem(add_group_device_sw)
            self.operate.elem_send_keys(add_device_input_sn_sw_xpath, self.device_sn['sw'])
            if self.alias != {}:
                self.operate.elem_send_keys(add_device_input_alias_sw_xpath, self.alias['alias'])
        elif 'eg' in self.device_sn:
            self.operate.click_elem(add_group_device_eg)
            self.operate.elem_send_keys(add_device_input_sn_eg_xpath, self.device_sn['eg'])
            if self.alias != {}:
                self.operate.elem_send_keys(add_device_input_alias_eg_xpath, self.alias['alias'])
            self.operate.elem_send_keys(add_device_input_password_eg_xpath, self.eg_password)
        elif 'ap' in self.device_sn:
            self.operate.elem_send_keys(add_device_input_sn_xpath, self.device_sn['ap'])
            if self.alias != {}:
                self.operate.elem_send_keys(add_device_input_alias_xpath, self.alias['alias'])
        elif self.device_sn == '':
            pass
        else:
            raise ValueError(u'输入格式不合法')
        self.operate.click_elem(add_group_device_ap)
        self.operate.click_elem(add_device_apply_xpath)
        time.sleep(5)
        self.operate.click_elem(add_device_close_xpath)
        time.sleep(5)
        # 将显示分组页面下拉到最后
        js = "var q=document.getElementById('svgBlockDiv').scrollTop=100000"
        self.driver.execute_script(js)
        time.sleep(5)
        # print (select_group_xpath_2.format(self.group_name))
        # 找到分组点击配置,进入页面config_basic
        self.operate.click_elem(select_group_xpath.format(self.group_name))
        self.operate.click_elem(select_setting_btn_xpath)
        time.sleep(10)
        # 配置安全密码
        self.operate.click_elem(add_SSID_security)
        self.operate.elem_send_keys(add_SSID_security_web_password, add_SSID_web_password)
        self.operate.elem_send_keys(add_SSID_security_telnet_password, add_SSID_telnet_password)
        # 保存
        self.operate.click_elem(add_SSID_save)
        time.sleep(10)


        return self.group_name


