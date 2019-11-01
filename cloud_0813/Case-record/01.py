# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://cloud-as.ruijienetworks.com/admin3/")
        driver.find_element_by_link_text("CONFIGURATION").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='CLIENT'])[2]/following::span[1]").click()
        driver.find_element_by_link_text("MAINTENANCE").click()
        driver.find_element_by_link_text("CONFIGURATION").click()
        driver.find_element_by_link_text("MONITORING").click()
        driver.find_element_by_id("monitor_device_accesspoint_menu").click()
        driver.find_element_by_id("monitor_device_gateway_menu").click()
        driver.find_element_by_link_text("CONFIGURATION").click()
        driver.find_element_by_id("config_wireless_basic_menu").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='(GMT+1:00)Europe/Berlin'])[1]/following::i[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='please click here→'])[1]/following::div[7]").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("13637499363@163.com")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("why961113")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='More'])[1]/following::div[2]").click()
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("321162718@qq.com")
        driver.find_element_by_id("login-form").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='找回密码'])[1]/following::div[7]").click()
        driver.find_element_by_id("J_userLogin_btn").click()
        driver.find_element_by_link_text("CONFIGURATION").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Database Backup'])[1]/following::span[1]").click()
        driver.find_element_by_link_text("CONFIGURATION").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='CLIENT'])[2]/following::span[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='test_chu'])[2]/following::i[6]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
