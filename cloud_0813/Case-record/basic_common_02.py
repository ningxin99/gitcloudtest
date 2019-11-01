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

# 升级前的设备版本
global firmware_ap_before_upgrade, firmware_sw_now, firmware_eg_now
# 升级后的设备版本
global firmware_ap, firmware_sw, firmware_eg



class BasicCommon(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Pyse("chrome")
        Login(cls.driver, url=login_url_cloud).login()
        cls.operate = ComFunction(cls.driver)
        AddGroup(cls.driver).add_group()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test01_basic_common_config(self):
        """验证添加设备基础配置(SSID)成功"""
        time.sleep(30)
        self.operate.click_elem(add_group_xpath)
        self.operate.elem_send_keys(add_SSID_name, add_SSID_ssid_name)
        # 配置SSID为加密，转发模式为nat
        # m = self.driver.find_element_by_xpath(add_SSID_open)

        time.sleep(5)
        self.operate.click_elem(add_SSID_open)
        self.operate.click_elem(add_SSID_open)
        self.operate.click_elem(add_SSID_open)
        # m.find_element_by_xpath("//option[@value='WPA2_PSK']").click()
        self.operate.click_elem(add_SSID_WPA2_PSK_1)
        self.operate.elem_send_keys(add_SSID_WPA2_PSK_password, "123456789")
        self.operate.click_elem(add_SSID_forward)
        # n = self.driver.find_element_by_xpath(add_SSID_forward)
        # n.find_element_by_xpath("//option[@value='nat']").click()
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
        self.operate.click_elem(add_SSID_security)
        self.operate.elem_send_keys(add_SSID_security_web_password, add_SSID_web_password)
        self.operate.elem_send_keys(add_SSID_security_telnet_password, add_SSID_telnet_password)
        # 保存
        self.operate.click_elem(add_SSID_save)





    def test02_basic_common_add_device(self):
        """添加设备：AP，sw，EG"""
        # # 调试代码
        # time.sleep(20)
        # self.operate.click_elem(configuration_page_xpath)  # 没有等60s
        # self.operate.click_elem(configuration_basic_xpath)
        # # 调试代码
        time.sleep(20)
        # 点击进入监控-AP，添加AP
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        time.sleep(15)
        self.operate.click_elem(add_device_add_access_point)
        time.sleep(5)
        self.operate.click_elem(add_device_alert_add_access_point)
        self.operate.elem_send_keys(add_device_alert_sn, add_device_alert_input_sn)
        self.operate.click_elem(add_device_alert_save)
        time.sleep(10)
        # 添加SW
        self.operate.click_elem(add_device_switch)
        time.sleep(15)
        self.operate.click_elem(add_device_add_switch)
        time.sleep(5)
        self.operate.click_elem(add_device_alert_add_access_point)
        self.operate.elem_send_keys(add_device_alert_sn_switch, add_device_alert_input_sn_switch)
        self.operate.click_elem(add_device_alert_save_switch)
        time.sleep(10)
        # 添加EG
        self.operate.click_elem(add_device_gateway)
        time.sleep(15)
        self.operate.click_elem(add_device_add_gateway)
        time.sleep(5)
        self.operate.elem_send_keys(add_device_alert_sn_gateway, add_device_alert_input_sn_gateway)
        self.operate.elem_send_keys(add_device_alert_password, add_device_alert_input_password)
        self.operate.click_elem(add_device_alert_save_gateway)
        time.sleep(10)
    
    def test03_check_online_EG(self):
        """验证EG在线"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        try:
            self.assertIsNotNone(self.operate.find_elem(add_device_online_eg, By.XPATH, 600), u"10min内EG上线失败")
        except:
            self.assertIsNotNone(None, u"10min内EG上线失败")
        else:
            print (u'EG上线')

    def test04_check_online_sw(self):
        """验证SW在线"""
        time.sleep(10)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_switch)
        try:
            self.assertIsNotNone(self.operate.find_elem(add_device_online_sw, By.XPATH, 600), u"10min内sw上线失败")
        except:
            self.assertIsNotNone(None, u"10min内SW上线失败")
        print (u"SW上线")

    def test05_check_online_AP(self):
        """验证AP在线，配置同步"""
        time.sleep(10)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        try:
            self.assertIsNotNone(self.operate.find_elem(add_device_online_ap, By.XPATH, 900), u"15min内AP上线失败")
            time_ap_online = time.time()
            self.operate.find_elem(add_device_synced, By.XPATH, 2700)
            time_ap_synced = time.time()
            t = int((time_ap_synced - time_ap_online) / 60)
            print (t)
            self.assertIsNotNone(self.operate.find_elem(add_device_synced, By.XPATH, 900), u"15min内AP同步失败")
        except:
            add_device_state_text = self.operate.find_elem(add_device_state).text
            if 'fail' in add_device_state_text:
                self.assertIsNotNone(None, u"AP同步配置失败")
            else:
                self.assertIsNotNone(None, u"15min内AP上线或同步失败")
        else:
            print (u"ap上线")
            self.assertIn(t, range(11), u'AP同步配置超时')


    def test06_check_device_detail(self):
        """查看设备详情"""
        # # 调试代码
        # time.sleep(30)
        # self.operate.click_elem(configuration_page_xpath)  # 没有等60s
        # self.operate.click_elem(configuration_basic_xpath)
        # time.sleep(10)
        # self.operate.click_elem(add_device_monitoring)
        # self.operate.click_elem(add_device_access_point)
        # # 调试代码


    def test06_check_AP_detail(self):
        """验证AP详情"""
        # 查看AP
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        # if self.operate.find_elems(add_device_online_ap, By.XPATH, 600) != 0 and self.operate.find_elem(
        #         add_device_synced, By.XPATH, 2400) != 0:
        time.sleep(40)
        print (add_device_device_info.format(add_device_alert_input_sn))
        self.operate.click_elem(add_device_device_info.format(add_device_alert_input_sn))
        sn_text_ap = self.operate.find_elem(add_device_device_info_SN, By.XPATH, 10).text
        model_text_ap = self.operate.find_elem(add_device_device_info_model, By.XPATH, 10).text
        hardware_text_ap = self.operate.find_elem(add_device_device_info_hardware).text
        mac_text_ap = self.operate.find_elem(add_device_device_info_mac).text
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
            time.sleep(30)
            text_version = self.driver.execute_script(js1)
            time.sleep(20)
            with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                # f.truncate()
                # f.write(text_running)
                f.write(text_version)
                f.seek(0, 0)
                text = f.read()
            if re.search('System description', text) is None:
                print (u'AP version 命令行第'+str(n) + u'次返回失败')
                time.sleep(20)
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
        # print (version.group())
        self.assertIsNotNone(version, u"AP详情验证不成功")
        self.assertIsNotNone(model, u"AP详情验证不成功")
        self.assertIsNotNone(sn, u"AP详情验证不成功")
        self.assertIsNotNone(hardware, u"AP详情验证不成功")


    def test07_check_ap_basic(self):
        self.operate.click_elem(device_more)
        self.operate.click_elem(device_diagnosis)
        js1 = 'return $("#cli_result").val();'
        n = 1
        while n < 4:
            self.operate.click_elem(device_running_config)
            time.sleep(30)
            text_running = self.driver.execute_script(js1)
            time.sleep(20)
            with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                # f.truncate()
                f.write(text_running)
                f.seek(0, 0)
                text = f.read()
            if re.search('!', text) is None:
                print (u'AP running 命令行第' + str(n) + u'次返回失败')
                time.sleep(20)
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
        q = re.search('wlansec 2[\S\s]*security rsn akm psk set-key ascii 123456789', text)
        # 验证内置认证
        s = re.search('wlansec 3[\S\s]*web-auth portal wifidog_3', text)
        print (p.group())
        print (q.group())
        print (s.group())
        self.assertIsNotNone(p, u"SSID配置下发不成功")
        self.assertIsNotNone(q, u"wpa2加密下发不成功")
        self.assertIsNotNone(s, u"SSID内置认证配置下发不成功")




    def test08_check_sw_detail(self):
        """验证交换机详情"""
        # 查看交换机
        time.sleep(10)
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
            time.sleep(30)
            # text_running = self.driver.execute_script(js1)
            # time.sleep(10)
            # self.operate.click_elem(device_running_version)
            text_version = self.driver.execute_script(js1)
            f = open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+')
            # f.write(text_running)
            f.write(text_version)
            f.seek(0, 0)
            text = f.read()
            f.close()
            if re.search('System', text) is None:
                print (u'交换机命令行第' + str(n) +u'次返回失败')
                time.sleep(30)
            else:
                print (u"交换机命令行返回成功")
                break
        t = re.search(model_text_sw+'[\S\s]*'+string_escape(version_text_sw)+'[\S\s]*'+ sn_text_sw, text)
        version = re.search(string_escape(version_text_sw), text)
        model = re.search(model_text_sw, text)
        sn = re.search(sn_text_sw, text)
        self.operate.click_elem(web_cli_close)
        self.assertIsNotNone(version)
        self.assertIsNotNone(model)
        self.assertIsNotNone(sn)
        self.assertIsNotNone(t)
        print (t.group())



    def test09_check_eg_detail(self):
        """验证EG详情"""
        # 查看EG
        time.sleep(10)
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
            time.sleep(30)
            js1 = 'return $("#cli_result").val();'
            text = self.driver.execute_script(js1)
            f = open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+')
            f.write(text)
            f.seek(0, 0)
            text = f.read()
            f.close()
            if re.search('System', text) is None:
                print (u'EG命令行'+str(n) + u'返回失败')
                time.sleep(30)
            else:
                print (u"EG命令行返回成功")
                break
        t = re.search(model_text_eg + '[\S\s]*' + string_escape(version_text_eg) + '[\S\s]*' + sn_text_eg, text)
        self.operate.click_elem(web_cli_close)
        self.assertIsNotNone(t)

    def test11_upgrade(self):
        """AP升级操作"""
        time.sleep(5)
        self.operate.click_elem(maintenance)
        self.operate.click_elem(upgrade_upgrade)
        time.sleep(5)
        global firmware_ap_before_upgrade
        firmware_ap_before_upgrade = self.operate.find_elem(upgrade_device_AP_v).text
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
        print (firmware_ap[-10:])
        self.operate.click_elem(upgrade_finish)
        self.operate.click_elem(select_firmware_upgrade)
        time.sleep(15)

    # def test11_upgrade(self):
    #     """交换机升级操作"""
    #     global firmware_sw_now
    #     firmware_sw_now = self.operate.find_elem(upgrade_device_SW_v).text
    #     print (firmware_sw_now)
    #     self.operate.click_elem(upgrade_device_SW)
    #     self.operate.click_elem(select_firmware)
    #     self.operate.click_elem(select_firmware_private)
    #     global firmware_sw
    #     l = self.operate.find_elems(select_firmware_list_length).length
    #     for i in range(l):
    #         print select_firmware_tr_td2.formate(str(l - 1))
    #         firmware_sw = self.operate.find_elem(select_firmware_tr_td2).formate(str(l - 1)).text
    #         if firmware_sw[-10:] == firmware_sw_now[-10:]:
    #             self.operate.click_elem(select_firmware_list_tr1_td1).formate(str(l - 1))
    #             break
    #
    #     print (firmware_sw)
    #     self.operate.click_elem(upgrade_finish)
    #     self.operate.click_elem(select_firmware_upgrade)
    #     time.sleep(15)
    #
    # def test12_upgrade(self):
    #     """EG升级操作"""
    #     global firmware_eg_now
    #     firmware_eg_now = self.operate.find_elem(upgrade_device_EG_v).text
    #     self.operate.click_elem(upgrade_device_EG)
    #     self.operate.click_elem(select_firmware)
    #     self.operate.click_elem(select_firmware_private)
    #     global firmware_eg
    #     l = self.operate.find_elems(select_firmware_list_length).length
    #     for i in range(l):
    #         print select_firmware_tr_td2.formate(str(l - 1))
    #         firmware_eg = self.operate.find_elem(select_firmware_tr_td2).formate(str(l - 1)).text
    #         if firmware_eg[-10:] == firmware_eg_now[-10:]:
    #             self.operate.click_elem(select_firmware_list_tr1_td1).formate(str(l - 1))
    #             break
    #     self.operate.click_elem(upgrade_finish)
    #     self.operate.click_elem(select_firmware_upgrade)

    def test13_check(self):
        """验证AP成功升级"""
        self.operate.click_elem(maintenance)
        self.operate.click_elem(view_log_upgrade_log)
        print (u"升级中~")
        while True:
            try:
                self.operate.find_elem(view_log_upgrade_log_success)
            except:
                time.sleep(60)
                self.operate.click_elem(view_log_upgrade_log_refresh)
            else:
                self.operate.click_elem(upgrade_upgrade)
                break
        firmware_ap_before_upgrade_upgrade = self.operate.find_elem(upgrade_device_AP_v).text
        global firmware_ap
        print (firmware_ap[-10:])
        print (firmware_ap_before_upgrade_upgrade[-10:])
        self.assertEqual(firmware_ap[-10:], firmware_ap_before_upgrade_upgrade[-10:])

    # def test14_check(self):
    #     """验证交换机成功升级"""
    #     firmware_sw_now_upgrade = self.operate.find_elem(upgrade_device_SW_v).text
    #     global firmware_sw
    #     print (firmware_sw[-10:])
    #     print (firmware_sw_now_upgrade[-10:])
    #     self.assertEqual(firmware_sw[-10:], firmware_sw_now_upgrade[-10:])
    #
    # def test15_check(self):
    #     """验证EG成功升级"""
    #     global firmware_eg
    #     firmware_eg_now_upgrade = self.operate.find_elem(upgrade_device_EG_v).text
    #     self.assertEqual(firmware_eg[-10:], firmware_eg_now_upgrade[-10:])

    def test16_upgrade(self):
        """AP版本回退操作"""
        time.sleep(5)
        self.operate.click_elem(maintenance)
        self.operate.click_elem(upgrade_upgrade)
        time.sleep(5)
        global firmware_ap_before_upgrade
        self.operate.click_elem(upgrade_device_AP)
        self.operate.click_elem(select_firmware)
        self.operate.click_elem(select_firmware_private)
        global firmware_ap
        firmware_ap = self.operate.find_elem(select_firmware_list_tr1_td2).text
        print (firmware_ap_before_upgrade[-10:])
        if firmware_ap_before_upgrade[-10:] == firmware_ap[-10:]:
            self.operate.click_elem(select_firmware_list_tr1_td1)
        else:
            self.operate.click_elem(select_firmware_list_tr2_td1)
            firmware_ap = self.operate.find_elem(select_firmware_list_tr2_td2).text
        print (firmware_ap[-10:])
        self.operate.click_elem(upgrade_finish)
        self.operate.click_elem(select_firmware_upgrade)
        time.sleep(15)


        # time.sleep(5)
        # self.operate.click_elem(maintenance)
        # self.operate.click_elem(upgrade_upgrade)
        # time.sleep(5)
        # global firmware_ap_before_upgrade
        # firmware_ap_before_upgrade = self.operate.find_elem(upgrade_device_AP_v).text
        # self.operate.click_elem(upgrade_device_AP)
        # self.operate.click_elem(select_firmware)
        # self.operate.click_elem(select_firmware_private)
        # global firmware_ap
        # l = self.operate.find_elems(select_firmware_list_length).length
        # for i in range(l):
        #     print select_firmware_tr_td2.formate(str(l - 1))
        #     firmware_ap = self.operate.find_elem(select_firmware_tr_td2).formate(str(l - 1)).text
        #     if firmware_ap[-10:] == firmware_ap_before_upgrade[-10:]:
        #         self.operate.click_elem(select_firmware_list_tr1_td1).formate(str(l - 1))
        #         break
        # print (firmware_ap_before_upgrade[-10:])
        # print (firmware_ap[-10:])
        # self.operate.click_elem(upgrade_finish)
        # self.operate.click_elem(select_firmware_upgrade)
        # time.sleep(15)

    # def test17_upgrade(self):
    #     global firmware_sw_now
    #     firmware_sw_now = self.operate.find_elem(upgrade_device_SW_v).text
    #     print (firmware_sw_now)
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
    #     print (firmware_sw)
    #     self.operate.click_elem(upgrade_finish)
    #     self.operate.click_elem(select_firmware_upgrade)
    #     time.sleep(15)
    #
    # def test18_upgrade(self):
    #     global firmware_eg_now
    #     firmware_eg_now = self.operate.find_elem(upgrade_device_EG_v).text
    #     self.operate.click_elem(upgrade_device_EG)
    #     self.operate.click_elem(select_firmware)
    #     self.operate.click_elem(select_firmware_private)
    #     global firmware_eg
    #     firmware_eg = self.operate.find_elem(select_firmware_list_tr1_td2).text
    #     if firmware_eg_now[-10:] == firmware_eg[-10:]:
    #         self.operate.click_elem(select_firmware_list_tr2_td1)
    #         firmware_eg = self.operate.find_elem(select_firmware_list_tr2_td2).text
    #     else:
    #         self.operate.click_elem(select_firmware_list_tr1_td1)
    #     self.operate.click_elem(upgrade_finish)
    #     self.operate.click_elem(select_firmware_upgrade)


    def test19_check(self):
        """验证AP版本成功回退"""
        self.operate.click_elem(maintenance)
        self.operate.click_elem(view_log_upgrade_log)
        print (u"升级中~")
        while True:
            try:
                self.operate.find_elem(view_log_upgrade_log_success)
            except:
                time.sleep(60)
                self.operate.click_elem(view_log_upgrade_log_refresh)
            else:
                self.operate.click_elem(upgrade_upgrade)
                break
        firmware_ap_before_upgrade_upgrade = self.operate.find_elem(upgrade_device_AP_v).text
        global firmware_ap_before_upgrade
        print (firmware_ap_before_upgrade[-10:])
        print (firmware_ap_before_upgrade_upgrade[-10:])
        self.assertEqual(firmware_ap_before_upgrade[-10:], firmware_ap_before_upgrade_upgrade[-10:])

    # def test20_check(self):
    #     """验证交换机版本成功回退"""
    #     firmware_sw_now_upgrade = self.operate.find_elem(upgrade_device_SW_v).text
    #     global firmware_sw_now
    #     print (firmware_sw_now[-10:])
    #     print (firmware_sw_now_upgrade[-10:])
    #     self.assertEqual(firmware_sw_now[-10:], firmware_sw_now_upgrade[-10:])
    #
    # def test21_check(self):
    #     """验证EG版本成功回退"""
    #     global firmware_eg_now
    #     firmware_eg_now_upgrade = self.operate.find_elem(upgrade_device_EG_v).text
    #     self.assertEqual(firmware_eg_now[-10:], firmware_eg_now_upgrade[-10:])







if __name__ == '__main__':
    try:
        unittest.main()
    except Exception as e:
        print e





'''
(05242419)
(05242419)
'''





