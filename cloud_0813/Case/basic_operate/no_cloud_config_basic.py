# coding:utf-8
"""
@author: Tracy
@mail: wanghongyu@ruijie.com.cn
@date: 2019.06.17
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
from Page.config_page import *
from Data.device_data import *
from Common.uuid import get_group_name


class ConfigBasic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Pyse("chrome")
        Login(cls.driver, user_cloud_local, password_cloud_local, login_url_local).login()
        cls.operate = ComFunction(cls.driver)
        cls.group_name = AddGroup(cls.driver, device_sn={'ap': add_device_alert_input_sn}).add_group()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # def test00(self):
    #     # 调试代码
    #     self.operate.click_elem(configuration_page_xpath)  # 没有等60s
    #     self.operate.click_elem(configuration_basic_xpath)
    #     # 调试代码

    def test02_ssid_default_not_hidden(self):
        """验证SSID默认不隐藏"""
        print (self.group_name)
        time.sleep(1)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        self.operate.click_elem(add_device_access_point)
        time.sleep(2)
        try:
            self.operate.find_elem(add_device_online_ap, By.XPATH, 360)
            while True:
                sync_state = self.operate.find_elem(add_device_state).text
                if sync_state == 'Sync Failed' or sync_state == 'Synchronized':
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
                time.sleep(11)
                text_running = self.driver.execute_script(js1)
                time.sleep(11)
                with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                    f.write(text_running)
                    f.seek(0, 0)
                    text = f.read()
                if re.search('!', text) is None:
                    print (u'AP running 命令行第' + str(n) + u'次返回失败')
                    # time.sleep(11)
                    n += 1
                else:
                    print (u"AP running 命令行返回成功")
                    break
            self.operate.click_elem(device_diagnosis_close)
        t = re.search('dot11 wlan 1\n no broadcast-ssid', text)
        self.assertIsNone(t)
        self.assertEqual(sync_state, 'Synchronized', u'AP有某项配置同步失败')
        


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
                if sync_state == 'Sync Failed' or sync_state == 'Synchronized':
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
                time.sleep(11)
                text_running = self.driver.execute_script(js1)
                time.sleep(11)
                with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                    f.write(text_running)
                    f.seek(0, 0)
                    text = f.read()
                if re.search('!', text) is None:
                    print (u'AP running 命令行第' + str(n) + u'次返回失败')
                    # time.sleep(11)
                    n += 1
                else:
                    print (u"AP running 命令行返回成功")
                    break
            self.operate.click_elem(device_diagnosis_close)
            t = re.search('dot11 wlan 1\n no broadcast-ssid', text)
            self.assertIsNotNone(t)
            t = re.search('wlansec 1\n!', text)
            self.assertIsNotNone(t)
            

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
                if sync_state == 'Sync Failed' or sync_state == 'Synchronized':
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
                time.sleep(11)
                text_running = self.driver.execute_script(js1)
                time.sleep(11)
                with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                    f.write(text_running)
                    f.seek(0, 0)
                    text = f.read()
                if re.search('!', text) is None:
                    print (u'AP running 命令行第' + str(n) + u'次返回失败')
                    # time.sleep(11)
                    n += 1
                else:
                    print (u"AP running 命令行返回成功")
                    break
            self.operate.click_elem(device_diagnosis_close)
            t = re.search('ip dhcp pool macc_sta_pool'+'[\S\s]*'
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
                if sync_state == 'Sync Failed' or sync_state == 'Synchronized':
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
                time.sleep(11)
                text_running = self.driver.execute_script(js1)
                time.sleep(11)
                with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                    f.write(text_running)
                    f.seek(0, 0)
                    text = f.read()
                if re.search('!', text) is None:
                    print (u'AP running 命令行第' + str(n) + u'次返回失败')
                    # time.sleep(11)
                    n += 1
                else:
                    print (u"AP running 命令行返回成功")
                    break
            self.operate.click_elem(device_diagnosis_close)

            t = re.search('ip dhcp pool macc_sta_pool\n network '+nat_pool_network_input+' 255.255.255.0', text)
            if t is None:
                print text
            self.assertIsNotNone(t)
            

    
    def test06_ssid_nat_bridge(self):
        """验证AP bridge模式可成功下发/默认下发2个radio/默认支持128个客户端/telnet 密码下发/5G优先关闭"""
        time.sleep(1)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(configuration_basic_xpath)
        time.sleep(5)
        self.operate.click_elem(config_ssid_edit)
        self.operate.click_elem(config_ssid_forward)
        self.operate.click_elem(config_ssid_forward_bridge)
        self.operate.elem_clear_send_keys(config_ssid_forward_bridge_vlan, '100')
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
                if sync_state == 'Sync Failed' or sync_state == 'Synchronized':
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
                time.sleep(11)
                text_running = self.driver.execute_script(js1)
                time.sleep(11)
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
            t_radio = re.search('interface Dot11radio 1/0'+'[^!]*'+'shutdown'+'[\S\s]*'+'interface Dot11radio 2/0'+'[^!]*'
                                + 'shutdown', text)
            t_bridge = re.search('encapsulation dot1Q 100', text)
            t_radio_max_client = re.search('interface Dot11radio 1/0' + '[^!]*' + 'sta-limit 128',text)
                                           # + '[\S\s]*' +
                                           # 'interface Dot11radio 2/0' + '[^!]*' + 'sta-limit 100', text)
            t_telnet_password = re.search('line vty 0 4' + '[^!]*' + 'password ruijie123', text)
            t_band = re.search('band-select enable', text)
            if t_radio is None or t_bridge is None or t_radio_max_client is None or t_telnet_password is None:
                print text
            self.assertIsNone(t_radio)
            self.assertIsNotNone(t_bridge)
            self.assertIsNotNone(t_radio_max_client)
            self.assertIsNotNone(t_telnet_password)
            self.assertIsNone(t_band)
            


    def test07_ssid_radio_Max_clients(self):
        """验证radio 支持的最大客户端数下发成功"""
        time.sleep(1)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(configuration_basic_xpath)
        time.sleep(5)
        self.operate.elem_clear_send_keys(config_ssid_radio_1_max_client, '1')
        self.operate.elem_clear_send_keys(config_ssid_radio_2_max_client, '256')
        self.operate.click_elem(add_SSID_save)
        time.sleep(10)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        time.sleep(2)
        try:
            self.operate.find_elem(add_device_online_ap, By.XPATH, 360)
            while True:
                sync_state = self.operate.find_elem(add_device_state).text
                if sync_state == 'Sync Failed' or sync_state == 'Synchronized':
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
                time.sleep(11)
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

            t_radio_2_client = re.search('interface Dot11radio 2/0' + '[^!]*' + 'sta-limit 256', text)
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
                if sync_state == 'Sync Failed' or sync_state == 'Synchronized':
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
                time.sleep(11)
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
            


    def test09_ssid_bridge_2(self):
        """验证关闭radio 1,打开radio 2"""
        time.sleep(1)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(configuration_basic_xpath)
        time.sleep(5)
        self.operate.click_elem(config_ssid_radio_1)
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
                if sync_state == 'Sync Failed' or sync_state == 'Synchronized':
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
                time.sleep(11)
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
        t_radio_1 = re.search('interface Dot11radio 1/0' + '[^!]*' + 'shutdown', text)

        t_radio_2 = re.search('interface Dot11radio 2/0' + '[^!]*' + 'shutdown', text)
        self.assertIsNotNone(t_radio_1)
        self.assertIsNone(t_radio_2)
        




    def test10_ssid_wpa_psk(self):
        """验证SSID加密方式为wpa_psk"""
        time.sleep(1)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(configuration_basic_xpath)
        time.sleep(5)
        self.operate.click_elem(config_ssid_edit)
        self.operate.click_elem(config_ssid_encryption)
        self.operate.click_elem(config_ssid_encryption_wpa_psk)
        self.operate.elem_clear_send_keys(config_ssid_encryption_wpa_psk_password , config_ssid_encryp_password_wpa_input)
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
                if sync_state == 'Sync Failed' or sync_state == 'Synchronized':
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
                time.sleep(11)
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
                'wlansec 1\n security wpa enable' + '[\S\s]*' + 'security wpa akm psk set-key ascii '
                + config_ssid_encryp_password_wpa_input, text)
            self.assertIsNotNone(t)
            

    def test11_ssid_wpa2_psk(self):
        """验证SSID加密方式为wpa2_psk"""
        time.sleep(1)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(configuration_basic_xpath)
        time.sleep(5)
        self.operate.click_elem(config_ssid_edit)
        self.operate.click_elem(config_ssid_encryption)
        self.operate.click_elem(config_ssid_encryption_wpa2_psk)
        self.operate.elem_clear_send_keys(config_ssid_encryption_wpa_psk_password, config_ssid_encryp_password_wpa2_input)
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
                if sync_state == 'Sync Failed' or sync_state == 'Synchronized':
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
                time.sleep(11)
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
                + config_ssid_encryp_password_wpa2_input, text)
            self.assertIsNotNone(t)
            


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
        self.operate.elem_clear_send_keys(config_ssid_encryption_wpa_psk_password , config_ssid_encryp_password_wpa2_input)
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
                if sync_state == 'Sync Failed' or sync_state == 'Synchronized':
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
                time.sleep(11)
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
                if sync_state == 'Sync Failed' or sync_state == 'Synchronized':
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
                time.sleep(11)
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
                if sync_state == 'Sync Failed' or sync_state == 'Synchronized':
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
                time.sleep(11)
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
            

    def test15_ssid_5G(self):
        """验证SSID 5G优先"""
        time.sleep(1)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(configuration_basic_xpath)
        time.sleep(5)
        self.operate.click_elem(config_ssid_edit)
        self.operate.click_elem(config_ssid_band)
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
                if sync_state == 'Sync Failed' or sync_state == 'Synchronized':
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
                time.sleep(11)
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
            t = re.search('dot11 wlan 1' + '[^!]*'+'band-select enable', text)
            self.assertIsNotNone(t)
            

    def test16_SSID_add(self):
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
                if sync_state == 'Sync Failed' or sync_state == 'Synchronized':
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
                time.sleep(11)
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
            

    def test17_ssid_delete(self):
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
                if sync_state == 'Sync Failed' or sync_state == 'Synchronized':
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
                time.sleep(11)
                text_running = self.driver.execute_script(js1)
                time.sleep(6)
                with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                    f.write(text_running)
                    f.seek(0, 0)
                    text = f.read()
                if re.search('MBSSID', text) is None:
                    print (u'AP MBSSID 命令行第' + str(n) + u'次返回失败')
                    # time.sleep(11)
                    n += 1
                else:
                    print (u"AP MBSSID 命令行返回成功")
                    break
            self.operate.click_elem(device_diagnosis_close)
            t = re.search('MBSSID:\nNone', text)
            self.assertIsNotNone(t)
            

    def test18_ssid_import(self):
        """验证可从其他分组导入SSID配置，不验证其他配置"""
        time.sleep(2)
        self.operate.click_elem(configuration_page_xpath)
        self.operate.click_elem(groups_page_xpath)
        time.sleep(15)
        self.operate.click_elem(add_groups_xpath)  # 点一次可能不生效, 多点几次
        group_name_2 = get_group_name()
        print group_name_2
        self.operate.elem_send_keys(add_groups_input_name_xpath, group_name_2)
        self.operate.click_elem(add_groups_next_page_xpath)
        self.operate.click_elem(add_groups_apply_xpath)
        self.operate.click_elem(add_group_device_ap)
        self.operate.click_elem(add_device_apply_xpath)
        time.sleep(2)
        self.operate.click_elem(add_device_close_xpath)
        time.sleep(2)
        # 将显示分组页面下拉到最后
        js = "var q=document.getElementById('svgBlockDiv').scrollTop=100000"
        self.driver.execute_script(js)
        time.sleep(2)
        # 找到分组点击配置,进入页面config_basic
        self.operate.click_elem(select_group_xpath.format(self.group_name))
        self.operate.click_elem(select_setting_btn_xpath)
        time.sleep(15)
        self.operate.click_elem(config_ssid_more)
        self.operate.click_elem(config_ssid_more_import)
        time.sleep(1)
        js = "var q=document.getElementById('svgBlockDiv').scrollTop=100000"
        self.driver.execute_script(js)
        time.sleep(2)
        self.operate.click_elem(config_ssid_more_import_select_group .format(group_name_2))
        self.operate.click_elem(key_OK)
        time.sleep(5)
        l = len(self.operate.find_elems(config_group_more_config_ssid_list))
        t = self.operate.find_elem(config_ssid_tr1_name).text
        self.assertEqual(t, group_name_2)
        self.assertEqual(l, 1)









if __name__ == '__main__':
    unittest.main()










