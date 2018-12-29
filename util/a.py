from util.faker_num import get_card_no, get_id_no, get_phone_no, get_corp_no
import random
from faker import Faker
from datetime import datetime
import time

fake = Faker('zh_CN')
a = fake.street_name()
print(a, type(a))
print(a + '支行')
s = get_card_no()
print(s[0], s[1])
m = get_id_no()
print(m)

dic = {'622588': '招商银行', '622848': '中国农业银行',
           '622280': '中国建设银行', '603367': '杭州银行',
           '601428': '交通银行', '621226': '中国工商银行'}
num = random.randint(0, len(dic)-1)
n = get_phone_no()
print(n)
print(get_corp_no())
s = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(s)
time.sleep(2)
m = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(m)

o1 = '2018-12-14 13:50:00'
print(s > o1)

n = datetime.strptime(m, "%Y-%m-%d %H:%M:%S")
print(n)

l1 = datetime.strptime('2018-12-15 13:46:10', "%Y-%m-%d %H:%M:%S")
print(n < l1)
