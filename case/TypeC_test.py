# _*_coding:utf-8
import unittest
from selenium import webdriver
from util.pg_util import Index
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from faker import Faker
from util.faker_num import *
from datetime import datetime
from util.get_config import getConfig


class typec(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions( )
        profile = {'plugins.plugins_list': [{"enabled": False, "name": "Chrome PDF Viewer"}],
                   'download.default_directory': "D:\\AutoTest\\PDF"}
        options.add_experimental_option("prefs", profile)
        cls.driver = webdriver.Chrome(chrome_options=options)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        cls.pg = Index(cls.driver)
        global curl, burl, cname, cpassword, captcha, login_list, name, action, text, position, order_type, start_time
        curl = getConfig("Typec", "curl")   # 未解决
        burl = getConfig("Typec", "burl")
        cname = getConfig("Typec", "cname")
        cpassword = getConfig("Typec", "cpassword")
        captcha = getConfig("Typec", "captcha")
        l1 = getConfig("Typec", "login_list")
        login_list = eval(l1)
        name = list(login_list.keys())
        l2 = getConfig("Typec", "action")
        action = eval(l2)
        l3 = getConfig("Typec", "position")
        position = eval(l3)
        l4 = getConfig("Typec", "text")
        text = eval(l4)
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        order_type = getConfig("Typec", "order_type")
        globals()["xp"] = None
        globals()["oid"] = None

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_c0(self):
        pg = self.pg
        dr = self.driver
        pg.c_login(curl, cname, cpassword)
        l1 = dr.find_element_by_css_selector('.btn.btn-mj.layui-layer-btn0')
        l1.click()
        l2 = "document.getElementsByClassName('inner')[1].click()"
        dr.execute_script(l2)
        l3 = dr.find_element_by_css_selector('a[href="/hms/hosting/develop/hostingHouseList.htm"]')
        l3.click()
        l4 = dr.find_elements_by_css_selector('[class="btn btn-mj"]')[3]
        l4.click()
        l5 = dr.find_element_by_id('city-title')
        l5.send_keys('浙江省/杭州市/西湖区')
        print('ok')

        print("ok")

    def test_c1(self):
        pg = self.pg
        dr = self.driver
        dr.get(curl)
        fake = Faker('zh_CN')
        m1 = dr.find_element_by_name('propertyNo')
        m1.clear()
        m2 = dr.find_element_by_name('propertyAddress')
        m2.clear()
        m3 = dr.find_element_by_name('houseAddress')
        m3.clear()
        m4 = dr.find_element_by_name('owner')
        m4.clear()
        m5 = dr.find_element_by_name('cardId')
        m5.clear()
        m6 = dr.find_element_by_name('ownerPhone')
        m6.clear()

        s1 = Select(dr.find_element_by_name('ownerType'))
        s1.select_by_value('01')

        m7 = dr.find_element_by_name('propertyEnterpriceName')
        m7.clear()
        m8 = dr.find_element_by_name('propertyEnterpriceAddress')
        m8.clear()
        m9 = dr.find_element_by_name('propertyBusinessLicense')
        m9.clear()

        s1 = Select(dr.find_element_by_name('ownerType'))
        s1.select_by_value('01')
        s2 = Select(dr.find_element_by_name('gender'))
        s2.select_by_value('01')
        s3 = Select(dr.find_element_by_name('cardType'))
        s3.select_by_value('1')

        m1.send_keys(fake.ean13())
        m2.send_keys(fake.address())
        m3.send_keys(fake.address())
        m4.send_keys(fake.name())
        m5.send_keys(get_id_no())
        m6.send_keys(get_phone_no())
        m7.send_keys(fake.company())
        m8.send_keys(fake.address())
        m9.send_keys(get_corp_no())

        js1 = "var q=document.documentElement.scrollTop=100000"
        dr.execute_script(js1)

        js2 = "document.getElementById('beginTime').removeAttribute('readonly');"
        dr.execute_script(js2)
        dr.find_element_by_name('beginTime').send_keys('2018-11-08')

        js3 = "document.getElementById('endTime').removeAttribute('readonly');"
        dr.execute_script(js3)
        dr.find_element_by_xpath('//*[@id="endTime"]').send_keys('2018-12-08')

        # 点击其他输入框关闭 时间输入框
        m9.click()

        # 使用zip双列表循环 上传图片
        list_num = ['num_0101', 'num_0102', 'num_0103', 'num_0104', 'num_0105', 'num_0106', 'num_0120']
        list_text = ['租赁合同上传成功', '房屋产权证明上传成功', '产权人营业执照上传成功', '法人身份证照片上传成功', '房源现场照片上传成功', '付租相关凭证上传成功', '委托管理合同上传成功']
        frame_id = 1
        pg.pic_upload(order_type, frame_id, list_num, list_text)

        m10 = dr.find_element_by_id('onebtn')
        m10.click()
        wait(dr, 10).until_not(EC.visibility_of_element_located((By.ID, 'onebtn')))
        m11 = dr.find_element_by_name('mjHouseRentTypes[0].rentPrice')
        m11.send_keys('15')
        m12 = dr.find_element_by_name('mjHouseRentTypes[0].depositPrice')
        m12.send_keys('12')
        m13 = dr.find_element_by_name('agreeTreaty')
        m13.click()
        m14 = dr.find_element_by_id('btn btn-lg btn-blue')
        m14.click()
        m15 = dr.find_element_by_class_name('layui-layer-btn0')
        m15.click()
        wait(dr, 10).until_not(EC.visibility_of_element_located((By.CLASS_NAME, 'layui-layer-btn0')))
        wait(dr, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'apply-finish-msg'), '恭喜您，提交成功！'))
        print('C类进件成功')

        # 获取订单ID
        pg.admin_login(burl, name[0], login_list[name[0]], captcha)
        wait(dr, 10).until(EC.title_is('消费金融系统'))
        # 获取order_id 暂时无解 可以采用 提交成功页后跳转csmanage 页面 或者 走 数据库
        globals()["xp"], globals()["oid"] = pg.get_order_id(start_time, order_type, burl, name[0], login_list[name[0]], captcha)

    def test_c2(self):
        pg = self.pg
        pg.deal(burl, name[0], login_list[name[0]], captcha, position[0], globals()["xp"], text[0], action[0])

    def test_c3(self):
        pg = self.pg
        pg.deal(burl, name[1], login_list[name[1]], captcha, position[1], globals()["xp"], text[1], action[1])

    def test_c4(self):
        pg = self.pg
        pg.deal(burl, name[0], login_list[name[0]], captcha, position[0], globals()["xp"], text[2], action[0])

    def test_c5(self):
        pg = self.pg
        pg.deal(burl, name[1], login_list[name[1]], captcha, position[1], globals()["xp"], text[3], action[0])

    def test_c6(self):
        pg = self.pg
        pg.deal(burl, name[2], login_list[name[2]], captcha, position[2], globals()["xp"], text[4], action[0])

    def test_c7(self):
        pg = self.pg
        pg.deal(burl, name[2], login_list[name[2]], captcha, position[3], globals()["xp"], text[5], action[0])

    def test_c8(self):
        pg = self.pg
        pg.deal(burl, name[3], login_list[name[3]], captcha, position[4], globals()["xp"], text[6], action[0])

    # 由于去标接口失效，暂时不复核提交 用例跳过
    @unittest.skip
    # def test_c9(self):
    #     pg = self.pg
    #     pg.deal(burl, name[1], login_list[name[1]], captcha, position[5], globals()["xp"], text[7], action[0])
    def test_c9(self):
        pg = self.pg
        pg.deal(burl, name[1], login_list[name[1]], captcha, position[5], globals()["xp"], text[8], action[2])

    # 造数据繁琐，暂时停用终止流程
    @unittest.skip
    def test_cz(self):
        pg = self.pg
        pg.deal(burl, name[0], login_list[name[0]], captcha, position[0], globals()["xp"], text[9], action[3])
