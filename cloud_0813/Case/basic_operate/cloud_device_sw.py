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
from Page.device_page import *
from Page.basic_page import *
from Data.device_data import *
from PIL import Image


class DeviceSw(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Pyse("chrome")
        Login(cls.driver, user_cloud_local, password_cloud_local, login_url_local).login()
        cls.operate = ComFunction(cls.driver)
        cls.group_name = AddGroup(cls.driver, device_sn={'sw': add_device_alert_input_sn_switch},
                                  alias=device_input_alias_data).add_group()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test01_SW_alias(self):
        """验证SW别名可修改成功"""
        # 调试代码
        # self.operate.click_elem(configuration_page_xpath)  # 没有等60s
        # self.operate.click_elem(configuration_basic_xpath)
        # time.sleep(5)
        # self.operate.click_elem(add_device_monitoring)
        # self.operate.click_elem(add_device_switch)
        # 调试代码
        print (self.group_name)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_switch)
        time.sleep(5)
        self.operate.click_elem(device_sw_alias)
        self.operate.elem_clear_send_keys(device_alias_sw_input, device_sw_input_alias_data)
        self.operate.click_elem(device_alias_sw_input_confirm)
        sw_alias = self.operate.find_elem(device_sw_alias).text
        time.sleep(5)
        self.assertEqual(sw_alias, device_sw_input_alias_data)


    def test01_check_online_SW(self):
        """验证SW在线"""

        time.sleep(10)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_switch)
        try:
            self.operate.find_elem(add_device_online_sw, By.XPATH, 900)
        except Exception as e:
            print e
            self.assertIsNotNone(None, u"SW上线失败")
        else:
            print (u"SW成功上线")


    def test04_SW_detail_version(self):
        """验证设备详情version信息与命令行一致，version信息：SN，model，hardware，version"""
        time.sleep(10)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_switch)
        time.sleep(5)
        self.operate.click_elem(add_device_SW_info.format(add_device_alert_input_sn_switch))
        model_text_sw = self.operate.find_elem(add_device_SW_info_model, By.XPATH, 10).text
        sn_text_sw = self.operate.find_elem(add_device_SW_info_SN).text
        version_text_sw = self.operate.find_elem(add_device_SW_info_version, By.XPATH, 10).text
        print (model_text_sw, version_text_sw)
        # 关闭
        self.operate.click_elem(add_device_device_info_close)
        # 查看命令行
        self.operate.click_elem(sw_select)
        self.operate.click_elem(sw_more)
        self.operate.click_elem(sw_diagnosis)
        js1 = 'return $("#cli_result").val();'
        n = 1
        while n < 4:
            self.operate.click_elem(device_running_version)
            time.sleep(30)
            text_version = self.driver.execute_script(js1)
            f = open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+')
            f.write(text_version)
            f.seek(0, 0)
            text = f.read()
            f.close()
            if re.search('System', text) is None:
                print (u'交换机命令行第' + str(n) + u'次返回失败')
                time.sleep(10)
                n += 1
            else:
                print (u"交换机命令行返回成功")
                break

        t = re.search(model_text_sw + '[\S\s]*' + string_escape(version_text_sw) + '[\S\s]*' + sn_text_sw, text)

        self.operate.click_elem(web_cli_close)
        self.assertIsNotNone(t)



    def test05_SW_detail_cpu(self):
        """验证交换机的cpu/memory信息有数据，不验证其正确性"""
        time.sleep(1)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_switch)
        time.sleep(5)
        self.operate.click_elem(add_device_SW_info.format(add_device_alert_input_sn_switch))
        time.sleep(2)
        view_path = self.operate.save_screen_shot('viewSW')
        try:
            element_cpu = self.operate.find_elem(device_sw_detail_cpu)
            element_memory = self.operate.find_elem(device_sw_detail_memory)
            self.operate.find_elem(device_sw_detail_speed)
        except Exception as e:
            self.assertIsNotNone(None, u"交换机的cpu/memory值为空或者speed数据为空")
        else:
            # mmeory图片截图
            left = element_memory.location['x']
            top = element_memory.location['y']
            right = element_memory.location['x'] + element_memory.size['width']
            bottom = element_memory.location['y'] + element_memory.size['height']
            im = Image.open(view_path + '\\viewSW.png')
            im = im.crop((left, top, right, bottom))
            im.save(view_path + '\\view_memory.png')
            api_key = "fLYyaSUX2fP4GdPRxqprPGFU"
            secret_key = "YFIBCjMSVt7OaeIrnTq5aGDaqVPRvsol"
            access_token2 = self.operate.get_token(api_key, secret_key)
            w = self.operate.recognition_word_high(view_path, '\\view_memory.png', access_token2)
            val_memory = w['words_result'][0]['words'].split('.')[0]
            print val_memory
            # CPU图片截图
            left = element_cpu.location['x']
            top = element_cpu.location['y']
            right = element_cpu.location['x'] + element_memory.size['width']
            bottom = element_cpu.location['y'] + element_memory.size['height']
            im = Image.open(view_path + '\\viewSW.png')
            im = im.crop((left, top, right, bottom))
            im.save(view_path + '\\view_cpu.png')
            api_key = "fLYyaSUX2fP4GdPRxqprPGFU"
            secret_key = "YFIBCjMSVt7OaeIrnTq5aGDaqVPRvsol"
            access_token2 = self.operate.get_token(api_key, secret_key)
            recognition_word_high = self.operate.recognition_word_high(view_path, '\\view_cpu.png', access_token2)
            val_cpu = recognition_word_high['words_result'][0]['words'].split('.')[0]
            print val_cpu
            self.assertIn(int(val_memory), range(1, 90))
            self.assertIn(int(val_cpu), range(1, 90))
        finally:
            self.operate.click_elem(add_device_device_info_close)




    
    # def test06_SW_restart(self):
    #     """验证交换机能成功重启"""
    #     time.sleep(5)
    #     self.operate.click_elem(add_device_monitoring)
    #     self.operate.click_elem(add_device_switch)
    #     time.sleep(5)
    #     self.operate.click_elem(sw_select)
    #     self.operate.click_elem(sw_more)
    #     self.operate.click_elem(sw_restart)
    #     self.operate.click_elem(key_OK)
    #     self.operate.click_elem(device_sw_list_refresh)
    #     time.sleep(10)
    #     text_offline = self.operate.find_elem(device_sw_list_tr1_state).text
    #     try:
    #         self.operate.find_elem(add_device_online_sw, By.XPATH, 300)
    #     except Exception as e:
    #         print (e)
    #     else:
    #         self.assertNotEqual(text_offline, 'Online')


    def test07_SW_diagnosis_tool(self):
        """验证SW诊断工具可用"""
        time.sleep(5)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_switch)
        time.sleep(5)
        self.operate.click_elem(sw_select)
        self.operate.click_elem(sw_more)
        self.operate.click_elem(sw_diagnosis)
        js1 = 'return $("#cli_result").val();'
        n = 1
        while n < 4:
            self.operate.click_elem(device_running_version)
            time.sleep(30)
            text_version = self.driver.execute_script(js1)
            f = open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+')
            f.write(text_version)
            f.seek(0, 0)
            text = f.read()
            f.close()
            if re.search('System', text) is None:
                print (u'交换机命令行第' + str(n) + u'次返回失败')
                time.sleep(30)
                n += 1
            else:
                print (u"交换机命令行返回成功")
                break
        self.operate.click_elem(device_diagnosis_close)
        t = re.search("System", text)
        self.assertIsNotNone(t)

    def test09_sw_setting_vlan(self):
        """验证下发vlan"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_switch)
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
        time.sleep(40)
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
        # self.operate.click_elem(device_sw_detail_vlan_page_last)
        self.operate.click_elem(device_sw_detail_vlan_delete.format(sw_vlan_id_input))
        self.operate.click_elem(key_OK)
        time.sleep(5)
        self.operate.click_elem(add_device_device_info_close)
        # 断言
        t = re.search('VLAN' + sw_vlan_id_input, text)
        if t is None:
            print text
        self.assertIsNotNone(t)

    def test10_sw_setting_port(self):
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
        time.sleep(15)
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
        self.operate.elem_clear_send_keys(device_sw_detail_int_accesss_vlan_id, '1')
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



    # def test19_sw_setting_device_name(self):
    #     """验证下发设备别名"""
    #     t = re.search('hostname ' + device_input_alias_data, text)
    #     if t is None:
    #         print text
    #     self.assertIsNotNone(t)

    def test20_SW_move(self):
        """验证SW可成功移动分组"""
        time.sleep(5)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_switch)
        self.operate.click_elem(add_device_switch)
        time.sleep(5)
        self.operate.click_elem(sw_select)
        self.operate.click_elem(sw_more)
        self.operate.click_elem(device_sw_move)
        self.operate.click_elem(device_move_first_group)
        self.operate.click_elem(device_move_confirm)
        self.operate.click_elem(key_OK)
        time.sleep(5)
        sw_tr = self.operate.find_elem(device_sw_list_tr).text
        self.assertEqual(sw_tr, 'No matching records found')

    def test21_SW_delete(self):
        """验证SW可成功删除"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_switch)
        time.sleep(15)
        self.operate.click_elem(add_device_add_switch)
        time.sleep(5)
        self.operate.click_elem(add_device_alert_add_access_point)
        self.operate.elem_send_keys(add_device_alert_sn_switch, add_device_alert_input_sn_switch)
        self.operate.click_elem(add_device_alert_save_switch)
        time.sleep(10)
        self.operate.click_elem(sw_select)
        self.operate.click_elem(sw_more)
        self.operate.click_elem(device_delete)
        self.operate.click_elem(key_OK)
        time.sleep(10)
        sw_tr = self.operate.find_elem(device_sw_list_tr).text
        self.assertEqual(sw_tr, 'No matching records found')


if __name__ == '__main__':
    unittest.main()