# _*_coding:utf-8_*_
import requests
import json
from util.get_config import getConfig


class MJ:

    def mj_login(self):
        url = getConfig("MJ", "url")
        doLogin = getConfig("MJ", "doLogin")
        username = getConfig("MJ", "username")
        password = getConfig("MJ", "password")
        data = {"doLogin": doLogin, "username": username, "password": password}
        response = requests.post(url, data=data)
        print(response.status_code)
        return response.status_code


if __name__ == "__main__":
    MJ().mj_login()
