# conding:utf-8
import requests
from lxml import etree
import urllib3
urllib3.disable_warnings()


s = requests.session()


def get_it_execution():
    result = {}
    loginurl = "https://account.chsi.com.cn/passport/login"
    h1 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    }
    s.headers.update(h1)
    r = s.get(loginurl, verify=False)
    dom = etree.HTML(r.content.decode("utf-8"))

    try:
        result["lt"] = dom.xpath('//input[@name="lt"]')[0].get("value")
        result["execution"] = dom.xpath(
            '//input[@name="execution"]')[0].get("value")
        print(result)
    except:
        print("lt、execution参数获取失败！")
    return result


def login(result, user='13812348888', psw='123456'):
    loginurl = "https://account.chsi.com.cn/passport/login"
    h2 = {
        "Referer": loginurl,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Origin": "https://account.chsi.com.cn",
        "Content-Length": "119",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    body = {
        "username": user,
        "password": psw,
        "rememberMe": "true",
        "lt": result["lt"],
        "execution": result["execution"],
        "_eventId": "submit"
    }
    s.headers.update(h2)
    r4 = s.post(loginurl, data=body, verify=False)
    print(r4.text)


if __name__ == "__main__":
    result = get_it_execution()
    login(result, user='330122199008151710', psw='368008234')