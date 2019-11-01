# coding:utf-8
"""
@author: Tracy
@mail: wanghongyu@ruijie.com.cn
@date: 2019.05.27
"""
import os


""" 读取配置 """

BASE_PATH = os.path.split(os.path.abspath(__file__))[0]
PAGE_PATH = os.path.join(BASE_PATH, 'Page')
DATA_PATH = os.path.join(BASE_PATH, 'Data')
LOG_PATH = os.path.join(BASE_PATH, 'Log')
REPORT_PATH = os.path.join(BASE_PATH, 'Report')
DRIVER_PATH = os.path.join(BASE_PATH, 'Driver')
CASE_PATH = os.path.join(BASE_PATH, 'Case')
CONFIG_PATH = os.path.join(BASE_PATH, 'config')
CASE_RECORD_PATH = os.path.join(BASE_PATH, 'Case-record')
CASE_PATH_BASIC_OPERATE = os.path.join(CASE_PATH, 'basic_operate')


