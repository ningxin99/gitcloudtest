# coding:utf-8
"""
@author: Tracy
@mail: wanghongyu@ruijie.com.cn
@date: 2019.05.15
"""
from selenium import webdriver
from Common.com_function import *
from Data.basic_data import *
from Page.basic_page import *
import datetime


class OperateAddssid(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.operate = ComFunction(self.driver)

    def login(self):
        # 登陆
        self.driver.get("https://cloud-as.ruijienetworks.com")
        self.operate.elem_send_keys(user_name_xpath, login_user_name_data)
        self.operate.elem_send_keys(password_xpath, login_password_data)
        self.operate.click_elem(login_btn_xpath)
        # 关闭提示
        # self.operate.click_elem(login_close_tips_xpath, By.XPATH, 300)

    def add_ssid(self, add_ssid_name_custom):
        # configuration/basic
        time.sleep(60)
        self.operate.click_elem(configuration_page_xpath)# 没有等60s
        self.operate.click_elem(configuration_basic_xpath)
        # 初始化分组为空一个SSID，一个设备，添加SSID
        time.sleep(60)
        self.operate.click_elem(delet_SSID_config)
        self.operate.click_elem(delet_SSID_confirm)
        self.operate.click_elem(add_group_xpath)
        self.operate.elem_send_keys(add_SSID_name, add_ssid_name_custom)
        self.operate.click_elem(add_SSID_save_ssid)
        # 配置安全密码
        # self.operate.click_elem(add_SSID_security)
        # self.operate.elem_send_keys(add_SSID_security_web_password, add_SSID_web_password)
        # self.operate.elem_send_keys(add_SSID_security_telnet_password, add_SSID_telnet_password)
        # 保存
        self.operate.click_elem(add_SSID_save)
        now_time_start = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print ('SSID:'+add_ssid_name_custom + ' start config ,   the start time is' + now_time_start)
        time.sleep(40)


    def check_ssid(self, ssid_name_custom):
        # monitoring/access point
        self.operate.click_elem(add_device_monitoring)
        self.operate.click_elem(add_device_access_point)
        # time.sleep(70)
        print ('the state of device is Syncing or not Synced,please wait!')
        try:
            if self.operate.find_elems(add_device_online, By.XPATH, 600) != 0 and self.operate.find_elem(add_device_synced, By.XPATH, 2400) != 0:
                self.operate.click_elem(add_device_device_info.format(add_device_alert_input_sn))
                now_time_end = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print ('configuration synchronized end,the end time is' + now_time_end)
                # print ((now_time_end-now_time_start).days)
        except:
            print ("SSID config lose in 40 mins")
            self.operate.click_elem(view_log_maintenance)
            self.operate.click_elem(view_log_config_log)
            print ('config log start time is'+self.operate.find_elem(view_log_config_log_start_time).text)
            print ('config log end time is'+self.operate.find_elem(view_log_config_log_end_time).text)
            print ('\n')
        else:
            try:
                ssid_text = self.operate.find_elem(add_device_device_info_SSID, By.XPATH, 10).text
            except:
                self.operate.click_elem(add_device_device_info_close)
                print ('did not get the ssid name')
            else:
                if ssid_text == ssid_name_custom:
                    print ('SSID:' + ssid_text + " config complete successful")
                    print('\n')
                self.operate.click_elem(add_device_device_info_close)






if __name__ == '__main__':
    basic = OperateAddssid()
    basic.login()
    i = 1
    while i < ssid_num:
        basic.add_ssid("auto"+str(i))
        basic.check_ssid("auto"+str(i))
        i += 1


















