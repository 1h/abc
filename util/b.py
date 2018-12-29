# _*_coding:utf-8
import unittest
from selenium import webdriver
from util.pg_util import Index
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait
from datetime import datetime


class B2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        profile = {'plugins.plugins_list': [{"enabled": False, "name": "Chrome PDF Viewer"}],
                   'download.default_directory': "D:\\AutoTest\\PDF", 'profile.default_content_settings.popups': 0}
        options.add_experimental_option("prefs", profile)
        cls.driver = webdriver.Chrome(chrome_options=options)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        cls.pg = Index(cls.driver)

        global burl, captcha, login_list, name, action, text, position, order_type, start_time
        burl = 'https://admin-testa.panguyr.tech'
        captcha = 'ojbk'
        login_list = {'csmanager': '123456@pgyr', 'bsmanager': '123456@pgyr', 'rsmanager': '123456@pgyr', 'brmanager': '123456@pgyr', 'rscontroller': '123456@pgyr', 'zongcai': '123456@pgyr', 'zhujinling': 'ckjr@123456'}
        name = list(login_list.keys())
        action = ['passTask', 'rejectTask', 'toApplicant']
        position = ['usertask_sm_usertask_bcbof_m', '_usertask_sm_m', 'usertask_bcbof_usertask_brcm_m', 'usertask_brcm_usertask_bgm_m','usertask_bgm_usertask_cr_m', 'usertask_cr_usertask_bcbof_m', 'usertask_bcbof_usertask_crm_m', 'usertask_crm_usertask_ceo_m', 'usertask_ceo_usertask_acc_m']
        text = ['综合岗驳回成功', '业务员重新提交', '综合岗审核通过', '征信审核通过', '分公司负责人审核通过', '合规审核通过', '业务员签订合同', '合同复审通过', '总裁审核通过', '资金核算驳回到发起人', '业务员终止订单']
        order_type = 'F2'
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def test_id(self):
        pg = self.pg
        dr = self.driver
        pg.admin_login(burl, name[0], login_list[name[0]], captcha)
        wait(dr, 10).until(EC.title_is('消费金融系统'))
        n1 = dr.find_element_by_class_name('menu-text')
        n1.click()
        n2 = dr.find_element_by_css_selector('a[href="sales/wfAllMyOrderIndex"]')
        n2.click()
        wait(dr, 10).until(EC.frame_to_be_available_and_switch_to_it('mainFrame'))

        for num in range(2, 11):
            a = dr.find_element_by_xpath('//*[@id="grid-table"]/tbody/tr[' + str(num) + ']/td[1]').text
            b = dr.find_element_by_xpath('//*[@id="grid-table"]/tbody/tr[' + str(num) + ']/td[3]').text
            c = dr.find_element_by_xpath('//*[@id="grid-table"]/tbody/tr[' + str(num) + ']/td[4]').text
            d = dr.find_element_by_xpath('//*[@id="grid-table"]/tbody/tr[' + str(num) + ']/td[5]').text
            e = dr.find_element_by_xpath('//*[@id="grid-table"]/tbody/tr[' + str(num) + ']/td[6]').text

            if order_type == 'F2':
                if b == '收房乐' and c == '胡杭杰' and e == '杭州市':
                    if d > start_time:
                        return a
            elif order_type == 'K1':
                if b == '装修乐' and c == '胡杭杰' and e == '杭州市':
                    if d > start_time:
                        return a
            elif order_type == 'CF2':
                if b == '集中式收房乐' and c == '胡杭杰' and e == '杭州市':
                    if d > start_time:
                        return a
            elif order_type == 'CK1':
                if b == '集中式装修乐' and c == '胡杭杰' and e == '杭州市':
                    if d > start_time:
                        return a
            else:
                continue



