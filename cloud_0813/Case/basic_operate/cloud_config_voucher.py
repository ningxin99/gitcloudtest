# coding:utf-8
"""
@author: Tracy
@mail: wanghongyu@ruijie.com.cn
@date: 2019.07.15
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
from Page.config_page import *
from Page.basic_page import *
from Data.device_data import *
from selenium.webdriver.common.keys import Keys


class CloudConfigVoucher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Pyse("chrome")
        Login(cls.driver, user_cloud_local, password_cloud_local, login_url_local).login()
        cls.operate = ComFunction(cls.driver)
        cls.group_name = AddGroup(cls.driver, device_sn={'ap': add_device_alert_input_sn}).add_group()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # def test01(self):
    #     time.sleep(15)
    #     self.operate.click_elem(login_close_tips_xpath)
        # self.operate.click_elem(configuration_page_xpath)
        # self.operate.click_elem(config_voucher)
        # time.sleep(5)

    def test01_add_package(self):
        """验证添加的voucher package列表中的描述信息与填入的信息一致"""
        print (self.group_name)
        time.sleep(10)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(config_voucher)
        time.sleep(5)
        self.operate.click_elem(config_manage_package)
        self.operate.click_elem(config_add_package)
        self.operate.elem_send_keys(config_package_name, package_name_input)
        self.operate.elem_send_keys(config_package_des, package_des_input)
        self.operate.elem_send_keys(config_package_price, package_price_input)
        self.operate.click_elem(config_package_max_client_1)
        self.operate.click_elem(config_package_period_week)
        self.operate.click_elem(config_package_quota_500)
        self.operate.click_elem(config_package_max_download_rate_2M)
        self.operate.click_elem(config_package_max_upload_rate_2M)
        self.operate.click_elem(key_OK)
        time.sleep(2)
        for i in range(1, 10):
            package_list_i = self.operate.find_elem(config_package_list.format(i)).text
            print (package_list_i)
            if i == 1:
                self.assertEqual(package_list_i, package_name_input)
            elif i == 2:
                self.assertEqual(package_list_i, package_des_input)
            elif i == 3:
                self.assertEqual(package_list_i[0], package_price_input)
            elif i == 4:
                self.assertEqual(package_list_i, '1')
            elif i == 6:
                self.assertEqual(package_list_i, '1 Week')
            elif i == 7:
                self.assertEqual(package_list_i, '500 MB')
            elif i == 8:
                self.assertEqual(package_list_i, '2 Mbps')
            elif i == 9:
                self.assertEqual(package_list_i, '2 Mbps')




    def test02_add_package_delete(self):
        """验证package list 可以添加多条并搜索"""
        time.sleep(10)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(config_voucher)
        time.sleep(5)
        self.operate.click_elem(config_manage_package)
        self.operate.click_elem(config_add_package)
        self.operate.elem_send_keys(config_package_name, package_name_input_2)
        self.operate.click_elem(key_OK)
        time.sleep(5)
        # self.operate.click_elem(config_add_package)
        # self.operate.elem_send_keys(config_package_name, package_name_input_2)
        # self.operate.click_elem(key_OK)
        self.operate.elem_send_keys(config_package_search, package_name_input_2)
        self.operate.elem_send_keys(config_package_search, Keys.ENTER)
        t = self.operate.find_elem(config_package_list.format(1)).text
        num = len(self.operate.find_elems(config_package_list_tr))
        self.assertEqual(num, 1)
        self.assertEqual(t, package_name_input_2)


    def test03_add_package_delete(self):
        """验证package list 可以删除"""
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(config_voucher)
        time.sleep(5)
        self.operate.click_elem(config_manage_package)
        num = len(self.operate.find_elems(config_package_list_tr))
        time.sleep(10)
        self.operate.click_elem(config_package_tr1_delete)
        self.operate.click_elem(key_OK)
        time.sleep(5)
        num_delete = len(self.operate.find_elems(config_package_list_tr))
        print (num, num_delete)
        self.assertEqual(num - num_delete, 1)



    def test04_add_package_edit(self):
        """验证package可编辑，voucher package列表中的描述信息与编辑填入的信息一致"""
        time.sleep(10)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(config_voucher)
        time.sleep(5)
        self.operate.click_elem(config_manage_package)
        self.operate.click_elem(config_package_tr1_edit)
        self.operate.elem_clear_send_keys(config_package_name, package_name_input_edit)
        self.operate.elem_clear_send_keys(config_package_price, package_price_input_edit)
        self.operate.click_elem(config_package_max_client_2)
        self.operate.click_elem(config_package_period_day)
        self.operate.click_elem(config_package_quota_G)
        self.operate.click_elem(config_package_max_download_rate_256k)
        self.operate.click_elem(config_package_max_upload_rate_5M)
        self.operate.click_elem(key_OK)
        time.sleep(2)
        for i in range(1, 10):
            package_list_i = self.operate.find_elem(config_package_list.format(i)).text
            print (package_list_i)
            try:
                if i == 1:
                    self.assertEqual(package_list_i, package_name_input_edit)
                elif i == 3:
                    self.assertEqual(package_list_i[0], package_price_input_edit)
                elif i == 4:
                    self.assertEqual(package_list_i, '2')
                elif i == 6:
                    self.assertEqual(package_list_i, '1 Day')
                elif i == 7:
                    self.assertEqual(package_list_i, '1 GB')
                elif i == 8:
                    self.assertEqual(package_list_i, '256 Kbps')
                elif i == 9:
                    self.assertEqual(package_list_i, '5 Mbps')
            except Exception as e:
                print e
   
    def test05_voucher_print(self):
        """验证输入的voucher信息与生成的voucher list显示的信息一致"""
        time.sleep(5)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(config_voucher)
        time.sleep(5)
        self.operate.click_elem(config_voucher_print)
        self.operate.elem_send_keys(config_voucher_name, voucher_name_1)
        self.operate.click_elem(config_voucher_key_print)
        print_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        time.sleep(10)
        handles = self.driver.window_handles
        self.driver.switch_to_window(handles[-1])
        self.driver.close()
        self.driver.switch_to_window(handles[0])
        time.sleep(5)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(config_voucher)
        self.operate.click_elem(config_voucher_list_refresh)
        time.sleep(2)
        for i in range(1, 15):
            voucher_list_i = self.operate.find_elem(config_voucher_list_tr.format(i)).text
            print voucher_list_i
            if i == 3:
                self.assertEqual(voucher_list_i, voucher_name_1)
            elif i == 4:
                self.assertEqual(voucher_list_i, package_name_input_edit)
            elif i == 5:
                self.assertEqual(voucher_list_i[0], package_price_input_edit)
            elif i == 6:
                self.assertEqual(voucher_list_i, '1 Day')
            elif i == 7:
                print voucher_list_i[:-3]
                self.assertEqual(voucher_list_i[:-3], print_time)
            elif i == 9:
                self.assertEqual(voucher_list_i[-1], '2')
                self.assertEqual(voucher_list_i[0], '0')
            elif i == 11:
                self.assertEqual(voucher_list_i[-4:], '1 GB')
            elif i == 12:
                self.assertEqual(voucher_list_i, '256 Kbps')
            elif i == 13:
                self.assertEqual(voucher_list_i, '5 Mbps')
            elif i == 14:
                self.assertEqual(voucher_list_i, 'Not Activated')


    def test06_voucher_multiple_print(self):
        """验证打印出多个voucher,voucher list中的信息与package信息是否一致"""
        time.sleep(5)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(config_voucher)
        time.sleep(5)
        self.operate.click_elem(config_voucher_print)
        self.operate.click_elem(config_voucher_multiple)
        self.operate.elem_send_keys(config_voucher_multiple_quantity, '10')
        self.operate.click_elem(config_voucher_key_print_multiple)
        print_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        print print_time
        time.sleep(5)
        handles = self.driver.window_handles
        self.driver.switch_to_window(handles[-1])
        self.driver.close()
        self.driver.switch_to_window(handles[0])
        time.sleep(5)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(config_voucher)
        self.operate.click_elem(config_voucher_list_refresh)
        time.sleep(2)
        l = len(self.operate.find_elems(config_voucher_list_time.format(print_time)))
        time.sleep(2)
        for i in range(1, 15):
            voucher_list_i = self.operate.find_elem(config_voucher_list_tr.format(i)).text
            print voucher_list_i
            if i == 4:
                self.assertEqual(voucher_list_i, package_name_input_edit)
            elif i == 5:
                self.assertEqual(voucher_list_i[0], package_price_input_edit)
            elif i == 6:
                self.assertEqual(voucher_list_i, '1 Day')
            elif i == 7:
                print voucher_list_i[:-3]
                self.assertEqual(voucher_list_i[:-3][:-2], print_time[:-2])
            elif i == 9:
                self.assertEqual(voucher_list_i[-1], '2')
                self.assertEqual(voucher_list_i[0], '0')
            elif i == 11:
                self.assertEqual(voucher_list_i[-4:], '1 GB')
            elif i == 12:
                self.assertEqual(voucher_list_i, '256 Kbps')
            elif i == 13:
                self.assertEqual(voucher_list_i, '5 Mbps')
            elif i == 14:
                self.assertEqual(voucher_list_i, 'Not Activated')
        self.assertEqual(l, 10)

    def test07_config_voucher_search(self):
        """验证可通过voucher code搜索到voucher"""
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(config_voucher)
        time.sleep(5)
        voucher_code = self.operate.find_elem(config_voucher_code).text
        self.operate.elem_send_keys(config_voucher_search, voucher_code)
        self.operate.elem_send_keys(config_voucher_search, Keys.ENTER)
        l = len(self.operate.find_elems(config_voucher_tr_len))
        t = self.operate.find_elem(config_voucher_code).text
        self.assertEqual(l, 1)
        self.assertEqual(t, voucher_code)

    def test08_config_ppsk_add(self):
        """验证ppsk账号可添加,可同步"""
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(configuration_basic_xpath)
        time.sleep(5)
        self.operate.click_elem(configuration_basic_xpath)
        time.sleep(5)
        self.operate.click_elem(add_group_xpath)
        self.operate.elem_send_keys(add_SSID_name, add_SSID_ssid_name)
        self.operate.click_elem(config_basic_ppsk)
        self.operate.click_elem(add_SSID_save_ssid)
        # 调试代码
        # 配置安全密码
        # self.operate.click_elem(add_SSID_security)
        # self.operate.elem_send_keys(add_SSID_security_web_password, add_SSID_web_password)
        # self.operate.elem_send_keys(add_SSID_security_telnet_password, add_SSID_telnet_password)
        # 调试代码
        # 保存
        self.operate.click_elem(add_SSID_save)
        time.sleep(5)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(config_ppsk)
        time.sleep(5)
        self.operate.click_elem(config_ppsk_add_account)
        time.sleep(5)
        self.operate.click_elem(config_ppsk_alert_add_account)
        self.operate.elem_send_keys(config_ppsk_alert_ppsk_name, ppsk_name_input)
        self.operate.click_elem(ppsk_key_OK)
        print_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        print print_time
        time.sleep(10)
        self.operate.elem_send_keys(config_ppsk_bind_mac, ppsk_bind_mac_input)
        self.operate.click_elem(config_ppsk_bind_button)
        self.operate.click_elem(key_OK)
        time.sleep(10)
        ppsk_name = self.operate.find_elem(config_ppsk_list_tr_name).text
        ppsk_time = self.operate.find_elem(config_ppsk_list_tr_time).text
        ppsk_mac = self.operate.find_elem(config_ppsk_list_tr_mac).text
        self.assertEqual(ppsk_name, ppsk_name_input)
        self.assertIn(print_time, ppsk_time)
        self.assertEqual(ppsk_mac, ppsk_bind_mac_input)
        self.operate.click_elem(config_ppsk_list_action_check)
        time.sleep(50)
        try:
            ppsk_synced = self.operate.find_elem(config_ppsk_SYNCED).text
        finally:
            self.operate.click_elem(config_ppsk_list_check_close)
            self.assertEqual(ppsk_synced, 'SYNCED')







if __name__ == '__main__':
    unittest.main()
