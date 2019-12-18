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
from Data.device_data import *
from PIL import Image


class DeviceAp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Pyse("chrome")
        Login(cls.driver, user_cloud_local, password_cloud_local, url=login_url_local).login()
        cls.operate = ComFunction(cls.driver)
        cls.group_name = AddGroup(cls.driver, device_sn={'ap': add_device_alert_input_sn}).add_group()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test01_ap_alias(self):
        """验证AP别名可修改成功"""
        print (self.group_name)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        self.operate.click_elem(device_alias)
        self.operate.elem_clear_send_keys(device_alias_input, device_ap_input_alias_data)
        self.operate.click_elem(device_alias_input_confirm)
        ap_alias = self.operate.find_elem(device_alias).text
        time.sleep(5)
        self.assertEqual(ap_alias, device_ap_input_alias_data)

    def test01_check_online_AP(self):
        """验证AP在线，配置同步"""
        time.sleep(15)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        try:
            self.operate.find_elem(add_device_online_ap, By.XPATH, 600)
        except Exception as e:
            print e
            self.assertIsNotNone(None, u"10min中内，AP上线失败")
        else:
            time_ap_online = time.time()
            while True:
                time.sleep(10)
                self.operate.click_elem(device_list_refresh)
                time.sleep(10)
                state_ap = self.operate.find_elem(add_device_state).text
                if state_ap == 'Synced':
                    print(u"AP配置同步成功")
                    time_ap_Synced = time.time()
                    t = int((time_ap_Synced - time_ap_online) / 60)
                    break
                elif state_ap == 'Sync Failed':
                    t = 1
                    break
            if state_ap == 'Sync Failed':
                self.assertIsNotNone(None, u"AP同步配置失败")
            self.assertIn(t, range(11), u'AP同步配置超时')

    def test02_ap_deliver(self):
        """验证AP配置可重新下发"""
        time.sleep(1)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        self.operate.click_elem(device_list_refresh)
        try:
            self.operate.find_elems(add_device_online_ap)
            self.operate.find_elem(add_device_synced)
        except Exception as e:
            print (e)
            self.assertIsNotNone(None, u"AP上线或同步配置失败")
        else:
            self.operate.click_elem(add_device_syned)
            self.operate.click_elem(device_config_manually_deliver)
            self.operate.click_elem(key_OK)
            time.sleep(5)
            self.operate.click_elem(device_config_manually_deliver)
            self.operate.click_elem(key_OK)
            time.sleep(5)
            self.operate.click_elem(device_config_manually_deliver)
            self.operate.click_elem(key_OK)
            time.sleep(5)
            if self.operate.find_elem(device_config_state).text == "Not Synced":
                self.operate.click_elem(device_config_state_page_close)

            # Ljm_2019-0809
            while True:
                time.sleep(10)
                self.operate.click_elem(device_list_refresh)
                time.sleep(10)
                state_ap = self.operate.find_elem(add_device_state).text
                if state_ap == 'Synced':
                    print(u"AP配置重新下发成功")
                    break
                elif state_ap == 'Sync Failed':
                    break
            if state_ap == 'Sync Failed':
                self.assertIsNotNone(None, u"AP同步配置失败")

    def test03_ap_log(self):
        """验证设备详情中设备日志信息存在"""
        time.sleep(1)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        time.sleep(5)
        self.operate.click_elem(add_device_device_info.format(add_device_alert_input_sn))
        try:
            self.operate.find_elems(add_device_log_list)
        except Exception as e:
            print (e)
            self.assertIsNotNone(None, u'没有设备日志信息存在')
        finally:
            self.operate.click_elem(add_device_device_info_close)

    def test04_ap_detail_cpu(self):
        """验证设备详情cpu/memory/traffic 信息是否有值，不验证其正确性"""
        time.sleep(1)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        time.sleep(2)
        self.operate.click_elem(add_device_device_info.format(add_device_alert_input_sn))
        time.sleep(2)
        view_path = self.operate.save_screen_shot('viewAP')
        try:
            element_memory = self.operate.find_elem(device_ap_detail_memory)
            element_cpu = self.operate.find_elem(device_ap_detail_cpu)
            self.operate.find_elem(device_ap_detail_traffic)
        except:
            self.assertIsNotNone(None, u'cpu/memory/traffic信息不存在')
        else:
            # mmeory图片截图
            left = element_memory.location['x']
            top = element_memory.location['y']
            right = element_memory.location['x'] + element_memory.size['width']
            bottom = element_memory.location['y'] + element_memory.size['height']
            im = Image.open(view_path + '\\viewAP.png')
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
            im = Image.open(view_path + '\\viewAP.png')
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

    def test04_ap_detail_version(self):
        """验证设备详情version信息与命令行一致，version信息：SN，model，hardware，version"""
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
                print (u'AP version 命令行第' + str(n) + u'次返回失败')
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
        self.assertIsNotNone(version, u"AP详情验证不成功")
        self.assertIsNotNone(model, u"AP详情验证不成功")
        self.assertIsNotNone(sn, u"AP详情验证不成功")
        self.assertIsNotNone(hardware, u"AP详情验证不成功")

    def test05_ap_detail_radio(self):
        """验证设备详情中radio信息与命令行一致，radio信息：带宽，信道"""
        time.sleep(2)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        self.operate.click_elem(add_device_device_info.format(add_device_alert_input_sn))
        channel_5_ap_text = self.operate.find_elem(add_device_device_info_channel_5G).text
        bandwidth_5_ap_text = self.operate.find_elem(add_device_device_info_bandwidth_5G).text
        channel_2_ap_text = self.operate.find_elem(add_device_device_info_channel_2).text
        bandwidth_2_ap_text = self.operate.find_elem(add_device_device_info_bandwidth_2).text
        print channel_5_ap_text
        print bandwidth_5_ap_text
        print channel_2_ap_text
        print bandwidth_2_ap_text
        # 关闭
        self.operate.click_elem(add_device_device_info_close)
        # 打开命令行
        self.operate.click_elem(device_more)
        self.operate.click_elem(device_diagnosis)
        js1 = 'return $("#cli_result").val();'
        n = 1
        while n < 4:
            self.operate.click_elem(device_running_config)
            time.sleep(30)
            text_radio = self.driver.execute_script(js1)
            time.sleep(20)
            with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                # f.truncate()
                # f.write(text_running)
                f.write(text_radio)
                f.seek(0, 0)
                text = f.read()
            if re.search('!', text) is None:
                print (u'AP version 命令行第' + str(n) + u'次返回失败')
                time.sleep(20)
                n += 1
            else:
                print(u"AP version 命令行返回成功")
                break
        self.operate.click_elem(device_diagnosis_close)
        # 验证AP basic信息
        channel_5_ap = re.search(" channel " + channel_5_ap_text + '[\S\s]*', text)
        bandwidth_5_ap = re.search(" chan-width " + bandwidth_5_ap_text + '[\S\s]*', text)
        channel_2_ap = re.search(" channel " + channel_2_ap_text + '[\S\s]*', text)
        bandwidth_2_ap = re.search(" chan-width " + bandwidth_2_ap_text + '[\S\s]*', text)
        self.assertIsNotNone(channel_5_ap, u"AP5G信道验证不成功")
        self.assertIsNotNone(bandwidth_5_ap, u"AP5G带宽验证不成功")
        self.assertIsNotNone(channel_2_ap, u"AP2.4G信道验证不成功")
        self.assertIsNotNone(bandwidth_2_ap, u"AP2.4G带宽验证不成功")

    def test06_ap_restart(self):
        """验证AP能成功重启"""
        time.sleep(5)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        self.operate.click_elem(add_device_access_point)
        time.sleep(5)
        self.operate.click_elem(device_select)
        self.operate.click_elem(device_more)
        self.operate.click_elem(device_restart)
        self.operate.click_elem(key_OK)
        time.sleep(10)
        self.operate.click_elem(device_list_refresh)
        time.sleep(10)
        text_offline = self.operate.find_elem(device_list_tr1_state).text
        try:
            self.operate.find_elem(add_device_online_ap, By.XPATH, 300)
        except Exception as e:
            print (e)
        else:
            self.assertNotEqual(text_offline, 'Online')

    def test07_ap_diagnosis_tool(self):
        """验证可打开AP诊断工具"""
        time.sleep(5)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        self.operate.click_elem(add_device_access_point)
        time.sleep(5)
        self.operate.click_elem(device_select)
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
                f.write(text_running)
                f.seek(0, 0)
                text = f.read()
            if re.search('!', text) is None:
                print (u'AP running 命令行第' + str(n) + u'次返回失败')
                # time.sleep(20)
                n += 1
            else:
                print (u"AP running 命令行返回成功")
                break
        self.operate.click_elem(device_diagnosis_close)
        t = re.search('!', text)
        self.assertIsNotNone(t, u'AP命令行返回不成功')

    def test08_ap_move(self):
        """验证AP可成功移动分组"""
        time.sleep(5)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        self.operate.click_elem(add_device_access_point)
        time.sleep(5)
        self.operate.click_elem(device_select)
        self.operate.click_elem(device_more)
        self.operate.click_elem(device_move)
        time.sleep(2)
        self.operate.click_elem(device_move_first_group)
        self.operate.click_elem(device_move_confirm)
        self.operate.click_elem(key_OK)
        time.sleep(5)
        ap_tr = self.operate.find_elem(device_list_tr).text
        self.assertEqual(ap_tr, 'No matching records found')

    def test09_ap_delete(self):
        """验证AP可成功删除"""
        time.sleep(5)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        self.operate.click_elem(add_device_access_point)
        time.sleep(15)
        self.operate.click_elem(add_device_add_access_point)
        time.sleep(5)
        self.operate.click_elem(add_device_alert_add_access_point)
        self.operate.elem_send_keys(add_device_alert_sn, add_device_alert_input_sn)
        self.operate.click_elem(add_device_alert_save)
        time.sleep(10)
        self.operate.click_elem(device_select)
        self.operate.click_elem(device_more)
        self.operate.click_elem(device_delete)
        self.operate.click_elem(key_OK)
        time.sleep(5)
        ap_tr = self.operate.find_elem(device_list_tr).text
        self.assertEqual(ap_tr, 'No matching records found')


if __name__ == '__main__':
    unittest.main()














