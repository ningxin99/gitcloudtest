from Common.com_function import *
from Data.basic_data import *
from Page.basic_page import *
from utils.log import logger1
import sys

class Login:
    def __init__(self, driver, login_user=login_user_name_data_11, login_password=login_password_data_11,
                 url=login_url_local, maximize_window=True):
        self.driver = driver
        self.operate = ComFunction(self.driver)
        self.url = url
        self.maximize_window = maximize_window
        self.login_user = login_user
        self.login_password = login_password


    def login(self):
        code_obj = sys._getframe(1).f_code
        code_file = os.path.basename(code_obj.co_filename)
        # logger1.warning(code_file)
        if self.maximize_window:
            self.driver.maximize_window()
        self.driver.get(self.url)
        self.operate.elem_send_keys(user_name_xpath, self.login_user)
        self.operate.elem_send_keys(password_xpath, self.login_password)
        self.operate.click_elem(login_btn_xpath)
        time.sleep(10)
        self.operate.click_elem(login_close_tips_xpath)

