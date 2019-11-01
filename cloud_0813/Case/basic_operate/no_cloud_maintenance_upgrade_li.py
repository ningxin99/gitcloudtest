# coding:utf-8
"""
@author: Tracy
@mail: wanghongyu@ruijie.com.cn
@date: 2019.07.24
"""
from Common.com_function import *
from Data.basic_data import *
from Page.basic_page import *
from Page.device_page import *
from Common.driver import Pyse
from Common.login import Login
from Common.string_escape import string_escape
from Common.add_group import AddGroup
import unittest
import re

# 升级前的设备版本
global firmware_ap_before_upgrade, firmware_sw_now, firmware_eg_now
# 升级后的设备版本
global firmware_ap, firmware_sw, firmware_eg


class BasicCommon(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Pyse("chrome")
        Login(cls.driver, user_cloud_local, password_cloud_local, url=login_url_local).login()
        cls.operate = ComFunction(cls.driver)
        AddGroup(cls.driver, device_sn={
            'sw': add_device_alert_input_sn_switch,
            'ap': add_device_alert_input_sn,
            'eg': add_device_alert_input_sn_gateway
        }).add_group()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()


    def test11_upgrade_ap(self):
        """AP升级及验证操作"""

        time.sleep(5)
        self.operate.click_elem(maintenance)
        self.operate.click_elem(upgrade_upgrade)
        time.sleep(5)
        global firmware_ap_before_upgrade
        firmware_ap_before_upgrade = self.operate.find_elem(upgrade_device_AP_v).text
        print (u"AP的原本版本："+ firmware_ap_before_upgrade)
        self.operate.click_elem(upgrade_device_AP)
        self.operate.click_elem(select_firmware)
        self.operate.click_elem(select_firmware_private)
        global firmware_ap
        firmware_ap = self.operate.find_elem(select_firmware_list_tr1_td2).text
        print (firmware_ap_before_upgrade[-10:])
        if firmware_ap_before_upgrade[-10:] == firmware_ap[-10:]:
            self.operate.click_elem(select_firmware_list_tr2_td1)
            firmware_ap = self.operate.find_elem(select_firmware_list_tr2_td2).text
        else:
            self.operate.click_elem(select_firmware_list_tr1_td1)
        print (u"选择升级的AP版本：" + firmware_ap)
        print (firmware_ap[-10:])
        self.operate.click_elem(upgrade_finish)
        time.sleep(2)
        self.operate.click_elem(select_firmware_upgrade)
        time.sleep(15)

        # 验证AP升级操作成功
        # self.operate.click_elem(maintenance)
        self.operate.click_elem(view_log_upgrade_log)
        print (u"AP升级中~")
        while True:
            try:
                self.operate.find_elem(view_log_upgrade_log_success)
            except Exception as e:
                print (e)
                time.sleep(5)
                self.operate.click_elem(view_log_upgrade_log_refresh)
            else:
                self.operate.click_elem(upgrade_upgrade)
                break
        # 升级后的AP版本
        firmware_ap_before_upgrade_upgrade = self.operate.find_elem(upgrade_device_AP_v).text
        print (u"升级后的AP版本：" + firmware_ap_before_upgrade_upgrade)
        # global firmware_ap
        print (firmware_ap[-10:])
        print (firmware_ap_before_upgrade_upgrade[-10:])
        self.assertEqual(firmware_ap[-10:], firmware_ap_before_upgrade_upgrade[-10:])
        print (u"AP升级成功！")

    def test12_upgrade_ap(self):
        """AP版本回退操作"""
        # 回退到原本的版本
        time.sleep(5)
        self.operate.click_elem(maintenance)
        self.operate.click_elem(upgrade_upgrade)
        time.sleep(5)
        global firmware_ap_before_upgrade
        firmware_ap_before_upgrade = self.operate.find_elem(upgrade_device_AP_v).text
        print (u"回退后，查看当前AP的版本是：" + firmware_ap_before_upgrade)
        self.operate.click_elem(upgrade_device_AP)
        self.operate.click_elem(select_firmware)
        self.operate.click_elem(select_firmware_private)
        global firmware_ap
        firmware_ap = self.operate.find_elem(select_firmware_list_tr1_td2).text
        print (firmware_ap_before_upgrade[-10:])
        if firmware_ap_before_upgrade[-10:] == firmware_ap[-10:]:
            self.operate.click_elem(select_firmware_list_tr2_td1)
            firmware_ap = self.operate.find_elem(select_firmware_list_tr2_td2).text
        else:
            self.operate.click_elem(select_firmware_list_tr1_td1)
        print (u"选择回退的AP版本：" + firmware_ap)
        print (firmware_ap[-10:])
        self.operate.click_elem(upgrade_finish)
        time.sleep(2)
        self.operate.click_elem(select_firmware_upgrade)
        time.sleep(15)

        self.operate.click_elem(view_log_upgrade_log)
        print (u"AP回退中~")
        while True:
            try:
                self.operate.find_elem(view_log_upgrade_log_success)
            except Exception as e:
                print (e)
                time.sleep(5)
                self.operate.click_elem(view_log_upgrade_log_refresh)
            else:
                self.operate.click_elem(upgrade_upgrade)
                break
        firmware_ap_before_upgrade_upgrade = self.operate.find_elem(upgrade_device_AP_v).text
        global firmware_ap_before_upgrade
        # print (firmware_ap_before_upgrade[-10:])
        print (u"回退后的AP版本" + firmware_ap_before_upgrade_upgrade)
        self.assertEqual(firmware_ap[-10:], firmware_ap_before_upgrade_upgrade[-10:])
        print (u"AP回退成功！")
    #
    # def test13_upgrade_sw(self):
    #     """交换机升级操作"""
    #     time.sleep(5)
    #     self.operate.click_elem(maintenance)
    #     self.operate.click_elem(upgrade_upgrade)
    #     time.sleep(5)
    #     global firmware_sw_now
    #     firmware_sw_now = self.operate.find_elem(upgrade_device_SW_v).text
    #     print (u"SW原本的版本："+ firmware_sw_now)
    #     self.operate.click_elem(upgrade_device_SW)
    #     self.operate.click_elem(select_firmware)
    #     self.operate.click_elem(select_firmware_private)
    #     global firmware_sw
    #     firmware_sw = self.operate.find_elem(select_firmware_list_tr1_td2).text
    #     if firmware_sw_now[-10:] == firmware_sw[-10:]:
    #         self.operate.click_elem(select_firmware_list_tr2_td1)
    #         global firmware_sw
    #         firmware_sw = self.operate.find_elem(select_firmware_list_tr2_td2).text
    #     else:
    #         self.operate.click_elem(select_firmware_list_tr1_td1)
    #     print (u"选择升级的SW版本：" + firmware_sw)
    #     self.operate.click_elem(upgrade_finish)
    #     time.sleep(2)
    #     self.operate.click_elem(select_firmware_upgrade)
    #     time.sleep(15)
    #
    #     # 验证SW升级操作成功
    #     self.operate.click_elem(maintenance)
    #     self.operate.click_elem(view_log_upgrade_log)
    #     print (u"SW升级中~")
    #     while True:
    #         try:
    #             self.operate.find_elem(view_log_upgrade_log_success)
    #         except Exception as e:
    #             print (e)
    #             time.sleep(5)
    #             self.operate.click_elem(view_log_upgrade_log_refresh)
    #         else:
    #             self.operate.click_elem(upgrade_upgrade)
    #             break
    #     firmware_sw_now_upgrade = self.operate.find_elem(upgrade_device_SW_v).text
    #     # global firmware_sw
    #     # print (firmware_sw[-10:])
    #     print (u"升级后的SW版本："+ firmware_sw_now_upgrade[-10:])
    #     self.assertEqual(firmware_sw[-10:], firmware_sw_now_upgrade[-10:])
    #     print (u"SW升级成功！")
    #
    # def test14_upgrade_sw(self):
    #     """交换机回退操作"""
    #     time.sleep(5)
    #     self.operate.click_elem(maintenance)
    #     self.operate.click_elem(upgrade_upgrade)
    #     time.sleep(5)
    #     global firmware_sw_now
    #     firmware_sw_now = self.operate.find_elem(upgrade_device_SW_v).text
    #     self.operate.click_elem(upgrade_device_SW)
    #     self.operate.click_elem(select_firmware)
    #     self.operate.click_elem(select_firmware_private)
    #     global firmware_sw
    #     firmware_sw = self.operate.find_elem(select_firmware_list_tr1_td2).text
    #     if firmware_sw_now[-10:] == firmware_sw[-10:]:
    #         self.operate.click_elem(select_firmware_list_tr2_td1)
    #         global firmware_sw
    #         firmware_sw = self.operate.find_elem(select_firmware_list_tr2_td2).text
    #     else:
    #         self.operate.click_elem(select_firmware_list_tr1_td1)
    #     print (u"选择回退的SW版本：" + firmware_sw)
    #     self.operate.click_elem(upgrade_finish)
    #     time.sleep(2)
    #     self.operate.click_elem(select_firmware_upgrade)
    #     time.sleep(15)
    #
    #     # """验证交换机版本成功回退"""
    #     self.operate.click_elem(view_log_upgrade_log)
    #     print (u"SW回退中~")
    #     while True:
    #         try:
    #             self.operate.find_elem(view_log_upgrade_log_success)
    #         except Exception as e:
    #             print (e)
    #             time.sleep(5)
    #             self.operate.click_elem(view_log_upgrade_log_refresh)
    #         else:
    #             self.operate.click_elem(upgrade_upgrade)
    #             break
    #     firmware_sw_now_upgrade = self.operate.find_elem(upgrade_device_SW_v).text
    #     global firmware_sw_now
    #     # print (firmware_sw_now[-10:])
    #     print (u"回退后的SW版本：" + firmware_sw_now_upgrade[-10:])
    #     self.assertEqual(firmware_sw[-10:], firmware_sw_now_upgrade[-10:])
    #     print (u"SW回退成功！")
    #

    def test15_upgrade_eg(self):
        """EG升级操作"""
        time.sleep(5)
        self.operate.click_elem(maintenance)
        self.operate.click_elem(upgrade_upgrade)
        time.sleep(5)
        global firmware_eg_now
        firmware_eg_now = self.operate.find_elem(upgrade_device_EG_v).text
        print (u"EG原本的版本：" + firmware_eg_now)
        self.operate.click_elem(upgrade_device_EG)
        self.operate.click_elem(select_firmware)
        self.operate.click_elem(select_firmware_private)
        global firmware_eg
        firmware_eg = self.operate.find_elem(select_firmware_list_tr1_td2).text
        if firmware_eg_now[-10:] == firmware_eg[-10:]:
            self.operate.click_elem(select_firmware_list_tr2_td1)
            firmware_eg = self.operate.find_elem(select_firmware_list_tr2_td2).text
        else:
            self.operate.click_elem(select_firmware_list_tr1_td1)
        print (u"选择升级的EG版本：" + firmware_eg)
        self.operate.click_elem(upgrade_finish)
        time.sleep(2)
        self.operate.click_elem(select_firmware_upgrade)
        time.sleep(15)

        # 验证EG升级操作成功
        self.operate.click_elem(view_log_upgrade_log)
        print (u"EG升级中~")
        while True:
            try:
                self.operate.find_elem(view_log_upgrade_log_success)
            except Exception as e:
                print (e)
                time.sleep(5)
                self.operate.click_elem(view_log_upgrade_log_refresh)
            else:
                self.operate.click_elem(upgrade_upgrade)
                break
        # global firmware_eg
        firmware_eg_now_upgrade = self.operate.find_elem(upgrade_device_EG_v).text
        print (u"升级后的EG版本：" + firmware_eg_now_upgrade)
        self.assertEqual(firmware_eg[-10:], firmware_eg_now_upgrade[-10:])
        print (u"EG升级成功！")


    def test16_upgrade_eg(self):
        """EG版本回退操作"""
        time.sleep(5)
        self.operate.click_elem(maintenance)
        self.operate.click_elem(upgrade_upgrade)
        time.sleep(5)
        global firmware_eg_now
        firmware_eg_now = self.operate.find_elem(upgrade_device_EG_v).text
        self.operate.click_elem(upgrade_device_EG)
        self.operate.click_elem(select_firmware)
        self.operate.click_elem(select_firmware_private)
        global firmware_eg
        firmware_eg = self.operate.find_elem(select_firmware_list_tr1_td2).text
        if firmware_eg_now[-10:] == firmware_eg[-10:]:
            self.operate.click_elem(select_firmware_list_tr2_td1)
            firmware_eg = self.operate.find_elem(select_firmware_list_tr2_td2).text
        else:
            self.operate.click_elem(select_firmware_list_tr1_td1)
        print (u"选择回退的EG版本：" + firmware_eg)
        self.operate.click_elem(upgrade_finish)
        time.sleep(2)
        self.operate.click_elem(select_firmware_upgrade)
        time.sleep(15)

        # """验证EG版本成功回退"""
        self.operate.click_elem(view_log_upgrade_log)
        print (u"EG回退中~")
        while True:
            try:
                self.operate.find_elem(view_log_upgrade_log_success)
            except Exception as e:
                print (e)
                self.operate.click_elem(view_log_upgrade_log_refresh)
            else:
                self.operate.click_elem(upgrade_upgrade)
                break
        # """验证EG版本成功回退"""
        global firmware_eg_now
        firmware_eg_now_upgrade = self.operate.find_elem(upgrade_device_EG_v).text
        print (u"回退后的EG版本：" + firmware_eg_now_upgrade)
        self.assertEqual(firmware_eg[-10:], firmware_eg_now_upgrade[-10:])
        print (u"EG回退成功！")


    def test20_upgrade_batch(self):
        """验证设备可批量升级"""
        self.operate.click_elem(maintenance)
        self.operate.click_elem(upgrade_upgrade)
        time.sleep(5)
        self.operate.click_elem(upgrade_upgrade_all)
        for i in range(3):
            print select_firmware_current_firmware.format(str(i))
            ver_current = self.operate.find_elem(select_firmware_current_firmware.format(str(i))).text
            self.operate.click_elem(select_firmware_batch.format(str(i)))
            self.operate.click_elem(select_firmware_private)
            firmware = self.operate.find_elem(select_firmware_list_tr1_td2).text
            # print (firmware_ap_before_upgrade[-10:])
            print i
            if ver_current[-10:] == firmware[-10:]:
                self.operate.click_elem(select_firmware_list_tr2_td1)
                firmware = self.operate.find_elem(select_firmware_list_tr2_td2).text
            else:
                self.operate.click_elem(select_firmware_list_tr1_td1)
            self.operate.click_elem(upgrade_finish)
        self.operate.click_elem(select_firmware_upgrade)
        time.sleep(15)
        self.operate.click_elem(maintenance)
        self.operate.click_elem(view_log_upgrade_log)
        print (u"升级中~")
        while True:
            try:
                self.operate.find_elem(view_log_upgrade_log_success)
                self.operate.find_elem(view_log_upgrade_log_success_2)
                self.operate.find_elem(view_log_upgrade_log_success_3)
            except Exception as e:
                print (e)
                time.sleep(60)
                self.operate.click_elem(view_log_upgrade_log_refresh)
            else:
                break
        try:
            self.operate.find_elem(view_log_upgrade_log_success)
            self.operate.find_elem(view_log_upgrade_log_success_2)
            self.operate.find_elem(view_log_upgrade_log_success_3)
        except Exception as e:
            self.assertIsNotNone(None, u"批量升级不成功")





if __name__ == '__main__':
    unittest.main()
