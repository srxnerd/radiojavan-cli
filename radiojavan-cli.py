from selenium import webdriver
import time
import colored
import requests
import bs4
import os
import string
import sys
from selenium.webdriver.common.action_chains import ActionChains
print("        --------------------------------------------------")
print("        |                                               ||")
print("        |              🎷radiojavan-cli                 ||")
print("        |                 version : 1.1                 ||")
print("        |                                               ||")
print("        |             📨telegram:@py_gnu                ||")
print("        |                                               ||")
print("        |                                               ||")
print("        |                                               ||")
print("        |               Nerd In the Life                ||")
print("        |_____________🎷🎷🎷🎷🎷🎷🎷🎷🎷🎷_______________")
time.sleep(5)
print("\n\nPlease wait a few moment...")
link = "https://www.radiojavan.com/playlists/playlist/mp3/854b87855624"
driver =webdriver.Chrome("/home/sti/down_git/chromedriver")
driver.get(link)
time.sleep(2)
#]driver.find_element_by_xpath("//input[@name='username']").send_keys(userName)
#driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
elem = driver.find_element_by_xpath("""//*[@id="navContainer"]/div/a[1]""")
actions = ActionChains(driver)
actions.click(elem).perform()
elem2 = driver.find_element_by_xpath("""//*[@id="playlist"]/div/div[1]/div/div[2]/a[2]""").click()
po1 = driver.find_element_by_class_name("song").text
os.system("clear")
while True:
    next = input("\n\n                       ======>>>radiojavan-cli<<<=====\n\n1-Next music type(n) \n\n2-exit Type(e) \n\n3-Stop Type(s) \n\n4-Repeat Type(r)  \n\n5-max_window Type(max)  \n\n6-min_window  Type(min)   \n\n7-Downlaod Type(d) \n\n8-Back muisc Type(b) \n\n9-Muisc-Bio Type(bio) \n\n\nPlease Type:  ")
    po1 = driver.find_element_by_class_name("song").text
    po1 = driver.find_element_by_class_name("song").text
    if next == "bio":
        tx = driver.find_element_by_class_name("mp3Description").text
        os.system("clear")
        print("==========>Bio muisc<=============\n",tx)
    if next == "n":
        driver.find_element_by_xpath("""//*[@id="mp3_next"]""").click()
        os.system("clear")
    if next == "e":
        print("goodbye👋")
        break
    if next == "s":
        driver.find_element_by_xpath("""//*[@id="mp3_play"]""").click()
        os.system("clear")
    if next == "r":
        driver.find_element_by_xpath("""//*[@id="mp3_repeat"]""").click()
        os.system("clear")
    if next == "max":
        driver.maximize_window()
        os.system("clear")
    if next == "min":
        driver.minimize_window()
        os.system("clear")
    if next == "b":
        driver.find_element_by_xpath("""//*[@id="mp3_back"]""").click()
        os.system("clear")
    if next == "d":
        po = driver.find_element_by_class_name("artist").text
        link_rj="https://host2.rj-mw1.com/media/mp3/mp3-256/"
        ar = po
        ar = ar.replace(',', '')
        ar = ar.replace('&', '')
        ar = ar.replace('vs', '')
        ar = ar.replace('@', '')
        ar = ar.replace('*', '')
        ar = ar.replace('()', '')
        ar = ar.replace('(', '').replace(')', '')
        ar = ar.replace('[', '').replace(']', '')
        mp = "-".join(ar.split())
        song = po1
        song = song.replace(',', '')
        song = song.replace('(', '').replace(')', '')
        song = song.replace('[', '').replace(']', '')
        song = song.replace('{', '').replace('}', '')
        song = song.replace('*', '')
        song = song.replace('&', '')
        song = song.replace('vs', '')
        song = song.replace('@', '')
        md = "-".join(song.split())
        mp3=".mp3"
        newstr = "-".join((mp, md))
        ok=link_rj+newstr+mp3
        print(ok)
        os.system("mkdir radiojavan_music")
        os.system("wget "+ok)
        os.system("notify-send Downlaod-done✅")
        os.system("mv *.mp3 radiojavan_music")
        os.system("clear")
driver.close()
