# _*_coding:utf-8_*_
import requests
import json
from util.get_config import getConfig


def mj_login(func):

    def logging():
        url = getConfig("MJ", "url1")
        doLogin = getConfig("MJ", "doLogin")
        username = getConfig("MJ", "username")
        password = getConfig("MJ", "password")
        data = {"doLogin": doLogin, "username": username, "password": password}
        response = requests.post(url, data=data)
        print(response.status_code)
        return func
    return logging()


@mj_login
def mj_addhouser():
    url = getConfig("MJ", "url2")
    data = {"pageNo": 1, "pageSize": 20, "houseRentType": 1}
    response = requests.post(url, data=data)
    print(response.status_code)


if __name__ == "__main__":
    mj_addhouser()