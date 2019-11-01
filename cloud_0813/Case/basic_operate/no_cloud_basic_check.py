# coding:utf-8
"""
@author: Tracy
@mail: wanghongyu@ruijie.com.cn
@date: 2019.06.17
"""
from Common.com_function import *
from Data.basic_data import *
from Page.basic_page import *
from Page.device_page import *
from Common.driver import Pyse
from Common.login import Login
from Common.string_escape import string_escape
from Common.add_group import AddGroup
from Page.config_page import *
from Data.device_data import *
import unittest
import re

# 升级前的设备版本
global firmware_ap_before_upgrade, firmware_sw_now, firmware_eg_now
# 升级后的设备版本
global firmware_ap, firmware_sw, firmware_eg



class BasicCheck(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Pyse("chrome")
        Login(cls.driver, user_cloud_local, password_cloud_local, login_url_local).login()
        cls.operate = ComFunction(cls.driver)
        cls.group_name = AddGroup(cls.driver, sub_group=True, device_sn={
            'sw': add_device_alert_input_sn_switch,
            'ap': add_device_alert_input_sn,
            'eg': add_device_alert_input_sn_gateway
        }).add_group()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test03_ssid_hidden(self):
        """验证配置SSID隐藏可以成功下发/SSID不加密"""
        time.sleep(1)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(configuration_basic_xpath)
        time.sleep(5)
        # 配置SSID隐藏
        self.operate.click_elem(config_ssid_edit)
        self.operate.click_elem(config_ssid_hidden)
        self.operate.click_elem(config_ssid_hidden_yes)
        self.operate.click_elem(add_SSID_save_ssid)
        # 保存
        self.operate.click_elem(add_SSID_save)
        time.sleep(10)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        time.sleep(2)
        try:
            self.operate.find_elem(add_device_online_ap, By.XPATH, 360)
            while True:
                sync_state = self.operate.find_elem(add_device_state).text
                if sync_state == 'Sync Failed' or sync_state == 'Synced':
                    break
        except Exception as e:
            print (e)
            print (u"6minAP上线或同步配置失败")
        else:
            self.operate.click_elem(device_select)
            self.operate.click_elem(device_more)
            self.operate.click_elem(device_diagnosis)
            js1 = 'return $("#cli_result").val();'
            n = 1
            while n < 4:
                self.operate.click_elem(device_running_config)
                time.sleep(6)
                text_running = self.driver.execute_script(js1)
                time.sleep(6)
                with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                    f.write(text_running)
                    f.seek(0, 0)
                    text = f.read()
                if re.search('!', text) is None:
                    print (u'AP running 命令行第' + str(n) + u'次返回失败')
                    # time.sleep(6)
                    n += 1
                else:
                    print (u"AP running 命令行返回成功")
                    break
            self.operate.click_elem(device_diagnosis_close)
            t = re.search('dot11 wlan 1\n no broadcast-ssid', text)
            self.assertIsNotNone(t)
            t = re.search('wlansec 1\n!', text)
            self.assertIsNotNone(t)
            self.assertEqual(sync_state, 'Synced', u'AP有某项配置同步失败')

    def test04_ssid_nat_common(self):
        """验证NAT地址池可成功下发"""
        time.sleep(1)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(configuration_basic_xpath)
        time.sleep(5)
        self.operate.click_elem(config_ssid_edit)
        self.operate.click_elem(config_ssid_forward)
        self.operate.click_elem(config_ssid_forward_nat)
        self.operate.click_elem(add_SSID_save_ssid)
        # 保存
        self.operate.click_elem(add_SSID_save)
        time.sleep(10)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        time.sleep(2)
        try:
            self.operate.find_elem(add_device_online_ap, By.XPATH, 360)
            while True:
                sync_state = self.operate.find_elem(add_device_state).text
                if sync_state == 'Sync Failed' or sync_state == 'Synced':
                    break
        except Exception as e:
            print (e)
            print (u"6minAP上线或同步配置失败")
        else:
            self.operate.click_elem(device_select)
            self.operate.click_elem(device_more)
            self.operate.click_elem(device_diagnosis)
            js1 = 'return $("#cli_result").val();'
            n = 1
            while n < 4:
                self.operate.click_elem(device_running_config)
                time.sleep(6)
                text_running = self.driver.execute_script(js1)
                time.sleep(6)
                with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                    f.write(text_running)
                    f.seek(0, 0)
                    text = f.read()
                if re.search('!', text) is None:
                    print (u'AP running 命令行第' + str(n) + u'次返回失败')
                    # time.sleep(6)
                    n += 1
                else:
                    print (u"AP running 命令行返回成功")
                    break
            self.operate.click_elem(device_diagnosis_close)
            t = re.search('ip dhcp pool macc_sta_pool' + '[\S\s]*'
                                                         'ip nat inside source list 2 interface BVI 1', text)
            self.assertIsNotNone(t)

    def test05_ssid_nat_custom(self):
        """验证自定义的nat地址池可成功下发"""
        time.sleep(1)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(configuration_basic_xpath)
        time.sleep(5)
        self.operate.click_elem(config_ssid_edit)
        self.operate.click_elem(config_ssid_forward)
        self.operate.click_elem(config_ssid_forward_nat)
        self.operate.click_elem(config_ssid_forward_nat_pool_config)
        self.operate.click_elem(config_ssid_forward_nat_pool_config_select)
        self.operate.click_elem(config_ssid_forward_nat_pool_config_click)
        self.operate.elem_clear_send_keys(config_ssid_forward_nat_pool_config_network, nat_pool_network_input)
        self.operate.elem_clear_send_keys(config_ssid_forward_nat_pool_config_submask, nat_pool_submask_input)
        self.operate.click_elem(key_save)
        time.sleep(5)
        self.operate.click_elem(add_SSID_save_ssid)
        # 保存
        self.operate.click_elem(add_SSID_save)
        time.sleep(10)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        time.sleep(2)
        try:
            self.operate.find_elem(add_device_online_ap, By.XPATH, 360)
            while True:
                sync_state = self.operate.find_elem(add_device_state).text
                if sync_state == 'Sync Failed' or sync_state == 'Synced':
                    break
        except Exception as e:
            print (e)
            print (u"6minAP上线或同步配置失败")
        else:
            self.operate.click_elem(device_select)
            self.operate.click_elem(device_more)
            self.operate.click_elem(device_diagnosis)
            js1 = 'return $("#cli_result").val();'
            n = 1
            while n < 4:
                self.operate.click_elem(device_running_config)
                time.sleep(6)
                text_running = self.driver.execute_script(js1)
                time.sleep(6)
                with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                    f.write(text_running)
                    f.seek(0, 0)
                    text = f.read()
                if re.search('!', text) is None:
                    print (u'AP running 命令行第' + str(n) + u'次返回失败')
                    # time.sleep(6)
                    n += 1
                else:
                    print (u"AP running 命令行返回成功")
                    break
            self.operate.click_elem(device_diagnosis_close)

            t = re.search('ip dhcp pool macc_sta_pool\n network ' + nat_pool_network_input + ' ' +
                          nat_pool_submask_input, text)
            if t is None:
                print text
            self.assertIsNotNone(t)

    def test07_ssid_radio_Max_clients(self):
        """验证radio 支持的最大客户端数下发成功"""
        time.sleep(1)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(configuration_basic_xpath)
        time.sleep(5)
        self.operate.elem_clear_send_keys(config_ssid_radio_1_max_client, '1')
        self.operate.elem_clear_send_keys(config_ssid_radio_2_max_client, '255')
        self.operate.click_elem(add_SSID_save)
        time.sleep(10)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        time.sleep(2)
        try:
            self.operate.find_elem(add_device_online_ap, By.XPATH, 360)
            while True:
                sync_state = self.operate.find_elem(add_device_state).text
                if sync_state == 'Sync Failed' or sync_state == 'Synced':
                    break
        except Exception as e:
            print (e)
            print (u"6minAP上线或同步配置失败")
        else:
            self.operate.click_elem(device_select)
            self.operate.click_elem(device_more)
            self.operate.click_elem(device_diagnosis)
            js1 = 'return $("#cli_result").val();'
            n = 1
            while n < 4:
                self.operate.click_elem(device_running_config)
                time.sleep(6)
                text_running = self.driver.execute_script(js1)
                time.sleep(6)
                with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                    f.write(text_running)
                    f.seek(0, 0)
                    text = f.read()
                if re.search('!', text) is None:
                    print (u'AP running 命令行第' + str(n) + u'次返回失败')
                    # time.sleep(6)
                    n += 1
                else:
                    print (u"AP running 命令行返回成功")
                    break
            self.operate.click_elem(device_diagnosis_close)
            t_radio_1_client = re.search('interface Dot11radio 1/0' + '[^!]*' + 'sta-limit 1' + '[\S\s]*', text)

            t_radio_2_client = re.search('interface Dot11radio 2/0' + '[^!]*' + 'sta-limit 111', text)
            if t_radio_1_client is None or t_radio_2_client is None:
                print text
            self.assertIsNotNone(t_radio_1_client)
            self.assertIsNotNone(t_radio_2_client)

    def test08_ssid_bridge(self):
        """验证关闭radio 2,打开radio 1"""
        time.sleep(1)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(configuration_basic_xpath)
        time.sleep(5)
        self.operate.click_elem(config_ssid_radio_2)
        self.operate.click_elem(add_SSID_save)
        time.sleep(10)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        time.sleep(2)
        try:
            self.operate.find_elem(add_device_online_ap, By.XPATH, 360)
            while True:
                sync_state = self.operate.find_elem(add_device_state).text
                if sync_state == 'Sync Failed' or sync_state == 'Synced':
                    break
        except Exception as e:
            print (e)
            print (u"6minAP上线或同步配置失败")
        else:
            self.operate.click_elem(device_select)
            self.operate.click_elem(device_more)
            self.operate.click_elem(device_diagnosis)
            js1 = 'return $("#cli_result").val();'
            n = 1
            while n < 4:
                self.operate.click_elem(device_running_config)
                time.sleep(6)
                text_running = self.driver.execute_script(js1)
                time.sleep(6)
                with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                    f.write(text_running)
                    f.seek(0, 0)
                    text = f.read()
                if re.search('!', text) is None:
                    print (u'AP running 命令行第' + str(n) + u'次返回失败')
                    # time.sleep(6)
                    n += 1
                else:
                    print (u"AP running 命令行返回成功")
                    break
            self.operate.click_elem(device_diagnosis_close)
            t_radio_1 = re.search('interface Dot11radio 1/0' + '[^!]*' + 'shutdown' + '[\S\s]*', text)

            t_radio_2 = re.search('interface Dot11radio 2/0' + '[^!]*' + 'shutdown', text)
            self.assertIsNone(t_radio_1)
            self.assertIsNotNone(t_radio_2)

    def test12_ssid_wap_wpa2_psk(self):
        """验证SSID加密方式为wpa/wpa2_psk"""
        time.sleep(1)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(configuration_basic_xpath)
        time.sleep(5)
        self.operate.click_elem(config_ssid_edit)
        self.operate.click_elem(config_ssid_encryption)
        self.operate.click_elem(config_ssid_encryption_wpa_wpa2_psk)
        time.sleep(1)
        self.operate.elem_clear_send_keys(config_ssid_encryption_wpa_psk_password,
                                          config_ssid_encryp_password_wpa2_input)
        self.operate.click_elem(add_SSID_save_ssid)
        # 保存
        self.operate.click_elem(add_SSID_save)
        time.sleep(10)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        time.sleep(2)
        try:
            self.operate.find_elem(add_device_online_ap, By.XPATH, 360)
            while True:
                sync_state = self.operate.find_elem(add_device_state).text
                if sync_state == 'Sync Failed' or sync_state == 'Synced':
                    break
        except Exception as e:
            print (e)
            print (u"6minAP上线或同步配置失败")
        else:
            self.operate.click_elem(device_select)
            self.operate.click_elem(device_more)
            self.operate.click_elem(device_diagnosis)
            js1 = 'return $("#cli_result").val();'
            n = 1
            while n < 4:
                self.operate.click_elem(device_running_config)
                time.sleep(6)
                text_running = self.driver.execute_script(js1)
                time.sleep(6)
                with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                    f.write(text_running)
                    f.seek(0, 0)
                    text = f.read()
                if re.search('!', text) is None:
                    print (u'AP running 命令行第' + str(n) + u'次返回失败')
                    # time.sleep(6)
                    n += 1
                else:
                    print (u"AP running 命令行返回成功")
                    break
            self.operate.click_elem(device_diagnosis_close)
            t = re.search(
                'wlansec 1\n security rsn enable' + '[\S\s]*' + 'security rsn akm psk set-key ascii '
                + config_ssid_encryp_password_wpa2_input + '[\S\s]*' + 'security wpa enable'
                + '[\S\s]*' + 'security wpa akm psk set-key ascii '
                + config_ssid_encryp_password_wpa2_input
                , text)
            self.assertIsNotNone(t)

    def test13_ssid_ppsk(self):
        """验证SSID加密方式为PPSK"""
        time.sleep(1)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(configuration_basic_xpath)
        time.sleep(5)
        self.operate.click_elem(config_ssid_edit)
        self.operate.click_elem(config_ssid_encryption)
        self.operate.click_elem(config_ssid_encryption_ppsk)
        time.sleep(3)
        self.operate.click_elem(add_SSID_save_ssid)
        # 保存
        self.operate.click_elem(add_SSID_save)
        time.sleep(10)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        time.sleep(2)
        try:
            self.operate.find_elem(add_device_online_ap, By.XPATH, 360)
            while True:
                sync_state = self.operate.find_elem(add_device_state).text
                if sync_state == 'Sync Failed' or sync_state == 'Synced':
                    break
        except Exception as e:
            print (e)
            print (u"6minAP上线或同步配置失败")
        else:
            self.operate.click_elem(device_select)
            self.operate.click_elem(device_more)
            self.operate.click_elem(device_diagnosis)
            js1 = 'return $("#cli_result").val();'
            n = 1
            while n < 4:
                self.operate.click_elem(device_running_config)
                time.sleep(6)
                text_running = self.driver.execute_script(js1)
                time.sleep(6)
                with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                    f.write(text_running)
                    f.seek(0, 0)
                    text = f.read()
                if re.search('!', text) is None:
                    print (u'AP running 命令行第' + str(n) + u'次返回失败')
                    # time.sleep(6)
                    n += 1
                else:
                    print (u"AP running 命令行返回成功")
                    break
            self.operate.click_elem(device_diagnosis_close)
            t = re.search('security sta-psk enable', text)
            self.assertIsNotNone(t)

    def test14_ssid_speed_limit(self):
        """验证基于客户端限速/基于SSID限速命令下发成功"""
        time.sleep(1)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(configuration_basic_xpath)
        time.sleep(5)
        self.operate.click_elem(config_ssid_edit)
        self.operate.click_elem(config_ssid_rate_client)
        self.operate.elem_clear_send_keys(config_ssid_rate_client_upRate, '100')
        self.operate.elem_clear_send_keys(config_ssid_rate_client_downRate, '100')
        self.operate.click_elem(config_ssid_rate_ssid)
        self.operate.elem_clear_send_keys(config_ssid_rate_ssid_wlan_upRate, '100')
        self.operate.elem_clear_send_keys(config_ssid_rate_ssid_wlan_downRate, '100')
        time.sleep(3)
        self.operate.click_elem(add_SSID_save_ssid)
        # 保存
        self.operate.click_elem(add_SSID_save)
        time.sleep(10)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        time.sleep(2)
        try:
            self.operate.find_elem(add_device_online_ap, By.XPATH, 360)
            while True:
                sync_state = self.operate.find_elem(add_device_state).text
                if sync_state == 'Sync Failed' or sync_state == 'Synced':
                    break
        except Exception as e:
            print (e)
            print (u"6minAP上线或同步配置失败")
        else:
            self.operate.click_elem(device_select)
            self.operate.click_elem(device_more)
            self.operate.click_elem(device_diagnosis)
            js1 = 'return $("#cli_result").val();'
            n = 1
            while n < 4:
                self.operate.click_elem(device_running_config)
                time.sleep(6)
                text_running = self.driver.execute_script(js1)
                time.sleep(6)
                with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                    f.write(text_running)
                    f.seek(0, 0)
                    text = f.read()
                if re.search('!', text) is None:
                    print (u'AP running 命令行第' + str(n) + u'次返回失败')
                    # time.sleep(6)
                    n += 1
                else:
                    print (u"AP running 命令行返回成功")
                    break
            self.operate.click_elem(device_diagnosis_close)
            t = re.search(
                'wlan-qos wlan-based 1 total-user-limit up-streams average-data-rate 100 burst-data-rate 100' +
                '[^!]*' +
                'wlan-qos wlan-based 1 total-user-limit down-streams average-data-rate 100 burst-data-rate 100' +
                '[^!]*' +
                'wlan-qos wlan-based 1 per-user-limit down-streams average-data-rate 100 burst-data-rate 100'
                , text)
            self.assertIsNotNone(t)




    def test16_one_click(self):
        """验证可成功下发一键认证配置"""
        time.sleep(1)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(configuration_basic_xpath)
        time.sleep(5)
        self.operate.click_elem(config_ssid_edit)
        self.operate.click_elem(add_SSID_enable_auth)
        time.sleep(1)
        self.operate.click_elem(add_SSID_one_click_login)
        self.operate.click_elem(add_SSID_save_ssid)
        time.sleep(5)
        # 保存
        self.operate.click_elem(add_SSID_save)
        time.sleep(10)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        time.sleep(2)
        try:
            self.operate.find_elem(add_device_online_ap, By.XPATH, 360)
            while True:
                sync_state = self.operate.find_elem(add_device_state).text
                if sync_state == 'Sync Failed' or sync_state == 'Synced':
                    break
        except Exception as e:
            print (e)
            print (u"6minAP上线或同步配置失败")
        else:
            self.operate.click_elem(device_select)
            self.operate.click_elem(device_more)
            self.operate.click_elem(device_diagnosis)
            js1 = 'return $("#cli_result").val();'
            n = 1
            while n < 4:
                self.operate.click_elem(device_running_config)
                time.sleep(6)
                text_running = self.driver.execute_script(js1)
                time.sleep(6)
                with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                    f.write(text_running)
                    f.seek(0, 0)
                    text = f.read()
                if re.search('!', text) is None:
                    print (u'AP running 命令行第' + str(n) + u'次返回失败')
                    # time.sleep(6)
                    n += 1
                else:
                    print (u"AP running 命令行返回成功")
                    break
            self.operate.click_elem(device_diagnosis_close)
        # 验证内置认证
        t = re.search('wlansec 1' + '[\S\s]*' + 'web-auth portal wifidog_1', text)
        self.assertIsNotNone(t)

    def test17_SSID_add(self):
        """验证可成功下发多个SSID"""
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(configuration_basic_xpath)
        time.sleep(15)
        for i in range(2, 9):
            self.operate.click_elem(add_group_xpath)
            self.operate.elem_send_keys(add_SSID_name, str(i) + '_auto')
            self.operate.click_elem(add_SSID_save_ssid)
            time.sleep(2)
        # 保存
        self.operate.click_elem(add_SSID_save)
        time.sleep(15)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        time.sleep(2)
        try:
            self.operate.find_elem(add_device_online_ap, By.XPATH, 360)
            while True:
                sync_state = self.operate.find_elem(add_device_state).text
                if sync_state == 'Sync Failed' or sync_state == 'Synced':
                    break
        except Exception as e:
            print (e)
            print (u"6minAP上线或同步配置失败")
        else:
            self.operate.click_elem(device_select)
            self.operate.click_elem(device_more)
            self.operate.click_elem(device_diagnosis)
            self.operate.click_elem(device_diagnosis_wlan)
            js1 = 'return $("#cli_result").val();'
            n = 1
            while n < 4:
                self.operate.click_elem(device_diagnosis_wlan_mbssid)
                time.sleep(6)
                text_running = self.driver.execute_script(js1)
                time.sleep(6)
                with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                    f.write(text_running)
                    f.seek(0, 0)
                    text = f.read()
                if re.search('MBSSID', text) is None:
                    print (u'AP MBSSID 命令行第' + str(n) + u'次返回失败')
                    # time.sleep(6)
                    n += 1
                else:
                    print (u"AP MBSSID 命令行返回成功")
                    break
            self.operate.click_elem(device_diagnosis_close)
            for i in range(2, 9):
                t = re.search('wlan id: ' + str(i) + '[\S\s]*' + str(i) + '_auto', text)
                self.assertIsNotNone(t)

    def test18_ssid_delete(self):
        """验证SSID可成功删除"""
        time.sleep(1)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(configuration_basic_xpath)
        for i in range(8):
            self.operate.click_elem(config_ssid_delete)
            self.operate.click_elem(key_OK)
            time.sleep(1)
        # 保存
        self.operate.click_elem(add_SSID_save)
        time.sleep(10)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        time.sleep(2)
        try:
            self.operate.find_elem(add_device_online_ap, By.XPATH, 360)
            while True:
                sync_state = self.operate.find_elem(add_device_state).text
                if sync_state == 'Sync Failed' or sync_state == 'Synced':
                    break
        except Exception as e:
            print (e)
            print (u"6minAP上线或同步配置失败")
        else:
            self.operate.click_elem(device_select)
            self.operate.click_elem(device_more)
            self.operate.click_elem(device_diagnosis)
            self.operate.click_elem(device_diagnosis_wlan)
            js1 = 'return $("#cli_result").val();'
            n = 1
            while n < 4:
                self.operate.click_elem(device_diagnosis_wlan_mbssid)
                time.sleep(6)
                text_running = self.driver.execute_script(js1)
                time.sleep(6)
                with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                    f.write(text_running)
                    f.seek(0, 0)
                    text = f.read()
                if re.search('MBSSID', text) is None:
                    print (u'AP MBSSID 命令行第' + str(n) + u'次返回失败')
                    # time.sleep(6)
                    n += 1
                else:
                    print (u"AP MBSSID 命令行返回成功")
                    break
            self.operate.click_elem(device_diagnosis_close)
            t = re.search('MBSSID:\nNone', text)
            self.assertIsNotNone(t)

    def test19_group_delete(self):
        """验证分组可删除"""
        time.sleep(1)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(groups_page_xpath)
        time.sleep(5)
        js = "var q=document.getElementById('svgBlockDiv').scrollTop=100000"
        self.driver.execute_script(js)
        self.operate.click_elem(select_group_xpath.format(self.group_name))
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
            self.operate.click_elem(select_group_xpath.format('sub_' + self.group_name))
            self.operate.click_elem(config_group_delete)
            self.operate.click_elem(key_OK)
            time.sleep(5)
            self.operate.click_elem(select_group_xpath.format(self.group_name))
            self.operate.click_elem(config_group_delete)
            self.operate.click_elem(key_OK)
            time.sleep(5)
            try:
                self.operate.find_elem(select_group_xpath.format(self.group_name), by=By.XPATH, wait_times=30)
            except:
                flag = 1
            else:
                flag = 0
            finally:
                self.assertEqual(flag, 1)


if __name__ == '__main__':
    unittest.main()
