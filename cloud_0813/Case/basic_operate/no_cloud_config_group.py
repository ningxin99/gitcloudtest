# coding:utf-8
"""
@author: Tracy
@mail: wanghongyu@ruijie.com.cn
@date: 2019.07.24
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
from Common.uuid import get_group_name
from selenium.webdriver.common.keys import Keys




class CloudConfigGroup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Pyse("chrome")
        Login(cls.driver, user_cloud_local, password_cloud_local, login_url_local).login()
        cls.operate = ComFunction(cls.driver)
        cls.group_name = get_group_name()
        cls.subgroup_name = 'sub_' + cls.group_name
        cls.group_name_edit = 'edit_' + cls.group_name
        # cls.group_name = 'test_072901'
        # cls.subgroup_name = 'sub_test_072901'
        # cls.group_name_edit = 'edit_ZO7'
        cls.operate.click_elem(configuration_page_xpath)
        cls.operate.click_elem(groups_page_xpath)
        time.sleep(10)
        cls.operate.click_elem(add_groups_xpath)
        cls.operate.elem_send_keys(add_groups_input_name_xpath, cls.group_name)
        cls.operate.click_elem(add_groups_next_page_xpath)
        cls.operate.elem_clear_send_keys(add_groups_add_wifi_name_default, add_SSID_ssid_name_default)
        cls.operate.click_elem(add_groups_apply_xpath)
        time.sleep(5)
        cls.operate.click_elem(add_device_close_xpath)
        time.sleep(2)
        js = "var q=document.getElementById('svgBlockDiv').scrollTop=100000"
        cls.driver.execute_script(js)



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    # def test00(self):
    #     # 调试代码
    #     time.sleep(20)
    #     self.operate.click_elem(login_close_tips_xpath)
    #     self.operate.click_elem(configuration_page_xpath)
    #     self.operate.click_elem(groups_page_xpath)
    #     time.sleep(10)
    #     js = "var q=document.getElementById('svgBlockDiv').scrollTop=100000"
    #     self.driver.execute_script(js)
    #     time.sleep(5)





    def test02_subgroup_add(self):
        """验证是否能添加子分组"""
        print (self.group_name)
        time.sleep(5)
        self.operate.click_elem(select_group_xpath.format(self.group_name))
        self.operate.click_elem(config_group_subgroup)
        self.operate.elem_send_keys(config_group_subgroup_add, self.subgroup_name)
        self.operate.click_elem(config_group_subgroup_add_save)
        self.operate.click_elem(config_group_sugroup_save)
        self.operate.click_elem(add_device_close_xpath)
        time.sleep(5)
        self.operate.click_elem(config_group_subgroup_unfold)
        # self.operate.click_elem(config_group_subgroup_open.format(self.group_name))
        time.sleep(2)
        try:
            self.operate.find_elem(select_group_xpath.format(self.subgroup_name))
        except Exception as e:
            self.assertIsNotNone(None)

    def test03_subgroup_fold(self):
        """验证子分组可以展开/收起"""
        time.sleep(5)
        self.operate.click_elem(config_group_subgroup_fold)
        time.sleep(1)
        try:
            self.operate.find_elem(select_group_xpath.format(self.subgroup_name))
        except Exception as e:
            self.assertIsNone(None)
        finally:
            self.operate.click_elem(config_group_subgroup_unfold)
            try:
                self.operate.find_elem(select_group_xpath.format(self.subgroup_name))
            except Exception as e:
                self.assertIsNotNone(None)

    def test04_group_search(self):
        """验证可搜索到指定分组"""
        time.sleep(5)
        self.operate.click_elem(config_group_search)
        self.operate.elem_send_keys(config_group_search_input, self.group_name)
        self.operate.elem_send_keys(config_group_search_input, Keys.ENTER)
        time.sleep(1)
        try:
            self.operate.find_elem(config_group_search_ele.format(self.group_name))
        except Exception as e:
            self.assertIsNotNone(None)



    def test05_group_device_add(self):
        """验证分组是否可添加设备成功"""
        self.operate.click_elem(select_group_xpath.format(self.group_name))
        self.operate.click_elem(config_group_add_device)
        self.operate.elem_send_keys(add_device_input_sn_xpath, add_device_alert_input_sn)
        self.operate.click_elem(add_group_device_sw)
        self.operate.elem_send_keys(add_device_input_sn_sw_xpath, add_device_alert_input_sn_switch)
        self.operate.click_elem(add_group_device_eg)
        self.operate.elem_send_keys(add_device_input_sn_eg_xpath, add_device_alert_input_sn_gateway)
        self.operate.elem_send_keys(add_device_input_password_eg_xpath, add_device_alert_input_password)
        self.operate.click_elem(add_group_device_ap)
        self.operate.click_elem(add_device_apply_xpath)
        time.sleep(5)
        self.operate.click_elem(add_device_close_xpath)
        time.sleep(2)
        device_num = self.operate.find_elem(config_group_device_num.format(self.group_name)).text
        self.assertEqual(device_num[-1], '3')

    def test06_group_edit(self):
        """验证分组信息可编辑"""
        self.operate.click_elem(select_group_xpath.format(self.group_name))
        self.operate.click_elem(config_group_edit)
        self.operate.elem_clear_send_keys(config_group_edit_name, self.group_name_edit)
        self.operate.click_elem(config_group_edit_time_zone)
        self.operate.elem_clear_send_keys(config_group_edit_location, 'fuzhou')
        self.operate.click_elem(config_group_edit_save)
        time.sleep(5)
        try:
            self.operate.find_elem(select_group_xpath.format(self.group_name_edit))
        except Exception as e:
            print e
            self.assertIsNotNone(None)

    def test07_group_config(self):
        """验证可进入分组配置页面"""
        self.operate.click_elem(select_group_xpath.format(self.group_name_edit))
        self.operate.click_elem(config_group_config)
        time.sleep(5)
        try:
            self.operate.find_elem(config_group_more_config_ssid_list)
        except Exception as e:
            print e
            self.assertIsNotNone(None)


    def test08_group_config_delete(self):
        """验证分组可删除"""
        time.sleep(1)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(groups_page_xpath)
        time.sleep(5)
        js = "var q=document.getElementById('svgBlockDiv').scrollTop=100000"
        self.driver.execute_script(js)
        self.operate.click_elem(select_group_xpath.format(self.subgroup_name))
        self.operate.click_elem(config_group_delete)
        self.operate.click_elem(key_OK)
        time.sleep(5)
        self.operate.click_elem(select_group_xpath.format(self.group_name_edit))
        self.operate.click_elem(config_group_config)
        time.sleep(5)
        # 删除AP
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        self.operate.click_elem(add_device_access_point)
        time.sleep(15)
        self.operate.click_elem(device_select)
        self.operate.click_elem(device_more)
        self.operate.click_elem(device_delete)
        self.operate.click_elem(key_OK)
        time.sleep(5)
        # 删除交换机
        self.operate.click_elem(add_device_switch)
        self.operate.click_elem(add_device_switch)
        time.sleep(15)
        self.operate.click_elem(sw_select)
        self.operate.click_elem(sw_more)
        self.operate.click_elem(device_delete)
        self.operate.click_elem(key_OK)
        time.sleep(5)
        # 删除EG
        self.operate.click_elem(add_device_gateway)
        self.operate.click_elem(add_device_gateway)
        time.sleep(15)
        try:
            self.operate.click_elem(eg_select)
            self.operate.click_elem(eg_more)
            self.operate.click_elem(eg_delete)
            self.operate.click_elem(key_OK)
            time.sleep(5)
        except Exception as e:
            self.operate.click_elem(eg_unauth_delete)
            self.operate.click_elem(key_OK)
            time.sleep(5)
        finally:
            self.operate.click_elem(configuration_page_xpath)
            self.operate.click_elem(groups_page_xpath)
            time.sleep(10)
            js = "var q=document.getElementById('svgBlockDiv').scrollTop=100000"
            self.driver.execute_script(js)
            time.sleep(1)
            self.operate.click_elem(select_group_xpath.format(self.group_name_edit))
            self.operate.click_elem(config_group_delete)
            self.operate.click_elem(key_OK)
            time.sleep(5)
            try:
                self.operate.find_elem(select_group_xpath.format(self.group_name_edit), by=By.XPATH, wait_times=30)
            except:
                flag = 1
            else:
                flag = 0
            finally:
                self.assertEqual(flag, 1)






if __name__ == '__main__':
    unittest.main()










