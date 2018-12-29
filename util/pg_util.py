from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import re


class Index:
    def __init__(self, driver):
        self.dr = driver

    def admin_login(self, url, username, password, volidcode):
        dr = self.dr
        dr.get(url)
        l1 = dr.find_element_by_id('userName')
        l2 = dr.find_element_by_id('password')
        l3 = dr.find_element_by_id('valicode')
        l1.clear()
        l2.clear()
        l1.send_keys(username)
        l2.send_keys(password)
        l3.send_keys(volidcode)
        l4 = dr.find_element_by_id('submit')
        l4.click()

    def c_login(self, url, username, password):
        dr = self.dr
        dr.get(url)
        l1 = dr.find_element_by_id('userid')
        l2 = dr.find_element_by_id('pwd')
        l3 = dr.find_element_by_id('btn-Login')
        l1.clear()
        l2.clear()
        l1.send_keys(username)
        l2.send_keys(password)
        l3.click()

    def fundscode_login(self, url, mobile, volidcode):
        dr = self.dr
        dr.get(url)
        into_btn = dr.find_element_by_xpath(
            '//*[@id="login"]/div[2]/div[4]/a[2]')
        ActionChains(dr).click(into_btn).perform( )
        dr.find_element_by_id(
            'ipt-mobile').send_keys(mobile)
        get_btn = dr.find_element_by_xpath(
            '//*[@id="login"]/div[2]/div[2]/button/span')
        ActionChains(dr).click(get_btn).perform( )
        dr.find_element_by_id(
            'ipt-code').send_keys(volidcode)
        sleep(1)
        login_btn = dr.find_element_by_id('btn-login')
        ActionChains(dr).click(login_btn).perform( )
        try:
            wait(dr, 100).until_not(EC.visibility_of_element_located(
                (By.ID, 'btn-login')))
        except Exception as e:
            print("Exception found", format(e))

    def fundsreset_password(self, url, mobile, volidcode, password):
        dr = self.dr
        dr.get(url)
        into_btn = dr.find_element_by_xpath(
            '//*[@id="login"]/div[2]/div[4]/a[1]')
        ActionChains(dr).click(into_btn).perform( )
        sleep(1)
        dr.find_element_by_id(
            'ipt-mobile').send_keys(mobile)
        get_btn = dr.find_element_by_xpath(
            '//*[@id="forget"]/div[2]/div[2]/button/span')
        ActionChains(dr).click(get_btn).perform( )
        dr.find_element_by_id(
            'ipt-code').send_keys(volidcode)
        sleep(1)
        dr.find_element_by_id('ipt-pwd').send_keys(password)
        confirm_btn = dr.find_element_by_id('btn-confirm')
        ActionChains(dr).click(confirm_btn).perform( )
        try:
            wait(dr, 100).until_not(EC.visibility_of_element_located(
                (By.ID, 'btn-confirm')))
        except Exception as e:
            print("Exception found", format(e))

    def funds_login(self, url, username, password):
        dr = self.dr
        dr.get(url)
        dr.find_element_by_id(
            'ipt-mobile').send_keys(username)
        dr.find_element_by_id(
            'ipt-pwd').send_keys(password)
        try:
            wait(dr, 100).until(EC.visibility_of_element_located(
                (By.ID, 'btn-login')))
        except Exception as e:
            print("Exception found", format(e))
        dr.find_element_by_id('btn-login').click( )
        try:
            wait(dr, 100).until_not(EC.visibility_of_element_located(
                (By.ID, 'btn-login')))
        except Exception as e:
            print("Exception found", format(e))

    def esign(self):
        dr = self.dr
        dr.get('https://admin-testa.panguyr.tech/pg-wechat/pg-wechat.html#/login')
        dr.find_element_by_css_selector(
            'input[placeholder="请输入手机号码"]').send_keys('15657168150')
        dr.find_element_by_class_name('login-code').click( )
        dr.find_element_by_css_selector(
            'input[placeholder="请输入验证码"]').send_keys('123456')
        sleep(1)
        wait(dr, 10).until(EC.visibility_of_element_located(
            (By.CLASS_NAME, 'mint-button-text')))
        dr.find_element_by_css_selector('div.btn-wrap').click( )
        sleep(1)
        dr.find_element_by_css_selector('a.mint-cell').click( )
        sleep(1)
        dr.find_element_by_css_selector('div.btn-sign-wrap').click( )
        try:
            wait(dr, 100).until_not(EC.visibility_of_element_located(
                (By.CLASS_NAME, 'mint-button-text')))
        except Exception as e:
            print("Exception found", format(e))
        finally:
            print('合同上传成功')

    def pic_upload(self, order_type, frame_id, list1, list2):
        dr = self.dr
        pic_id = 1
        for num in zip(list1, list2):
            if num[1] != '房东身份证明' and order_type != 'type_c':
                dr.switch_to.frame('mainFrame')
            dr.find_element_by_id(num[0]).click( )
            if order_type != 'type_c':
                dr.switch_to.parent_frame( )
            file_add = 'D:/AutoTest/unittest/res/PNG/a' + str(pic_id) + '.png'
            frame_add = 'layui-layer-iframe' + str(frame_id)
            wait(dr, 10).until(
                EC.frame_to_be_available_and_switch_to_it(frame_add))
            dr.find_element_by_id('fileImage').send_keys(file_add)
            dr.find_element_by_id('startUpload').click( )  # 点击上传按钮
            wait(dr, 10).until(EC.visibility_of_element_located(
                (By.ID, 'uploadSuccess_0')))
            dr.find_element_by_id('close_btn').click( )
            wait(dr, 10).until_not(
                EC.visibility_of_element_located((By.ID, 'close_btn')))
            print(num[1] + '上传成功')
            pic_id += 1
            frame_id += 1

    def deal(self, burl, name, password, captcha, position, xp, text, action):
        dr = self.dr
        self.admin_login(burl, name, password, captcha)
        wait(dr, 10).until(EC.title_is(u"消费金融系统"))
        n1 = dr.find_element_by_css_selector(
            'a[href="sales/wfWaitingTaskIndex?flag=1"]')
        n1.click()
        wait(dr, 10).until(EC.frame_to_be_available_and_switch_to_it('mainFrame'))
        n2 = dr.find_element_by_id(position)
        n2.click()
        wait(dr, 10).until_not(
            EC.visibility_of_element_located((By.ID, position)))
        n3 = dr.find_element_by_xpath(xp)
        n3.click()
        locator = (By.XPATH, xp)
        wait(dr, 10).until_not(EC.visibility_of_element_located(locator))
        if text == '业务员签订合同' or text == '合同复审通过' or text == '总裁审核通过':
            elems = dr.find_elements_by_css_selector(
                'button[class="btn btn-sm btn-danger"]')
            for elem in elems:
                elem = elem.get_attribute('onclick')
                url = re.findall(r"window\.open\(\'(.+?)\'\)", elem)[0]
                dr.get(url)
                dr.switch_to.frame('mainFrame')
        if text == 'C类房源认证提交':
            n4 = dr.find_element_by_id('file10899')
            n4.send_keys('D:/AutoTest/unittest/res/PNG/a7.png')
            n5 = dr.find_element_by_class_name('upload')
            n5.click()
            wait(dr, 10).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'span[id="output10899"]')))
        n4 = dr.find_element_by_id('opinion')
        n4.send_keys(text)
        if text == '业务员终止订单':
            n5 = dr.find_elements_by_css_selector(
                '[class="btn btn-lg btn-danger"]')[1]
            n5.click()
        else:
            n5 = dr.find_element_by_id(action)
            n5.click()
            dr.switch_to.parent_frame()
        wait(dr, 10).until(EC.visibility_of_element_located(
            (By.CLASS_NAME, 'layui-layer-btn0')))
        n6 = dr.find_element_by_class_name('layui-layer-btn0')
        n6.click( )
        wait(dr, 10).until_not(EC.visibility_of_element_located(
            (By.CLASS_NAME, 'layui-layer-btn0')))

    def get_house_id(self, order_type):
        dr = self.dr
        for num in range(2, 11):
            a = dr.find_element_by_xpath('//*[@id="grid-table"]/tbody/tr[' + str(num) + ']/td[1]').text
            b = dr.find_element_by_xpath('//*[@id="grid-table"]/tbody/tr[' + str(num) + ']/td[5]').text
            if b == '暂无借款':
                return a
            elif order_type == 'F2':
                if b == '装修乐 ':
                    return a
            elif order_type == 'K1':
                if b == '收房乐 ':
                    return a
            elif order_type == 'CF2':
                if b == '装修乐 ':
                    return a
            elif order_type == 'CK1':
                if b == '收房乐 ':
                    return a
            else:
                continue

    def get_order_id(self, start_time, order_type, burl, name, password, captcha):
        dr = self.dr
        if order_type == 'RF2':
            dr.switch_to.default_content()
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

                if order_type == 'RF2':
                    if b == '收房乐' and c == '胡杭杰':
                        if d > start_time:
                            xp = '//*[@id="' + a + '"]/td[20]/a'
                            oid = a
                            return xp, oid

        elif order_type == 'TypeC':
            dr.admin_login(burl, name, password, captcha)
            wait(dr, 10).until(EC.title_is(u"消费金融系统"))
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

                if order_type == 'TypeC':
                    if b == 'C类金融房源认证' and c == '胡杭杰':
                        if d > start_time:
                            xp = '//*[@id="' + a + '"]/td[20]/a'
                            oid = a
                            return xp, oid
        else:
            wait(dr, 10).until(EC.frame_to_be_available_and_switch_to_it('mainFrame'))
            for num in range(2, 11):
                a = dr.find_element_by_xpath('//*[@id="grid-table"]/tbody/tr[' + str(num) + ']/td[1]').text
                b = dr.find_element_by_xpath('//*[@id="grid-table"]/tbody/tr[' + str(num) + ']/td[3]').text
                c = dr.find_element_by_xpath('//*[@id="grid-table"]/tbody/tr[' + str(num) + ']/td[4]').text
                d = dr.find_element_by_xpath('//*[@id="grid-table"]/tbody/tr[' + str(num) + ']/td[5]').text

                if order_type == 'F2':
                    if b == '收房乐' and c == '胡杭杰':
                        if d > start_time:
                            xp = '//*[@id="' + a + '"]/td[20]/a'
                            oid = a
                            return xp, a
                elif order_type == 'K1':
                    if b == '装修乐' and c == '胡杭杰':
                        if d > start_time:
                            xp = '//*[@id="' + a + '"]/td[20]/a'
                            oid = a
                            return xp, oid
                elif order_type == 'CF2':
                    if b == '集中式收房乐' and c == '胡杭杰':
                        if d > start_time:
                            xp = '//*[@id="' + a + '"]/td[20]/a'
                            oid = a
                            return xp, a
                elif order_type == 'CK1':
                    if b == '集中式装修乐' and c == '胡杭杰':
                        if d > start_time:
                            xp = '//*[@id="' + a + '"]/td[20]/a'
                            oid = a
                            return xp, a
                else:
                    continue

    def is_element_exist(self, istype, element):
        dr = self.dr
        flag = True
        try:
            if istype == 'xpath':
                dr.find_element_by_xpath(element)
                return flag
            elif istype == 'id':
                dr.find_element_by_id(element)
                return flag
            elif istype == 'class_name':
                dr.find_element_by_class_name(element)
                return flag
            elif istype == 'css_selector':
                dr.find_elements_by_css_selector(element)
                return flag
        except:
            flag = False
            return flag

