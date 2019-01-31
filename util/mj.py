# _*_coding:utf-8_*_
import requests
import json
import math
from util.get_config import getConfig


def login():
    url = getConfig("MJ", "url1")
    doLogin = getConfig("MJ", "doLogin")
    username = getConfig("MJ", "username")
    password = getConfig("MJ", "password")
    data = {"doLogin": doLogin, "username": username, "password": password}
    s = requests.session()
    res = s.post(url=url, data=data)
    return s


def mj_get_house(houseType):
    url = getConfig("MJ", "url2")
    data = {"pageNo": 1, "pageSize": 20, "houseRentType": houseType}
    rs = login().post(url=url, data=data)
    house_dump = rs.text
    house_info = json.loads(house_dump)
    house_no = math.ceil(house_info.get('records')/20)
    accept_house = []
    for a in range(house_no):
        data = {"pageNo": a+1, "pageSize": 20, "houseRentType": houseType}
        rs = login().post(url=url, data=data)
        house_dump = rs.text
        house_info = json.loads(house_dump)
        house_list = house_info.get('result')
        for b in house_list:
            hid = b['houseType']
            if hid == 1:
                accept_house.append(b['houseId'])
    return accept_house


def dict_generator(indict, pre=None, keyname=None):
    pre = pre[:] if pre else []
    x = keyname
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, dict):
                if len(value) == 0:
                    yield pre + [key, '{}']
                else:
                    for d in dict_generator(value, pre + [key], keyname):
                        yield d
            elif isinstance(value, list):
                if key == keyname and len(value) == 0:
                    yield key
                elif len(value) == 0:
                    yield pre + [key, '[]']
                else:
                    for v in value:
                        for d in dict_generator(v, pre + [key], keyname):
                            yield d
            elif isinstance(value, tuple):
                if len(value) == 0:
                    yield pre + [key, '()']
                else:
                    for v in value:
                        for d in dict_generator(v, pre + [key], keyname):
                            yield d
            else:
                yield pre + [key, value]

    else:
        yield indict


def mj_add_paytype():
    a = mj_get_house(1)
    b = mj_get_house(2)
    if len(a) > 0:
        for c in a:
            url = getConfig("MJ", "url3")
            data = {"houseId": c}
            rs = login().post(url=url, data=data)
            house_dump = rs.text
            house_id = json.loads(house_dump)
            for n in dict_generator(house_id, keyname='leaseRoomRentTypeList'):
                print(n)
    else:
        print("没有可供C类申请的房源")


mj_add_paytype()
