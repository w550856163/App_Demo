# -*- coding: utf-8 -*-
#@File ：app_demo01.py.py
#@Auth ： wwd
#@Time ： 2020/12/20 3:19 上午

from appium import webdriver
# 配置项
des = {
    "platformName":"android",
    "platformVersion":"8.0",
    "deviceName":"Samsung Galaxy S8",
    "appPackage": "com.android.settings",
    "appActivity": ".Settings",
    "udid":"192.168.56.102:5555",
    "noReset":True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    "newCommandTimeout":30
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des)