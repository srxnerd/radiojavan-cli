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
print("        |                 life fun ;)                   ||")
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
while True:
    next = input("\n\n1-Next music type(n) \n\n2-exit Type(e) \n\n3-Stop Type(s) \n\n4-Repeat Type(r)  \n\n5-max_window Type(maz)  \n\n6-min_window  Type(min)   \n\n7-Downlaod Type(d) \n\n\nPlease Type:  ")
    po1 = driver.find_element_by_class_name("song").text
    po1 = driver.find_element_by_class_name("song").text
    if next == "n":
        driver.find_element_by_xpath("""//*[@id="mp3_next"]""").click()
    if next == "e":
        break
    if next == "s":
        driver.find_element_by_xpath("""//*[@id="mp3_play"]""").click()
    if next == "r":
        driver.find_element_by_xpath("""//*[@id="mp3_repeat"]""").click()
    if next == "max":
        driver.maximize_window()
    if next == "min":
        driver.minimize_window()
    if next == "plus":
        driver.find_element_by_xpath("""//*[@id="mp3"]/div/div[3]/div[1]/div/div[3]/div[2]/div[2]/i[1]""")
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
        os.system("mv *.mp3 radiojavan_music")
driver.close()
