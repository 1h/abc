# _*_coding:utf-8_*_
import configparser
import os

def getConfig(section, key):
    config = configparser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + '/a.conf'
    config.read(path, encoding="utf-8-sig")
    return config.get(section, key)
