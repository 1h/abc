# _*_coding:utf-8
import unittest
from selenium import webdriver
from util.pg_util import Index
from time import sleep
from util.get_config import getConfig


class Funds(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        globals()["url"] = getConfig("Funds", "url")
        globals()["mobile"] = getConfig("Funds", "mobile")
        globals()["password"] = getConfig("Funds", "password")
        globals()["volidcode"] = getConfig("Funds", "volidcode")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.pg = Index(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_funds1codeLogin(self):
        pg = self.pg
        pg.fundscode_login(globals()["url"], globals()[
                           "mobile"], globals()["volidcode"])

    def test_funds2resetpasswod(self):
        pg = self.pg
        globals()["password"] = '12345678'
        pg.fundsreset_password(globals()["url"], globals()[
            "mobile"], globals()["volidcode"], globals()["password"])

    def test_funds3Login(self):
        pg = self.pg
        dr = self.driver
        pg.funds_login(globals()["url"], globals()[
                       "mobile"], globals()["password"])
        sleep(1)
        js = "document.getElementsByClassName('el-dropdown-menu__item')[0].click();"
        dr.execute_script(js)
        dr.find_element_by_xpath(
            '//*[@id="header"]/div[2]/div/div[2]/div[1]/div[2]/div/input').send_keys('12345678')
        dr.find_element_by_xpath(
            '//*[@id="header"]/div[2]/div/div[2]/div[2]/div[2]/div/input').send_keys('123456')
        dr.find_element_by_xpath(
            '//*[@id="header"]/div[2]/div/div[2]/div[3]/div[2]/div/input').send_keys('123456')
        dr.find_element_by_xpath(
            '//*[@id="header"]/div[2]/div/div[3]/span/button[2]/span').click()
