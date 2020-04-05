# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:11:05 2020

@author: Tejas
"""
from selenium import webdriver
import time
import urllib.request

options = webdriver.ChromeOptions()
options.add_argument("--headless") #1st objective of todays video
driver = webdriver.Chrome('F:\Channel\webdriver\chromedriver.exe', chrome_options=options)
time.sleep(1)

driver.get('https://unsplash.com/t/architecture')
time.sleep(1)

i = 1

unsplash = driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[2]')
wallpapers = unsplash.find_elements_by_css_selector('img._2zEKz')
for images in wallpapers:
    urllib.request.urlretrieve(images.get_attribute('src'),"{}.jpg".format(i)) #2nd objective of todays video
    i+=1
