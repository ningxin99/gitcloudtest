# coding:utf-8
"""
@author: Tracy
@mail: wanghongyu@ruijie.com.cn
@date: 2019.07.09
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


class DeviceEg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Pyse("chrome")
        Login(cls.driver, user_cloud_local, password_cloud_local, login_url_local).login()
        cls.operate = ComFunction(cls.driver)
        group_name = AddGroup(cls.driver).add_group()
        cls.group_name = group_name

        # LJM-0823
        # cls.operate.click_elem(add_device_monitoring)
        # cls.operate.click_elem(add_device_gateway)
        # cls.operate.click_elem(add_device_gateway)
        #
        # cls.group_name = cls.operate.find_elem('//*[@id="gateway_table"]/tbody/tr[1]/td[8]').text
        # time.sleep(2)
        # cls.operate.click_elem(configuration_page_xpath)
        # cls.operate.click_elem(groups_page_xpath)
        # time.sleep(10)
        # cls.operate.click_elem(select_group_xpath.format(cls.group_name))
        # cls.operate.click_elem(select_setting_btn_xpath)
        # time.sleep(5)



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test01_eg_list(self):
        """验证添加设备流程"""
        print (self.group_name)
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        time.sleep(15)
        self.operate.click_elem(add_device_add_gateway)
        time.sleep(5)
        self.operate.elem_send_keys(add_device_alert_sn_gateway, add_device_alert_input_sn_gateway)
        self.operate.elem_send_keys(add_device_alert_eg_alias, device_input_alias_data)
        self.operate.elem_send_keys(add_device_alert_password, 'ruijie123')
        self.operate.click_elem(add_device_alert_save_gateway)
        time.sleep(20)
        # eg_sn = self.operate.find_elem(device_eg_un_sn).text
        # eg_alias = self.operate.find_elem(device_eg_un_alias).text
        # eg_group = self.operate.find_elem(device_eg_un_group).text
        # print (eg_sn)
        # print (eg_alias)
        # print (eg_group)
        # print (self.group_name)
        # if eg_sn == add_device_alert_input_sn_gateway and eg_alias == 'EG123' and eg_group == self.group_name:
        #     k = 1
        # else:
        #     k = 0
        # self.assertEqual(k, 1)

    # def test02_eg_auth(self):
    #     """验证eg可重新认证并上线"""
    #     self.operate.click_elem(add_device_monitoring)
    #     self.operate.click_elem(add_device_gateway)
    #     self.operate.click_elem(device_eg_re_auth)
    #     self.operate.elem_send_keys(device_eg_re_password, add_device_alert_input_password)
    #     self.operate.click_elem(key_OK)
    #     time.sleep(10)
    #     try:
    #         self.operate.find_elem(add_device_online_eg, By.XPATH, 600)
    #     except:
    #         self.assertIsNotNone(None, u'EG重新认证失败')
    #
    # def test03_eg_alias(self):
    #     """验证可eg可成功修改别名"""
    #     self.operate.click_elem(add_device_monitoring)
    #     self.operate.click_elem(add_device_gateway)
    #     self.operate.click_elem(device_eg_list_alias)
    #     self.operate.elem_clear_send_keys(device_eg_list_alias_input, 'Test1')
    #     self.operate.click_elem(device_eg_list_alias_input_confirm)
    #     self.assertEqual(self.operate.find_elem(device_eg_list_alias).text, 'Test1')

    def test04_eg_online(self):
        """验证eg是否在线"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        try:
            self.assertIsNotNone(self.operate.find_elem(add_device_online_eg, By.XPATH, 600), u"10min内EG上线失败")
        except:
            self.assertIsNotNone(None, u"10min内EG上线失败")
        else:
            print (u'EG上线')



    # def test01(self):
    #     """调试代码"""
    #     # 调试代码
    #     time.sleep(15)
    #     self.operate.click_elem(login_close_tips_xpath)
    #     self.operate.click_elem(configuration_page_xpath)  # 没有等60s
    #     self.operate.click_elem(configuration_basic_xpath)
    #     time.sleep(15)
    #     self.operate.click_elem(add_device_monitoring)
    #     self.operate.click_elem(add_device_access_point)
    #     # 调试代码


    def test05_eg_basic(self):
        """验证eg的basic信息正确"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        self.operate.click_elem(add_device_eg_info.format(add_device_alert_input_sn_gateway))
        self.operate.click_elem(device_eg_diagnosis_tool)
        js1 = 'return $("#cli_result").val();'
        n = 1
        while n < 4:
            self.operate.click_elem(device_running_version)
            time.sleep(30)
            text_version = self.driver.execute_script(js1)
            time.sleep(20)
            with open(os.path.join(CONFIG_PATH, 'cmd.text'), 'w+') as f:
                f.write(text_version)
                f.seek(0, 0)
                text = f.read()
            if re.search('System description', text) is None:
                print (u'EG version 命令行第' + str(n) + u'次返回失败')
                time.sleep(20)
                n += 1
            else:
                print(u"EG version 命令行返回成功")
                break
        time.sleep(10)
        self.operate.click_elem(device_eg_diagnosis_tool_close)
        model_text_eg = self.operate.find_elem(add_device_EG_info_model).text
        version_text_eg = self.operate.find_elem(add_device_EG_info_version).text
        sn_text_eg = self.operate.find_elem(add_device_EG_info_SN).text
        # 关闭详情页面
        self.operate.click_elem(add_device_device_info_close)
        print model_text_eg,version_text_eg,string_escape(version_text_eg),sn_text_eg
        print text
        t = re.search(model_text_eg + '[\S\s]*' + string_escape(version_text_eg) + '[\S\s]*' + sn_text_eg, text)
        self.assertIsNotNone(t)

    def test06_eg_cpu(self):
        """验证有eg的CPU和memory信息"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        self.operate.click_elem(add_device_eg_info.format(add_device_alert_input_sn_gateway))
        time.sleep(2)
        view_path = self.operate.save_screen_shot('viewEG')
        val_memory = 0
        val_cpu = 0
        try:
            element_cpu = self.operate.find_elem(device_eg_detail_cpu)
            element_memory = self.operate.find_elem(device_eg_detail_memory)
            self.operate.find_elem(device_eg_detail_rate_summary)
        except:
            print ("cpu/memory无数据")
            self.assertIsNotNone(None, u"cpu/memory无数据")
        else:
            # mmeory图片截图
            print ('mmeory图片截图')
            left = element_memory.location['x']
            top = element_memory.location['y']
            right = element_memory.location['x'] + element_memory.size['width']
            bottom = element_memory.location['y'] + element_memory.size['height']
            im = Image.open(view_path + '//viewEG.png')
            im = im.crop((left, top, right, bottom))
            im.save(view_path + '\\view_memory.png')
            api_key = "fLYyaSUX2fP4GdPRxqprPGFU"
            secret_key = "YFIBCjMSVt7OaeIrnTq5aGDaqVPRvsol"
            access_token2 = self.operate.get_token(api_key, secret_key)
            w = self.operate.recognition_word_high(view_path, '\\view_memory.png', access_token2)
            print w
            val_memory = w['words_result'][0]['words'].split('.')[0]
            print val_memory
            # CPU图片截图
            # print ('CPU图片截图')
            left = element_cpu.location['x']
            top = element_cpu.location['y']
            right = element_cpu.location['x'] + element_memory.size['width']
            bottom = element_cpu.location['y'] + element_memory.size['height']
            im = Image.open(view_path + '//viewEG.png')
            im = im.crop((left, top, right, bottom))
            im.save(view_path + '\\view_cpu.png')
            api_key = "fLYyaSUX2fP4GdPRxqprPGFU"
            secret_key = "YFIBCjMSVt7OaeIrnTq5aGDaqVPRvsol"
            access_token2 = self.operate.get_token(api_key, secret_key)
            recognition_word_high = self.operate.recognition_word_high(view_path, '\\view_cpu.png', access_token2)
            print (recognition_word_high)
            val_cpu = recognition_word_high['words_result'][0]['words'].split('.')[0]
            print val_cpu
        finally:
            self.operate.click_elem(add_device_device_info_close)
            self.assertIn(int(val_memory), range(1, 90))
            self.assertIn(int(val_cpu), range(1, 90))

    def test07_eg_traffic(self):
        """验证eg的Top 10 Applications/users by Traffic图表有数据，无法验证数据的正确性"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        self.operate.click_elem(add_device_eg_info.format(add_device_alert_input_sn_gateway))
        try:
            self.operate.find_elems(device_eg_list_application)
            self.operate.find_elems(device_eg_list_users)
        except:
            self.assertIsNotNone(None, u"Top 10 Applications/users by Traffic图表无数据")
        self.operate.click_elem(add_device_device_info_close)


    def test08_eg_log(self):
        """验证是否有日志信息，无法验证日志信息的正确性"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        self.operate.click_elem(add_device_eg_info.format(add_device_alert_input_sn_gateway))
        try:
            self.operate.find_elems(device_eg_list_log_tr)
        except:
            self.assertIsNotNone(None, u"EG无日志信息")
        finally:
            self.operate.click_elem(add_device_device_info_close)


    def test09_eg_eweb(self):
        """验证可访问EG 的EWEB"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        self.operate.click_elem(add_device_eg_info.format(add_device_alert_input_sn_gateway))
        # cloud_hand = self.driver.current_window_handle
        self.operate.click_elem(device_eg_EWEB)
        flag = 1
        t = ''
        try:
            self.operate.find_elem(device_eg_EWEB_logo_success, By.XPATH, 300)
        except Exception as e:
            print e
            flag = 0
            t = self.operate.find_elem(devic_eg_EWEb_fail).text
        else:
            print(u'EG web页面打开')
            handles = self.driver.window_handles
            self.driver.switch_to_window(handles[-1])
            try:
                self.operate.find_elem(device_eg_EWEB_element, By.XPATH, 300)
            except Exception as e:
                try:
                    self.operate.find_elem(device_eg_EWEB_login_element)
                except:
                    flag = 0
        finally:
            if 'fail' in t:
                self.assertIsNotNone(None, u" Tunnel creation failed")
            time.sleep(5)
            handles = self.driver.window_handles
            self.driver.switch_to_window(handles[0])
            self.operate.click_elem(device_eg_diagnosis_tool_close)
            self.operate.click_elem(add_device_device_info_close)
            self.assertNotEqual(flag, 0, u'time out')

    def test10_eg_telnet(self):
        """验证可telnet到EG"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        self.operate.click_elem(add_device_eg_info.format(add_device_alert_input_sn_gateway))
        self.operate.click_elem(device_eg_telnet)
        flag = 1
        try:
            self.operate.find_elem(device_eg_telnet_success, By.XPATH, 300)
        except Exception as ee:
            print ee
            flag = 0
        else:
            print (u'telnet成功')
        finally:
            self.operate.click_elem(device_eg_diagnosis_tool_close)
            self.operate.click_elem(add_device_device_info_close)
            self.assertNotEqual(flag, 0)

    def test11_eg_SSH(self):
        """验证可通过SSH连接EG"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        self.operate.click_elem(add_device_eg_info.format(add_device_alert_input_sn_gateway))
        self.operate.click_elem(device_eg_detail_more)
        self.operate.click_elem(device_eg_ssh)
        t = 'fail'
        try:
            t = self.operate.find_elem(device_eg_ssh_content, by=By.XPATH, wait_times=300).text
        except Exception as e:
            self.assertIn('succeeded', t, u"SSH连接失败或SSH服务未开启")
        finally:
            self.operate.click_elem(device_eg_ssh_close)
            self.operate.click_elem(add_device_device_info_close)



    def test12_eg_diagnosis_tool(self):
        """验证EG的诊断工具可用,CWMP保活时间下发,下发设备别名"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        self.operate.click_elem(add_device_eg_info.format(add_device_alert_input_sn_gateway))
        self.operate.click_elem(device_eg_diagnosis_tool )
        js1 = 'return $("#cli_result").val();'
        n = 1
        while n < 4:
            self.operate.click_elem(device_running_config)
            time.sleep(10)
            text_running = self.driver.execute_script(js1)
            time.sleep(10)
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
        self.operate.click_elem(device_eg_diagnosis_close)
        self.operate.click_elem(add_device_device_info_close)
        # 验证CWMP保活时间下发
        t = re.search('cwmp' + '[^!]*' + 'cpe inform interval 180', text)
        self.assertIsNotNone(t)
        # 验证下发设备别名
        t = re.search('hostname ' + device_input_alias_data, text)
        self.assertIsNotNone(t)



    '''
    def test12_eg_restart(self):
        """验证EG可成功重启"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        self.operate.click_elem(add_device_eg_info.format(add_device_alert_input_sn_gateway))
        self.operate.click_elem(device_eg_detail_more)
        self.operate.click_elem(device_eg_restart)
        self.operate.click_elem(key_OK)
        self.operate.click_elem(add_device_device_info_close)
        time.sleep(10)
        self.operate.click_elem(device_list_refresh)
        text_offline = self.operate.find_elem(eg_list_tr1_state).text
        try:
            self.operate.find_elem(add_device_online_eg, By.XPATH, 300)
        except Exception as e:
            print (e)
        else:
            self.assertNotEqual(text_offline, 'Online')
    '''
    def test13_eg_edit(self):
        """验证EG详情页面的描述信息可进行编辑"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        self.operate.click_elem(add_device_eg_info.format(add_device_alert_input_sn_gateway))
        self.operate.click_elem(device_eg_detail_alias_edit)
        self.operate.elem_clear_send_keys(device_eg_detail_alias_input, 'EG')
        self.operate.click_elem(device_eg_detail_alias_ok)
        self.operate.click_elem(device_eg_detail_des_edit)
        self.operate.elem_clear_send_keys(device_eg_detail_des_input, 'abc')
        self.operate.click_elem(device_eg_detail_des_ok)
        eg_alias = self.operate.find_elem(device_eg_detail_alias).text
        eg_des = self.operate.find_elem(device_eg_detail_des).text
        if eg_alias == 'EG' and eg_des == 'abc':
            flag = 1
        else:
            flag = 0
        self.operate.click_elem(add_device_device_info_close)
        self.assertEqual(flag, 1)

    def test14_eg_password_edit(self):
        """验证可成功修改EG web 密码"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        self.operate.click_elem(add_device_eg_info.format(add_device_alert_input_sn_gateway))
        self.operate.click_elem(device_eg_detail_password)
        self.operate.elem_send_keys(device_eg_detail_password_input, 'ruijie123')
        self.operate.click_elem(device_eg_detail_password_ok)
        self.operate.click_elem(add_device_device_info_close)
        self.operate.click_elem(maintenance)
        self.operate.click_elem(view_log_operation_log)
        for i in range(100):
            time.sleep(60)
            log_des = self.operate.find_elem(device_eg_operation_log_des).text
            log_result = self.operate.find_elem(device_eg_operation_log_result).text
            self.operate.click_elem(device_eg_operation_log_refresh)
            if 'password' in log_des:
                break
        self.assertEqual(log_result, 'Success')

    def test15_eg_delete(self):
        """验证EG可成功删除"""
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_gateway)
        time.sleep(15)
        self.operate.click_elem(eg_select)
        self.operate.click_elem(eg_more)
        self.operate.click_elem(eg_delete)
        self.operate.click_elem(key_OK)
        time.sleep(5)
        eg_tr = self.operate.find_elem(device_eg_list_tr).text
        self.assertEqual(eg_tr, 'No matching records found')








if __name__ == '__main__':
    unittest.main()

















