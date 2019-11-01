# coding=utf-8
"""
@author: Tracy
@mail: wanghongyu@ruijie.com.cn
@date: 2019.08.08
"""

from Common.com_function import *
from Data.basic_data import *
from Page.basic_page import *
from Page.config_page import *
from Data.device_data import *


class GroupInit:
    def __init__(self, driver):
        self.driver = driver
        self.operate = ComFunction(self.driver)


    def group_init(self):
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(configuration_basic_xpath)
        time.sleep(5)
        # 添加白名单
        self.operate.click_elem(config_basic_advance)
        self.operate.click_elem(config_basic_advance_add_white)
        self.operate.elem_send_keys(config_basic_advance_add_white_ip, white_list_ip_input)
        self.operate.click_elem(key_OK)
        self.operate.click_elem(add_SSID_save)
        time.sleep(5)
        # 设置国家码
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(config_RF_planning_xpath)
        time.sleep(5)
        self.operate.click_elem(config_RF_radio1_bandwidth_2)
        self.operate.click_elem(config_RF_radio2_bandwidth_5)
        self.operate.click_elem(config_RF_radio3_bandwidth_5)
        self.operate.click_elem(config_RF_radio_save)
        time.sleep(5)
        # 设置功率和信道
        self.operate.click_elem(config_RF_select_ap)
        self.operate.elem_clear_send_keys(config_RF_radio1_power, ap_radio1_power_input)
        self.operate.elem_clear_send_keys(config_RF_radio2_power, ap_radio2_power_input)
        self.operate.click_elem(config_RF_radio1_channel_3)
        self.operate.click_elem(config_RF_radio2_channel_157)
        self.operate.click_elem(config_RF_radio_power_apply)
        time.sleep(5)
        # 蓝牙配置
        # self.operate.click_elem(configuration_page_xpath)
        # self.operate.click_elem(config_bluetooth_xpath)
        # time.sleep(5)
        # self.operate.click_elem(config_bluetooth_add)
        # self.operate.elem_send_keys(config_bluetooth_add_sn, add_device_alert_input_sn)
        # self.operate.click_elem(config_bluetooth_add_statue_on)
        # self.operate.elem_send_keys(config_bluetooth_add_UUID, bluetooth_UUID_input)
        # self.operate.elem_send_keys(config_bluetooth_major, bluetooth_major_input)
        # self.operate.elem_send_keys(config_bluetooth_minor, bluetooth_minor_input)
        # self.operate.click_elem(config_bluetooth_save)
        # time.sleep(5)





