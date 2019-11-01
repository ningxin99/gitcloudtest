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
from Common.group_init import GroupInit


global text



class ConfigDeliver(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Pyse("chrome")
        Login(cls.driver, user_cloud_local, password_cloud_local, login_url_local).login()
        cls.operate = ComFunction(cls.driver)
        cls.group_name = AddGroup(cls.driver, device_sn={'ap': add_device_alert_input_sn,
                                                         'sw': add_device_alert_input_sn_switch,
                                                         'eg': add_device_alert_input_sn_gateway
                                                         },

                                  alias=device_input_alias_data).add_group()
        GroupInit(cls.driver).group_init()



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # def test00(self):
    #     # 调试代码
    #     self.operate.click_elem(configuration_page_xpath)  # 没有等60s
    #     self.operate.click_elem(groups_page_xpath)
    #     js = "var q=document.getElementById('svgBlockDiv').scrollTop=100000"
    #     self.driver.execute_script(js)
    #     time.sleep(5)
    #     # 找到分组点击配置,进入页面config_basic
    #     self.operate.click_elem(select_group_xpath.format('G1N'))
    #     self.operate.click_elem(select_setting_btn_xpath)
    # 调试代码


    def test01_ap(self):
        """将AP sh run 的命令行写入cmd.text"""
        print (self.group_name)
        time.sleep(1)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        self.operate.click_elem(add_device_access_point)
        time.sleep(2)
        while True:
            t = self.operate.find_elem(add_device_state).text
            if t == 'Sync Failed' or t == 'Synchronized':
                break
        self.operate.click_elem(device_select)
        self.operate.click_elem(device_more)
        self.operate.click_elem(device_diagnosis)
        js1 = 'return $("#cli_result").val();'
        n = 1
        while n < 4:
            self.operate.click_elem(device_running_config)
            time.sleep(10)
            text_running = self.driver.execute_script(js1)
            time.sleep(10)
            with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                f.write(text_running)
                f.seek(0, 0)
                global text
                text = f.read()
            if re.search('!', text) is None:
                print (u'AP running 命令行第' + str(n) + u'次返回失败')
                time.sleep(5)
                n += 1
            else:
                print (u"AP running 命令行返回成功")
                break
        self.operate.click_elem(device_diagnosis_close)
        self.assertEqual(t, 'Synchronized', u'AP配置同步失败')


    def test02_settings_cwmp(self):
        """验证下发的CWMP保活时间为180s"""
        t = re.search('cwmp' + '[^!]*' + 'cpe inform interval 180', text)
        if t is None:
            print text
        self.assertIsNotNone(t)



    def test03_setting_radio_country_code(self):
        """验证下发默认国家码和配置的带宽,信道"""
        t = re.search('interface Dot11radio 1/0' + '[^!]*' + 'channel 3' + '[^!]*' + 'chan-width 40'
                      + '[\S\s]*'
                      + 'interface Dot11radio 2/0' + '[^!]*' + 'channel 157' + '[^!]*' + 'chan-width 40'
                      , text)
        if t is None:
            print text
        self.assertIsNotNone(t)

    def test04_setting_radio_power(self):
        """验证下发radio的功率"""
        t1 = re.search('interface Dot11radio 1/0' + '[^!]*' + 'power local', text)
        t2 = re.search('interface Dot11radio 2/0' + '[^!]*' + 'power local 90', text)
        if t1 is None or t2 is None:
            print text
        self.assertIsNone(t1)
        self.assertIsNotNone(t2)

    def test05_setting_device_name(self):
        """验证下发设备别名"""
        t = re.search('hostname ' + device_input_alias_data, text)
        if t is None:
            print text
        self.assertIsNotNone(t)

    def test06_setting_log(self):
        """验证下发log服务器地址"""
        t = re.search('macc wis enable'+ '[^!]*' +  'log_mng set log-server', text)
        if t is None:
            print text
        self.assertIsNotNone(t)

    def test07_setting_RF_parameter(self):
        """验证radio限制连接用户数"""
        t = re.search('interface Dot11radio 1/0' + '[^!]*' + 'sta-limit 128'
                      + '[\S\s]*'
                      + 'interface Dot11radio 2/0'+ '[^!]*' + 'sta-limit 100'
                      , text)
        if t is None:
            print text
        self.assertIsNotNone(t)
    '''
    def test08_setting_custom_cli(self):
        """验证下发cli配置"""
        t = re.search('http redirect port 443\nweb-auth sta-preemption enable', text)
        if t is None:
            print text
        self.assertIsNotNone(t)

    def test09_setting_bluetooth(self):
        """验证下发的蓝牙配置"""
        t = re.search('ibeacon uuid ' + bluetooth_UUID_input + ' major ' + bluetooth_major_input + ' minor '
                      + bluetooth_major_input, text)
        if t is None:
            print text
        self.assertIsNotNone(t)

    
    def test13_sw_setting_vlan(self):
        """验证下发vlan"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_switch)
        time.sleep(5)
        self.operate.click_elem(add_device_SW_info.format(add_device_alert_input_sn_switch))
        self.operate.click_elem(device_sw_detail_config)
        time.sleep(5)
        self.operate.click_elem(device_sw_detail_vlan_add)
        self.operate.elem_send_keys(device_sw_detail_vlan_id, sw_vlan_id_input)
        self.operate.click_elem(device_sw_detail_vlan_add_confirm)
        time.sleep(5)
        self.operate.click_elem(add_device_device_info_close)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_switch)
        time.sleep(2)
        # 查看命令行
        self.operate.click_elem(sw_select)
        self.operate.click_elem(sw_more)
        self.operate.click_elem(sw_diagnosis)
        js1 = 'return $("#cli_result").val();'
        n = 1
        while n < 4:
            self.operate.click_elem(device_web_cli)
            self.operate.click_elem(device_web_cli_2)
            self.operate.elem_send_keys(device_web_cli_cmd, 'sh vlan')
            self.operate.click_elem(device_web_cli_cmd_send)
            time.sleep(20)
            text_version = self.driver.execute_script(js1)
            # time.sleep(10)
            f = open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+')
            f.write(text_version)
            f.seek(0, 0)
            global text
            text = f.read()
            f.close()
            if re.search('VLAN', text) is None:
                print (u'交换机命令行第' + str(n) + u'次返回失败')
                time.sleep(10)
                n += 1
            else:
                print (u"交换机命令行返回成功")
                break
        self.operate.click_elem(device_diagnosis_close)
        time.sleep(2)
        # 删除添加的vlan
        self.operate.click_elem(add_device_SW_info.format(add_device_alert_input_sn_switch))
        self.operate.click_elem(device_sw_detail_config)
        self.operate.click_elem(device_sw_detail_vlan_page_last)
        self.operate.click_elem(device_sw_detail_vlan_delete.format(sw_vlan_id_input))
        self.operate.click_elem(key_OK)
        time.sleep(5)
        self.operate.click_elem(add_device_device_info_close)
        # 断言
        t = re.search('VLAN'+ sw_vlan_id_input, text)
        if t is None:
            print text
        self.assertIsNotNone(t)



    def test14_sw_setting_port(self):
        """验证下发trunk/native vlan 接口配置"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_switch)
        time.sleep(5)
        self.operate.click_elem(add_device_SW_info.format(add_device_alert_input_sn_switch))
        # 交换机端口配置下发
        self.operate.click_elem(device_sw_detail_port)
        time.sleep(2)
        port = self.operate.find_elems(device_sw_detail_int_down)
        port[0].click()
        interface_name = self.operate.find_elem(device_sw_detail_int_name).text
        print interface_name
        self.operate.click_elem(device_sw_detail_int_trunk)
        self.operate.elem_clear_send_keys(device_sw_detail_int_trunk_native_vlan_id, sw_native_vlan_id_input)
        self.operate.click_elem(device_sw_detail_int_save)
        time.sleep(5)
        self.operate.click_elem(add_device_device_info_close)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_switch)
        time.sleep(2)
        # 查看命令行
        self.operate.click_elem(sw_select)
        self.operate.click_elem(sw_more)
        self.operate.click_elem(sw_diagnosis)
        js1 = 'return $("#cli_result").val();'
        n = 1
        while n < 4:
            self.operate.click_elem(device_running_config)
            time.sleep(10)
            text_version = self.driver.execute_script(js1)
            time.sleep(5)
            f = open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+')
            f.write(text_version)
            f.seek(0, 0)
            global text
            text = f.read()
            f.close()
            if re.search('!', text) is None:
                print (u'交换机命令行第' + str(n) + u'次返回失败')
                time.sleep(10)
            else:
                print (u"交换机命令行返回成功")
                break
        self.operate.click_elem(device_diagnosis_close)
        # 恢复端口初始配置
        self.operate.click_elem(add_device_SW_info.format(add_device_alert_input_sn_switch))
        self.operate.click_elem(device_sw_detail_port)
        time.sleep(2)
        port = self.operate.find_elems(device_sw_detail_int_down)
        port[0].click()
        self.operate.click_elem(device_sw_detail_int_access)
        self.operate.elem_clear_send_keys(device_sw_detail_int_accesss_vlan_id , '1')
        self.operate.click_elem(device_sw_detail_int_save)
        time.sleep(5)
        self.operate.click_elem(add_device_device_info_close)
        # 断言
        t = re.search(interface_name[8:][:-1] + '[^!]*' + 'switchport mode trunk' + '[^!]*' +
                      'switchport trunk native vlan ' + sw_native_vlan_id_input, text)
        if t is None:
            print text
        self.assertIsNotNone(t)

    def test15_sw_setting_rldp(self):
        """验证下发RLDP配置"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_switch)
        time.sleep(5)
        self.operate.click_elem(add_device_SW_info.format(add_device_alert_input_sn_switch))
        self.operate.click_elem(device_sw_detail_config)
        leng = 0
        try:
            leng = len(self.operate.find_elems(device_sw_detail_rldp_green, by=By.XPATH, wait_times=20))
        except Exception as e:
            self.operate.scroll_into_view(device_sw_RLDP_enable)
            self.operate.click_elem(device_sw_RLDP_auto_config)
            self.operate.click_elem(key_OK)
            time.sleep(2)
            leng = len(self.operate.find_elems(device_sw_detail_rldp_green, by=By.XPATH, wait_times=20))
        finally:
            self.operate.click_elem(add_device_device_info_close)
        time.sleep(2)
        # 查看命令行
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_switch)
        self.operate.click_elem(add_device_switch)
        self.operate.click_elem(sw_select)
        self.operate.click_elem(sw_more)
        self.operate.click_elem(sw_diagnosis)
        js1 = 'return $("#cli_result").val();'
        n = 1
        while n < 4:
            self.operate.click_elem(device_running_config)
            time.sleep(10)
            text_version = self.driver.execute_script(js1)
            time.sleep(5)
            f = open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+')
            f.write(text_version)
            f.seek(0, 0)
            global text
            text = f.read()
            f.close()
            if re.search('!', text) is None:
                print (u'交换机命令行第' + str(n) + u'次返回失败')
                time.sleep(10)
            else:
                print (u"交换机命令行返回成功")
                break
        self.operate.click_elem(device_diagnosis_close)
        t = re.findall('rldp port loop-detect warning', text)
        if t is None:
            print text
        self.assertEqual(len(t), leng)



    def test16_sw_setting_cwmp(self):
        """验证CWMP保活时间下发"""
        t = re.search('cwmp' + '[^!]*' + 'cpe inform interval 180', text)
        if t is None:
            print text
        self.assertIsNotNone(t)



    def test19_sw_setting_device_name(self):
        """验证下发设备别名"""
        t = re.search('hostname ' + device_input_alias_data, text)
        if t is None:
            print text
        self.assertIsNotNone(t)
    '''




if __name__ == '__main__':
    unittest.main()