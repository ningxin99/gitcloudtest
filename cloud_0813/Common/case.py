# coding=utf-8
"""
@author: Tracy
@mail: wanghongyu@ruijie.com.cn
@date: 2019.06.04
"""
import unittest
from Common.driver import Pyse
from selenium import webdriver



class TestCase(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = Pyse("chrome")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

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
        self.assertEqual(actual_result, expect_result, msg)

    def assert_exist(self, expect_el, msg=None):
        """
        判断元素是否存在,存在则pass
        :param expect_el:
        :return:
        """
        self.assertIsNotNone(expect_el, msg)

    def assert_in(self, actual_text, expect_text, msg=None):
        """
        判断预期文字信息是否包含在当前文字信息中
        :param expect_text:
        :return:
        """
        self.assertIn(actual_text, expect_text, msg)





