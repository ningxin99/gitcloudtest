# coding=utf-8
"""
@author: zhouxihong
@mail: zhouxihong@ruijie.com.cn
@date: 2019.04.29
"""
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Common.brower import Browser
import time
from config import *
from Data.basic_data import *
import sys
import urllib
import urllib2
import base64
import json
import re
class ComFunction(object):
    """
    封装一些用来常规操作的方法
    """

    # def __init__(self, comfunction=None, browser_type='chrome'):
    #     if comfunction:
    #         self.driver = comfunction.driver
    #     else:
    #         super(ComFunction, self).__init__(browser_type=browser_type)

            

    def __init__(self, driver):
        self.driver = driver  # webdriver.Chrome()

    def __del__(self):
        pass

    # def elem_wait(self, locator, by=By.XPATH, wait_times=60):
    #     """
    #     等待元素可见
    #     :param locator: 定位方式 - 一般采用xpath
    #     :param by: 用来标识是通过什么方式定位
    #     :param wait_times: 最长等待时间
    #     :return:
    #     """
    #     WebDriverWait(self.driver, wait_times).until(ec.visibility_of_element_located((by, locator)))

    def elem_wait(self, locator, by=By.XPATH, wait_times=60):
        """
        等待元素可见
        :param locator: 定位方式 - 一般采用xpath
        :param by: 用来标识是通过什么方式定位
        :param wait_times: 最长等待时间
        :return:
        """
        try:
            WebDriverWait(self.driver, wait_times).until(ec.visibility_of_element_located((by, locator)))
        except Exception as e:
            self.save_screen_shot()
            raise e







    def elem_wait_click(self, locator, by=By.XPATH, wait_times=60):
        """
        等待元素可点击
        :param locator: 定位方式 - 一般采用xpah
        :param by: 用来表示是通过什么方式定位
        :param wait_times: 最长等待时间
        :return:
        """
        try:
            WebDriverWait(self.driver, wait_times).until(ec.element_to_be_clickable((by, locator)))
        except Exception as e:
            self.save_screen_shot()
            raise e



    def elem_presence_wait(self, locator, by=By.XPATH, wait_times=60):
        """
        等待元素出现在标签上
        :param locator: 定位方式 - 一般采用xpath
        :param by: 要用来表示通过什么方式定位
        :param wait_times: 最长等待时间
        :return:
        """
        WebDriverWait(self.driver, wait_times).until(ec.presence_of_element_located((by, locator)))

    def find_elem(self, locator, by=By.XPATH, wait_times=60):
        """
        单个元素查找方法
        :param locator: 定位方式 - 一般采用xpath
        :param by: 用来标识是通过什么方式定位
        :param wait_times: 最长等待时间
        :return: 返回元素
        """
        self.elem_wait(locator, by, wait_times)
        time.sleep(0.8)
        ele = self.driver.find_element(by, locator)
        return ele


    def click_elem(self, locator, by=By.XPATH, wait_times=60):
        """
        单个元素点击方法
        :param locator: 定位方式 - 一般采用xpath
        :param by: 用来表示是通过什么方式定位
        :param wait_times: 最长等待时间
        :return:
        """
        self.elem_wait_click(locator, by, wait_times)
        time.sleep(0.5)
        ele = self.driver.find_element(by, locator)
        ele.click()

    def elem_send_keys(self, locator, keys, by=By.XPATH, wait_times=60):
        """
        对元素发送信息
        :param locator: xpath定位符
        :param keys: 输入的字符
        :param by: 通过什么方式定位
        :param wait_times: 等待时间
        :return:
        """
        # 原代码
        # self.find_elem(locator, by, wait_times).send_keys(keys)
        self.elem_wait(locator, by, wait_times)
        time.sleep(0.8)
        self.driver.find_element(by, locator).send_keys(keys)


    def elem_clear_send_keys(self, locator, keys, by=By.XPATH, wait_times=60):
        # 原代码
        # self.find_elem(locator, by, wait_times).clear()
        # self.find_elem(locator, by, wait_times).send_keys(keys)
        self.elem_wait(locator, by, wait_times)
        time.sleep(0.8)
        ele = self.driver.find_element(by, locator)
        ele.clear()
        ele.send_keys(keys)


    def find_elems(self, locator, by=By.XPATH, wait_times=60):
        """
        一类元素查找方法
        :param locator: 定位方式 - 一般采用xpath
        :param by: 用来标识是通过什么方式定位
        :param wait_times: 最长等待时间
        :return: 返回一类元素
        """
        self.elem_wait(locator, by, wait_times)
        time.sleep(0.8)
        eles = self.driver.find_elements(by, locator)
        return eles

    def get_url(self):
        """
        获取当前url
        :return: 返回url
        """
        return self.driver.current_url

    def get_text(self, xpath):
        """
        获取当前文字信息
        :return:
        """
        el = self.find_elem(xpath)
        return el.text


    def switch_to_iframe(self, locator):
        """
        切换iframe
        :param locator: 定位方式
        :return:
        """
        self.driver.switch_to.frame(locator)

    def back_current_page(self):
        """
        返回到当前页面
        :return:
        """
        self.driver.switch_to.default_content()

    def get_driver(self):
        return self.driver


    def assert_text(self, actual_el, expect_result, msg=None):
        """
        当前元素的文字信息是否与预期一致
        :param actual_el:实际存在的元素
        :param expect_result:预期的该元素中的文字信息
        :return:
        """
        if actual_el is None or expect_result is None:
            raise NameError("'actual' or 'expect' can't be empty.")
        actual_result = self.get_text(actual_el)
        self.driver.assertEqual(actual_result, expect_result, msg)

    def assert_exist(self, expect_el, msg=None):
        """
        判断元素是否存在,存在则pass
        :param expect_el:
        :return:
        """
        self.diver.assertIsNotNone(expect_el, msg)

    def assert_in(self, actual_text, expect_text, msg=None):
        """
        判断预期文字信息是否包含在当前文字信息中
        :param expect_text:
        :return:
        """
        self.driver.assertIn(actual_text, expect_text, msg)

    def save_screen_shot(self, name='screen_shot'):
        """
        保存截图
        :param name:
        :return:
        """
        screen_shot_path = REPORT_PATH + '\\screen_shot_%s' % now_time_day
        if not os.path.exists(screen_shot_path):
            os.makedirs(screen_shot_path)
        code_obj = sys._getframe(3).f_code
        code_file = os.path.basename(code_obj.co_filename).replace('.', '_')
        code_method = sys._getframe(3).f_code.co_name
        # print code_file, code_method
        # screen_shot = self.driver.save_screenshot('\\%s_%s_%s.png' % (name, code_file, code_method))
        # screen_shot = self.driver.save_screenshot(screen_shot_path + '\\%s_%s.png' % (name, now_time_s))
        if name == 'screen_shot':
            print (screen_shot_path + '\\%s_%s_%s.png' % (name, code_file, code_method))
            screen_shot = self.driver.save_screenshot(
                screen_shot_path + '\\%s_%s_%s.png' % (name, code_file, code_method))
            return screen_shot
        elif name != 'screen_shot':
            self.driver.save_screenshot(screen_shot_path + '\\'+ name + '.png')
            return screen_shot_path

    # def get(self, url, maximize_window=True):
    #     """
    #     初始化浏览器
    #     :param url: 打开的url值
    #     :param maximize_window: 最大化窗口
    #     :return:
    #     """
    #     if maximize_window:
    #         self.driver.maximize_window()
    #     self.driver.get(url)

    def scroll_into_view(self, locator, by=By.XPATH, wait_times=50, click_type=0):
        """
        鼠标滚动
        """
        self.elem_presence_wait(locator, by, wait_times)
        ele = self.driver.find_element(by, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        if click_type == 0:
            ele.click()

    def get_token(self, api_key_1, secret_key_1):
        # 获取access_token
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + api_key_1 + \
               '&client_secret=' + secret_key_1
        request = urllib2.Request(host)
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        response = urllib2.urlopen(request)
        content = response.read()
        content_json = json.loads(content)
        access_token1 = content_json['access_token']
        print access_token1
        return access_token1

    def recognition_word_high(self, file_path1, file_name1, access_token3):
        #  proxy代理
        # The proxy address and port:
        proxy_info = {'host': 'web-proxy.oa.com', 'port': 8080}
        # We create a handler for the proxy
        proxy_support = urllib2.ProxyHandler({"http": "http://%(host)s:%(port)d" % proxy_info})
        # We create an opener which uses this handler:
        opener = urllib2.build_opener(proxy_support)
        # Then we install this opener as the default opener for urllib2:
        urllib2.install_opener(opener)

        url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=' + access_token3
        # url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=' + access_token3
        # url='https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=' + access_token
        # 二进制方式打开图文件
        f = open(file_path1 + file_name1, 'rb')  # 二进制方式打开图文件
        # 参数image：图像base64编码
        img = base64.b64encode(f.read())
        params = {"image": img}
        params = urllib.urlencode(params)
        request = urllib2.Request(url, params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        for tries in range(10):
            try:
                response = urllib2.urlopen(request)
                content = response.read()
                break
            except Exception as e:
                raise e
                continue
        if content:
            # print(content)
            world = re.findall('"words": "(.*?)"}', str(content), re.S)
            for each in world:
                print(each)
        print json.loads(content)
        return json.loads(content)






