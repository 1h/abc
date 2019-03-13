# _*_coding:utf-8
import unittest
from selenium import webdriver
from util.pg_util import Index
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait
from faker import Faker
from util.faker_num import *
from datetime import datetime
from util.get_config import getConfig


class F2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        profile = {'plugins.plugins_list': [{"enabled": False, "name": "Chrome PDF Viewer"}],
                   'download.default_directory': "D:\\AutoTest\\PDF"}
        options.add_experimental_option("prefs", profile)
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        # options.add_argument('window-size=1920,1080')
        cls.driver = webdriver.Chrome(chrome_options=options)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        cls.pg = Index(cls.driver)

        global burl, eurl, captcha, login_list, name, action, text, position, order_type, start_time
        burl = getConfig("F2", "burl")
        eurl = getConfig("Eh5", "url")
        captcha = getConfig("F2", "captcha")
        l1 = getConfig("F2", "login_list")
        login_list = eval(l1)
        name = list(login_list.keys())
        l2 = getConfig("F2", "action")
        action = eval(l2)
        l3 = getConfig("F2", "position")
        position = eval(l3)
        l4 = getConfig("F2", "text")
        text = eval(l4)
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        order_type = getConfig("F2", "order_type")
        globals()["xp"] = None
        globals()["oid"] = None

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_11order_submit(self):
        pg = self.pg
        dr = self.driver
        fake = Faker('zh_CN')
        pg.admin_login(burl, name[0], login_list[name[0]], captcha)
        wait(dr, 10).until(EC.title_is('消费金融系统'))
        n1 = dr.find_element_by_class_name('menu-text')
        n1.click()
        n2 = dr.find_element_by_css_selector('a[href="sales/wfAllMyOrderIndex"]')
        n2.click()
        wait(dr, 10).until(EC.frame_to_be_available_and_switch_to_it('mainFrame'))
        n3 = dr.find_elements_by_css_selector('[class="btn btn-danger btn-sm"]')[0]
        n3.click()
        n4 = dr.find_element_by_name('cardId')
        n4.send_keys('330122199008151710')
        n4.send_keys(Keys.ENTER)
        n5 = dr.find_element_by_name('customerName')
        n5.click()
        n6 = dr.find_elements_by_css_selector('[class="ace ace-checkbox-2"]')[0]
        n6.send_keys(Keys.SPACE)
        n7 = dr.find_element_by_id('orderSubmit')
        n7.click()
        # 有时有问题 有时没有
        # wait(dr, 10).until(EC.frame_to_be_available_and_switch_to_it('mainFrame'))
        order_id = pg.get_house_id(order_type)
        n8 = dr.find_element_by_xpath('//*[@id="2_' + order_id + '"]/td[6]/button')
        n8.click()
        dr.switch_to.parent_frame()
        wait(dr, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'layui-layer-min')))
        js4 = "document.querySelector('.layui-layer-setwin').children[2].click()"
        dr.execute_script(js4)
        dr.switch_to.frame('mainFrame')  # 切回主frame
        s1 = Select(dr.find_element_by_id('ownerType'))
        s1.select_by_value('01')
        l1 = dr.find_element_by_name('housingInfoBean.propertyEnterpriceName')
        l1.clear()
        l2 = dr.find_element_by_name('housingInfoBean.propertyEnterpriceAddress')
        l2.clear()
        l3 = dr.find_element_by_name('housingInfoBean.propertyBusinessLicense')
        l3.clear()
        m1 = dr.find_element_by_name('housingInfoBean.propertyNo')
        m1.clear()
        m2 = dr.find_element_by_name('housingInfoBean.ownerPhone')
        m2.clear()
        m3 = dr.find_element_by_name('housingInfoBean.owner')
        m3.clear()
        m4 = dr.find_element_by_name('housingInfoBean.cardId')
        m4.clear()
        m5 = dr.find_element_by_name('housingInfoBean.propertyAddress')
        m5.clear()
        m6 = dr.find_element_by_name('houseAddress')
        m6.clear()
        m7 = dr.find_element_by_name('housingInfoBean.landlordName')
        m7.clear()
        m8 = dr.find_element_by_name('housingInfoBean.landlordIdNo')
        m8.clear()
        m9 = dr.find_element_by_name('housingInfoBean.landlordCardNo')
        m9.clear()
        m10 = dr.find_element_by_name('housingInfoBean.landlordAccountingBranch')
        m10.clear()

        m1.send_keys(fake.ean13())
        l1.send_keys(fake.company())
        l2.send_keys(fake.address())
        l3.send_keys(get_corp_no())
        m2.send_keys(get_phone_no())
        m3.send_keys(fake.name())
        m4.send_keys(get_id_no())
        m5.send_keys(fake.address())
        m6.send_keys(fake.address())
        m7.send_keys(fake.name())
        m8.send_keys(get_id_no())
        m9.send_keys(get_card_no()[1])
        m10.send_keys(fake.street_name() + '支行')

        # 输入时间
        js1 = "document.getElementById('beginTime').removeAttribute('readonly');"
        dr.execute_script(js1)
        t1 = dr.find_element_by_id('beginTime')
        t1.send_keys('2018-11-08')
        js2 = "document.getElementById('endTime').removeAttribute('readonly');"
        dr.execute_script(js2)
        t2 = dr.find_element_by_id('endTime')
        t2.send_keys('2021-12-08')
        t3 = dr.find_elements_by_css_selector('[class="layui-icon"]')[2]
        t3.click()

        m11 = dr.find_element_by_name('housingInfoBean.rentalPrice')
        m11.send_keys('0.09')
        if pg.is_element_exist('id', 'houseArea'):
            dr.find_element_by_id('houseArea').send_keys('89')
        s2 = Select(dr.find_element_by_id('timeLimit'))
        s2.select_by_index(2)
        s3 = Select(dr.find_element_by_id('serviceChargeType'))
        s3.select_by_index(2)
        s4 = Select(dr.find_element_by_id('serviceChargeIssue'))
        s4.select_by_index(1)
        s5 = Select(dr.find_element_by_id('contractAmountType'))
        s5.select_by_index(1)

        js3 = "var q=document.documentElement.scrollTop=100000"
        dr.execute_script(js3)

        # 图片上传
        frame_id = 2
        list1 = ['num_0101', 'num_0102', 'num_0104', 'num_0105', 'num_0106', 'num_0107', 'num_0108']
        list2 = ['房东身份证明', '产权证明', '收款银行卡', '房源现场照片', '双签收房合同', '现场签约照片', '付租相关']
        pg.pic_upload(order_type, frame_id, list1, list2)

        # 页面提交
        dr.switch_to.frame('mainFrame')
        dr.find_element_by_css_selector('[class="btn btn-lg btn-danger"]').click()
        dr.switch_to.parent_frame()
        dr.find_element_by_class_name('layui-layer-btn0').click()
        dr.find_element_by_class_name('layui-layer-btn0').click()
        print('提交成功')

        # 查找生成的订单ID
        globals()["xp"], globals()["oid"] = pg.get_order_id(start_time, order_type, burl, name[0], login_list[name[0]], captcha)

    def test_12reject(self):
        pg = self.pg
        pg.deal(burl, name[1], login_list[name[1]], captcha, position[0], globals()["xp"], text[0], action[1])

    def test_13resubmit(self):
        pg = self.pg
        pg.deal(burl, name[0], login_list[name[0]], captcha, position[1], globals()["xp"], text[1], action[0])

    def test_14zhonghe(self):
        pg = self.pg
        pg.deal(burl, name[1], login_list[name[1]], captcha, position[0], globals()["xp"], text[2], action[0])

    def test_15fengkong(self):
        pg = self.pg
        pg.deal(burl, name[2], login_list[name[2]], captcha, position[2], globals()["xp"], text[3], action[0])

    def test_16fuzheren(self):
        pg = self.pg
        pg.deal(burl, name[3], login_list[name[3]], captcha, position[3], globals()["xp"], text[4], action[0])

    def test_17hegui(self):
        pg = self.pg
        pg.deal(burl, name[4], login_list[name[4]], captcha, position[4], globals()["xp"], text[5], action[0])

    def test_18esign(self):
        pg = self.pg
        pg.esign(eurl)

    def test_19hetong1(self):
        pg = self.pg
        pg.deal(burl, name[1], login_list[name[1]], captcha, position[5], globals()["xp"], text[6], action[0])

    def test_20hetong2(self):
        pg = self.pg
        pg.deal(burl, name[1], login_list[name[1]], captcha, position[6], globals()["xp"], text[7], action[0])

    def test_21zongcai(self):
        pg = self.pg
        pg.deal(burl, name[5], login_list[name[5]], captcha, position[7], globals()["xp"], text[8], action[0])

    def test_22zjhs(self):
        pg = self.pg
        pg.deal(burl, name[6], login_list[name[6]], captcha, position[8], globals()["xp"], text[9], action[2])

    def test_23deaf(self):
        pg = self.pg
        pg.deal(burl, name[0], login_list[name[0]], captcha, position[1], globals()["xp"], text[10], action[0])
