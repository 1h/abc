# _*_coding:utf-8
import random
import time
import string


def get_card_no():
    dic = {'622588': '招商银行', '622848': '中国农业银行',
           '622280': '中国建设银行', '603367': '杭州银行',
           '601428': '交通银行', '621226': '中国工商银行'}
    num = random.randint(0, len(dic)-1)
    prefix = list(dic)[num]
    bank_name = dic[prefix]
    a = ''.join(str(i) for i in random.sample(range(0, 9), 8))

    # 招行16位 交行17位 其他 19位
    if prefix == '622588':
        b = ''.join(str(i) for i in random.sample(range(0, 9), 1))
        bank_num = prefix + a + b
    elif prefix == '601428':
        b = ''.join(str(i) for i in random.sample(range(0, 9), 2))
        bank_num = prefix + a + b
    else:
        b = ''.join(str(i) for i in random.sample(range(0, 9), 4))
        bank_num = prefix + a + b

    num_lst = list(bank_num)
    count = 0
    for m in range(len(num_lst)):
        if m % 2 == 0:
            count = count + int(num_lst[m])*2
        else:
            count = count + int(num_lst[m])

    for n in range(10):
        if (count + n) % 10 == 0:
            bank_num = bank_num + str(n)
            break
    return bank_name, bank_num


def get_id_no():
    def region():
        # 生成身份证前六位
        # 列表里面的都是一些地区的前六位号码
        first_list = ['362402', '362421', '362422', '362423', '362424', '362425', '362426', '362427', '362428',
                      '362429', '362430', '362432', '110100', '110101', '110102', '110103', '110104', '110105',
                      '110106', '110107', '110108', '110109', '110111']
        first = random.choice(first_list)
        return first

    def year():
        # 生成年份
        now = time.strftime('%Y')
        # 1948为第一代身份证执行年份,now-18直接过滤掉小于18岁出生的年份
        second = random.randint(1948, int(now) - 18)
        # age = int(now) - second
        # print('随机生成的身份证人员年龄为：' + str(age))
        return second

    def month():
        # 生成月份
        three = random.randint(1, 12)
        # 月份小于10以下，前面加上0填充
        if three < 10:
            three = '0' + str(three)
            return three
        else:
            return three

    def day():
        # 生成日期
        four = random.randint(1, 31)
        # 日期小于10以下，前面加上0填充
        if four < 10:
            four = '0' + str(four)
            return four
        else:
            return four

    def randoms_num():
        # 生成身份证后三位
        # 后面序号低于相应位数，前面加上0填充
        five = random.randint(1, 999)
        if five < 10:
            five = '00' + str(five)
            return five
        elif 10 < five < 100:
            five = '0' + str(five)
            return five
        else:
            return five

    def id_no():
        first = region()
        second = year()
        three = month()
        four = day()
        five = randoms_num()
        id_card = str(first) + str(second) + str(three) + str(four) + str(five)
        check_dict = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7',
                      6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}

        check_num = 0
        for index, num in enumerate(id_card):
            check_num += int(num) * (2 ** (17 - index) % 11)
        right_code = check_dict.get(check_num % 11)
        return id_card + right_code

    return id_no()


def get_phone_no():
    pre_lst = ['133', '135', '136', '137', '138', '156', '157', '158', '166', '186', '187', '189', '198', '199']
    phone_no = random.choice(pre_lst) + ''.join(str(i) for i in random.sample(range(0, 9), 8))
    return phone_no


def get_corp_no():
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return salt
