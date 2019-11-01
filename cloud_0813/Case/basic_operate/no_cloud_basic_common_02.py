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
        cls.group_name = AddGroup(cls.driver, device_sn={
            'sw': add_device_alert_input_sn_switch,
            'ap': add_device_alert_input_sn,
            'eg': add_device_alert_input_sn_gateway
        }).add_group()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test01_basic_common_config(self):
        """验证添加设备基础配置(SSID)成功"""
        print (self.group_name)
        self.operate.click_elem(add_group_xpath)
        self.operate.elem_send_keys(add_SSID_name, add_SSID_ssid_name)
        # time.sleep(5)
        self.operate.click_elem(add_SSID_open)
        self.operate.click_elem(add_SSID_open)
        self.operate.click_elem(add_SSID_open)
        self.operate.click_elem(add_SSID_WPA2_PSK_1)
        self.operate.elem_send_keys(add_SSID_WPA2_PSK_password, "123456789")
        self.operate.click_elem(add_SSID_forward)
        self.operate.click_elem(add_SSID_forward_1)
        self.operate.click_elem(add_SSID_save_ssid)
        time.sleep(5)
        # 配置一键认证
        self.operate.click_elem(add_group_xpath)
        self.operate.elem_send_keys(add_SSID_name, add_SSID_ssid_name_one_click)
        self.operate.click_elem(add_SSID_enable_auth)
        self.operate.click_elem(add_SSID_one_click_login)
        self.operate.click_elem(add_SSID_save_ssid)
        time.sleep(5)
        # 配置安全密码
        # self.operate.click_elem(add_SSID_security)
        # self.operate.elem_clear_send_keys(add_SSID_security_web_password, add_SSID_web_password)
        # self.operate.elem_clear_send_keys(add_SSID_security_telnet_password, add_SSID_telnet_password)
        # 保存
        self.operate.click_elem(add_SSID_save)




    def test03_check_online_EG(self):
        """验证EG在线"""
        time.sleep(10)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        try:
            self.operate.find_elem(add_device_online_eg, By.XPATH, 180)
        except Exception as e:
            print (e)
            self.assertIsNotNone(None, u"10min内EG上线失败")
        else:
            print (u'EG上线')

    def test04_check_online_sw(self):
        """验证SW在线"""
        time.sleep(10)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_switch)
        try:
            self.operate.find_elem(add_device_online_sw, By.XPATH, 240)
        except Exception as e:
            print (e)
            self.assertIsNotNone(None, u"10min内SW上线失败")
        print (u"SW上线")

    def test05_check_online_AP(self):
        """验证AP在线，配置同步"""
        time.sleep(10)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        try:
            self.operate.find_elem(add_device_online_ap, By.XPATH, 240)
        except Exception as e:
            print e
            self.assertIsNotNone(None, u"AP上线失败")
        else:
            t = 100
            time_ap_online = time.time()
            while True:
                time.sleep(10)
                self.operate.click_elem(device_list_refresh)
                time.sleep(10)
                state_ap = self.operate.find_elem(add_device_state).text
                if state_ap == 'Synced':
                    print(u"AP配置同步成功")
                    time_ap_synced = time.time()
                    t = int((time_ap_synced - time_ap_online) / 60)
                    break
                elif state_ap == 'Sync Failed':
                    break
            if state_ap == 'Sync Failed':
                self.assertIsNotNone(None, u"AP同步配置失败")
            else:
                self.assertIn(t, range(11), u'AP同步配置超时')




    def test06_check_AP_detail(self):
        """验证AP详情"""
        # 查看AP
        time.sleep(2)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        self.operate.click_elem(add_device_device_info.format(add_device_alert_input_sn))
        sn_text_ap = self.operate.find_elem(add_device_device_info_SN, By.XPATH, 10).text
        model_text_ap = self.operate.find_elem(add_device_device_info_model, By.XPATH, 10).text
        hardware_text_ap = self.operate.find_elem(add_device_device_info_hardware).text
        # mac_text_ap = self.operate.find_elem(add_device_device_info_mac).text
        version_text_ap = self.operate.find_elem(add_device_device_info_version, By.XPATH, 10).text
        print(sn_text_ap, version_text_ap)
        # 关闭
        self.operate.click_elem(add_device_device_info_close)
        # 打开命令行
        self.operate.click_elem(device_more)
        self.operate.click_elem(device_diagnosis)
        js1 = 'return $("#cli_result").val();'
        n = 1
        while n < 4:
            self.operate.click_elem(device_running_version)
            time.sleep(11)
            text_version = self.driver.execute_script(js1)
            time.sleep(11)
            with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                # f.truncate()
                # f.write(text_running)
                f.write(text_version)
                f.seek(0, 0)
                text = f.read()
            if re.search('System description', text) is None:
                print (u'AP version 命令行第'+str(n) + u'次返回失败')
                time.sleep(11)
                n += 1
            else:
                print(u"AP version 命令行返回成功")
                break
        self.operate.click_elem(device_diagnosis_close)
        # 验证AP basic信息
        version = re.search(string_escape(version_text_ap) + '[\S\s]*', text)
        model = re.search(model_text_ap + '[\S\s]*', text)
        sn = re.search(sn_text_ap + '[\S\s]*', text)
        hardware = re.search(hardware_text_ap + '[\S\s]*', text)
        self.assertIsNotNone(version, u"AP详情验证不成功")
        self.assertIsNotNone(model, u"AP详情验证不成功")
        self.assertIsNotNone(sn, u"AP详情验证不成功")
        self.assertIsNotNone(hardware, u"AP详情验证不成功")




    def test07_check_ap_basic(self):
        time.sleep(2)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        self.operate.click_elem(add_device_access_point)
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
                # f.truncate()
                f.write(text_running)
                f.seek(0, 0)
                text = f.read()
            if re.search('!', text) is None:
                print (u'AP running 命令行第' + str(n) + u'次返回失败')
                time.sleep(11)
                n += 1
            else:
                print (u"AP running 命令行返回成功")
                break
        self.operate.click_elem(device_diagnosis_close)
        # 验证基础配置
        print (text_running)
        p = re.search(
            add_SSID_ssid_name_default + '[\S\s]*' + add_SSID_ssid_name + '[\S\s]*' + add_SSID_ssid_name_one_click,
            text)
        q = re.search('wlansec 2' + '[\S\s]*' + 'security rsn akm psk set-key ascii 123456789', text)
        # 验证内置认证
        s = re.search('wlansec 3' + '[\S\s]*'+ 'web-auth portal wifidog_3', text)
        self.assertIsNotNone(p, u"SSID配置下发不成功")
        self.assertIsNotNone(q, u"wpa2加密下发不成功")
        self.assertIsNotNone(s, u"SSID内置认证配置下发不成功")



    def test08_check_sw_detail(self):
        """验证交换机详情"""
        # 查看交换机
        time.sleep(10)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_switch)
        if self.operate.find_elems(add_device_online_sw, By.XPATH, 600) != 0:
            print ('SW online')
            self.operate.click_elem(add_device_SW_info.format(add_device_alert_input_sn_switch))
            model_text_sw = self.operate.find_elem(add_device_SW_info_model, By.XPATH, 10).text
            sn_text_sw = self.operate.find_elem(add_device_SW_info_SN).text
            # mac_text_sw = self.operate.find_elem(add_device_device_info_mac)
            version_text_sw = self.operate.find_elem(add_device_SW_info_version, By.XPATH, 10).text
            print (model_text_sw, version_text_sw)
            # 关闭
            self.operate.click_elem(add_device_device_info_close)
        print (string_escape(version_text_sw))
        print (model_text_sw)
        print (sn_text_sw)
        # 查看命令行
        # self.operate.click_elem(sw_select)
        self.operate.click_elem(sw_more)
        self.operate.click_elem(sw_diagnosis)
        js1 = 'return $("#cli_result").val();'
        n = 1
        while n < 4:
            self.operate.click_elem(device_running_version)
            time.sleep(11)
            text_version = self.driver.execute_script(js1)
            f = open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+')
            f.write(text_version)
            f.seek(0, 0)
            text = f.read()
            f.close()
            if re.search('System', text) is None:
                print (u'交换机命令行第' + str(n) +u'次返回失败')
                time.sleep(11)
            else:
                print (u"交换机命令行返回成功")
                break
        self.operate.click_elem(device_diagnosis_close)
        t = re.search(model_text_sw+'[\S\s]*'+string_escape(version_text_sw)+'[\S\s]*'+ sn_text_sw, text)
        # version = re.search(string_escape(version_text_sw), text)
        # model = re.search(model_text_sw, text)
        # sn = re.search(sn_text_sw, text)
        # self.operate.click_elem(web_cli_close)
        # self.assertIsNotNone(version)
        # self.assertIsNotNone(model)
        # self.assertIsNotNone(sn)
        self.assertIsNotNone(t)
        # print (t.group())




    def test09_check_eg_detail(self):
        """验证EG详情"""
        # 查看EG
        time.sleep(10)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        if self.operate.find_elems(add_device_online_eg, By.XPATH, 600) != 0:
            print ("EG online")
            self.operate.click_elem(add_device_eg_info.format(add_device_alert_input_sn_gateway))
            model_text_eg = self.operate.find_elem(add_device_EG_info_model).text
            version_text_eg = self.operate.find_elem(add_device_EG_info_version).text
            sn_text_eg = self.operate.find_elem(add_device_EG_info_SN).text
            print(model_text_eg, version_text_eg)
            # 关闭
            self.operate.click_elem(add_device_device_info_close)
        print (version_text_eg)
        print (model_text_eg)
        # 查看命令行
        # self.operate.click_elem(eg_select)
        self.operate.click_elem(eg_more)
        self.operate.click_elem(eg_diagnosis)
        n = 1
        while n < 4:
            self.operate.click_elem(device_running_version)
            time.sleep(11)
            js1 = 'return $("#cli_result").val();'
            text = self.driver.execute_script(js1)
            f = open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+')
            f.write(text)
            f.seek(0, 0)
            text = f.read()
            f.close()
            if re.search('System', text) is None:
                print (u'EG命令行'+str(n) + u'返回失败')
                time.sleep(11)
            else:
                print (u"EG命令行返回成功")
                break
        t = re.search(model_text_eg + '[\S\s]*' + string_escape(version_text_eg) + '[\S\s]*' + sn_text_eg, text)
        self.operate.click_elem(web_cli_close)
        self.assertIsNotNone(t)






if __name__ == '__main__':
    unittest.main()










