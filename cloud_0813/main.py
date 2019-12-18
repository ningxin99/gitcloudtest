# coding:utf-8
"""
@author: Tracy
@mail: wanghongyu@ruijie.com.cn
@date: 2019.05.29
"""
import unittest
from utils.log import logger1
from selenium import webdriver
from config import *
from utils.HTMLTestRunner import HTMLTestRunner
from Common.com_function import *
from Data.basic_data import *
from Page.basic_page import *
import datetime
from utils.mail import Email


class TestRunner(object):
    def __init__(self, case_name, case_path=CASE_PATH, title="", description=""):
        self.case_path = case_path
        self.title = title
        self.description = description
        self.case_name = case_name


    def run(self):
        tests = unittest.defaultTestLoader.discover(self.case_path,
                                                    # pattern=self.case_name + '*.py',
                                                    pattern='cloud_' + '*.py',
                                                    # pattern='cloud_basic_check.py',
                                                    top_level_dir=None)
        with open(report, 'wb') as f:
            runner = HTMLTestRunner(f, verbosity=2, title=self.title, description=self.description)
            runner.run(tests)

    def debug(self):
        # 不输出测试报告
        # self.case_name + '*.py'
        tests = unittest.defaultTestLoader.discover(self.case_path, pattern=self.case_name + '*.py')
        runner = unittest.TextTestRunner(verbosity=2)
        print(self.case_name + " test start")
        runner.run(tests)
        print("test end")





if __name__ == '__main__':
    # unittest.main()
    for i in range(1):
        try:
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            report = REPORT_PATH + '\\report' + ' ' + now_time + 'num' + str(i) + '.html'
            if run_case_package == 'basic_operate':
               test = TestRunner(run_case_name, case_path=CASE_PATH_BASIC_OPERATE, title="测试用例：" + run_case_name)
            else:
                test = TestRunner(run_case_name, case_path=CASE_PATH_BEFORE_UPGRADE, title="测试用例：" + run_case_name)
            test.run()
        except Exception as b:
            print("test run error:%s" % str(b))
    e = Email(title='cloud自动化测试报告',
              message='Hi,please open using chrome',
              receiver=email_name,
              sender='xionghuigo@foxmail.com',
              password='nvijhiarouqbhajd',
              # sender='why119613@163.com',
              # password='why1113',
              server='smtp.qq.com',
              path=report
              )
    e.send()