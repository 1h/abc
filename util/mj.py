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


def dict_get(dict, objkey, default):
    tmp = dict
    for k, v in tmp.items():
        if k == objkey:
            return v
        else:
            if type(v).__name__ == 'dict':
                ret = dict_get(v, objkey, default)
                if ret is not default:
                    return ret
            elif type(v).__name__ == 'list':
                for i in v:
                    if type(i).__name__ == 'dict':
                        ret = dict_get(i, objkey, default)
                        # if ret is not default:
                        #     return ret
                    elif type(i).__name__ == 'list':
                        for l in i:
                            ret = dict_get(l, objkey, default)
                            if ret is not default:
                                return ret
            else:
                continue
        return default


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
            d = dict_get(house_id, 'leaseRoomRentTypeList', None)
            print(d)


mj_add_paytype()
