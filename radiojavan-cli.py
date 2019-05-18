from selenium import webdriver
import time
import colored
import requests
import bs4
import os
import string
from colored import fore, back, style
import sys
import wget
import selenium.webdriver.opera
import pyfiglet
from selenium.webdriver.common.action_chains import ActionChains
ascii_banner = pyfiglet.figlet_format("                           Radiojavan-cli",font='digital')
print(ascii_banner)
print(fore.LIGHT_BLUE + back.BLACK+"                 |--------------------gun--linux------------------|"+style.RESET)
print(fore.LIGHT_BLUE + back.BLACK+"                 |-                                              -|"+style.RESET)
print(fore.LIGHT_BLUE + back.BLACK+"                 |-                                              -|"+style.RESET)
print(fore.LIGHT_BLUE + back.BLACK+"                 |-                                              -|"+style.RESET)
print(fore.LIGHT_BLUE + back.BLACK+"                 *------------------------------------------------*"+style.RESET)
print(fore.LIGHT_BLUE + back.BLACK+"                 |-              Nerd In the Life                -|"+style.RESET)
print(fore.LIGHT_BLUE + back.BLACK+"                 |-                                              -|"+style.RESET)
print(fore.LIGHT_BLUE + back.BLACK+"                 |-                                              -|"+style.RESET)
print(fore.LIGHT_BLUE + back.BLACK+"                 |-            📨telegram:@py_gnu                -|"+style.RESET)
print(fore.LIGHT_BLUE + back.BLACK+"                 *_____________🎷🎷🎷🎷🎷🎷🎷🎷🎷🎷______________*"+style.RESET)
time.sleep(4)
print("\n\nPlease wait a few moment...")
link = "https://www.radiojavan.com/playlists/playlist/mp3/854b87855624"
driver =webdriver.Chrome("/home/sti/down_git/chromedriver")
driver.get(link)
time.sleep(2)
playlist = []
#]driver.find_element_by_xpath("//input[@name='username']").send_keys(userName)
#driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
elem = driver.find_element_by_xpath("""//*[@id="navContainer"]/div/a[1]""")
actions = ActionChains(driver)
actions.click(elem).perform()
elem2 = driver.find_element_by_xpath("""//*[@id="playlist"]/div/div[1]/div/div[2]/a[2]""").click()
po = driver.find_element_by_class_name("artist").text
po1 = driver.find_element_by_class_name("song").text

os.system("clear")
try:
    while True:
        os.system("clear")
        next = input("\n\n                       ======>>>radiojavan-cli<<<=====\n0-)login in radiojavan Type(login)            \n1-)Next music Type(n) \n2-)Back muisc Type(b)  \n3-)Stop Type(s) \n4-)Repeat Type(r)  \n5-)max_window Type(max)  \n6-)min_window  Type(min)   \n6-)Downlaod Type(d) \n7-)Retry trying to download Type(trydl) \n8-)exit Type(e)\n9-)Muisc-Bio Type(bio) \n11-)list Artis Type(artist)  \n12-)New muisc  Type(new)   \n  \n\n>>> Please Type: ")
        # art = driver.find_element_by_xpath("""//*[@id="mp3"]/div/div[3]/div[1]/div/div[1]/div[1]/div/span[1]""").text
        # print(art)
        if next == "login":
            try:
                driver.find_element_by_xpath("""//*[@id="topBarMenu"]/button""").click()
                userName = input("Please Enter    email: ")
                password = input("Please Enter password: ")
                driver.find_element_by_xpath("""//*[@id="login_email"]""").send_keys(userName)
                driver.find_element_by_xpath("""//*[@id="login_password"]""").send_keys(password)
                login_bot = driver.find_element_by_xpath("""//*[@id="login_button"]""").click()
            except:
                print("Please sign up in radiojavan")
        if next == "like":
            try:
                driver.find_element_by_xpath("""//*[@id="mp3_likes"]/span""").click()
            except:
                print("Please login in radiojavan")
        if next == "clear":
            os.system("clear")
        if next == "bio":
            time.sleep(2)
        if next == "n":
            driver.find_element_by_xpath("""//*[@id="mp3_next"]""").click()
            os.system("clear")
        if next == "e":
            ascii_banners = pyfiglet.figlet_format("                           goodbay",font='digital')
            print(ascii_banners)
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
            try:
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
                time.sleep(1)
                wget.download(ok ,"radiojavan_music/"+str(po)+" "+str(po1)+".mp3")
                os.system("notify-send Downlaod-done✅")
                os.system("mkdir radiojavan_music")
                os.system("mv *.mp3 radiojavan_music")
                os.system("clear")
            except:
                print("Not Download Please Type(trydl)")
                time.sleep(3)
        if next == "artist":
            artis = driver.find_element_by_xpath("""//*[@id="navContainer"]/div/a[2]""").click()
            artis = input("Please Entern Type(>): ")
            if artis == ">":
                os.system("clear")
                cls = driver.find_element_by_xpath("""//*[@id="playlist_categories"]/div/a[9]""").click()
                cls = input("                            ==========>>>List Artis<<<========= \n\n1.Arash \n\n2.Sasy  \n\n3.Dariush \n\n4.Mohsen Chavoshi    \n\n5.Mohsen Yegane   \n\n6.Shadmehr Aghili   \n\n7.Sirvan khosravi       \n\n8.Moein    \n\n\nPlease Type(number):  ")
                if cls == "1":
                    dd = driver.find_element_by_xpath("""//*[@id="featured_playlist"]/div/a[1]""").click()
                    sr = input("Please Enter Type(play): ")
                    if sr == "play":
                        driver.find_element_by_xpath("""//*[@id="playlist"]/div/div[1]/div/div[2]/a[2]""").click()
                    os.system("clear")
                if cls == "2":
                    dd = driver.find_element_by_xpath("""//*[@id="featured_playlist"]/div/a[11]""").click()
                    sr = input("Please Type(play): ")
                    if sr == "play":
                        driver.find_element_by_xpath("""//*[@id="playlist"]/div/div[1]/div/div[2]/a[2]""").click()
                    os.system("clear")
                if cls == "3":
                    dd = driver.find_element_by_xpath("""//*[@id="featured_playlist"]/div/a[3]""").click()
                    sr = input("Please Type(play): ")
                    if sr == "play":
                        driver.find_element_by_xpath("""//*[@id="playlist"]/div/div[1]/div/div[2]/a[2]""").click()
                    os.system("clear")
                if cls == "4":
                    dd = driver.find_element_by_xpath("""//*[@id="featured_playlist"]/div/a[9]""").click()
                    sr = input("Please Type(play): ")
                    if sr == "play":
                        driver.find_element_by_xpath("""//*[@id="playlist"]/div/div[1]/div/div[2]/a[2]""").click()
                    os.system("clear")
                if cls == "5":
                    dd = driver.find_element_by_xpath("""//*[@id="featured_playlist"]/div/a[10]""").click()
                    sr = input("Please Type(play): ")
                    if sr == "play":
                        driver.find_element_by_xpath("""//*[@id="playlist"]/div/div[1]/div/div[2]/a[2]""").click()
                    os.system("clear")
                if cls == "6":
                    dd = driver.find_element_by_xpath("""//*[@id="featured_playlist"]/div/a[12]""").click()
                    sr = input("Please Type(play): ")
                    if sr == "play":
                        driver.find_element_by_xpath("""//*[@id="playlist"]/div/div[1]/div/div[2]/a[2]""").click()
                    os.system("clear")
                if cls == "7":
                    dd = driver.find_element_by_xpath("""//*[@id="featured_playlist"]/div/a[14]""").click()
                    sr = input("Please Type(play): ")
                    if sr == "play":
                        driver.find_element_by_xpath("""//*[@id="playlist"]/div/div[1]/div/div[2]/a[2]""").click()
                    os.system("clear")
                if cls == "8":
                    dd = driver.find_element_by_xpath("""//*[@id="featured_playlist"]/div/a[14]""").click()
                    sr = input("Please Type(play): ")
                    if sr == "play":
                        driver.find_element_by_xpath("""//*[@id="playlist"]/div/div[1]/div/div[2]/a[2]""").click()
                    os.system("clear")
        if next == "trydl":
            try:
                po = driver.find_element_by_class_name("artist").text
                link_rja="https://host2.rj-mw1.com/media/mp3/mp3-256/"
                ss = po
                ss = ss.replace(',', '')
                ss = ss.replace('&', '')
                ss = ss.replace('vs', '')
                ss = ss.replace('@', '')
                ss = ss.replace('*', '')
                ss = ss.replace('[', '').replace(']', '')
                mp = "-".join(ss.split())
                songs = po1
                songs = songs.replace(',', '')
                songs = songs.replace('[', '').replace(']', '')
                songs = songs.replace('{', '').replace('}', '')
                songs = songs.replace('*', '')
                songs = songs.replace('&', '')
                songs = songs.replace("/" , "")
                songs = songs.replace('vs', '')
                songs = songs.replace('@', '')
                md = "-".join(songs.split())
                mp3=".mp3"
                newstr = "-".join((mp, md))
                newstr.replace(" ", "")
                ok=link_rja+newstr+mp3
                print(ok)
                wget.download(ok ,"radiojavan_music/"+str(po)+" "+str(po1)+".mp3")
                time.sleep(3)
                os.system("mkdir radiojavan_music")
                os.system("mv *.mp3 radiojavan_music")
                os.system("clear")
            except:
                po = driver.find_element_by_class_name("artist").text
                link_rja="https://host1.rj-mw1.com/media/mp3/mp3-256/"
                ss = po
                ss = ss.replace(',', '')
                ss = ss.replace('&', '')
                ss = ss.replace('vs', '')
                ss = ss.replace('@', '')
                ss = ss.replace('*', '')
                ss = ss.replace('[', '').replace(']', '')
                mp = "-".join(ss.split())
                songs = po1
                songs = songs.replace(',', '')
                songs = songs.replace('[', '').replace(']', '')
                songs = songs.replace('{', '').replace('}', '')
                songs = songs.replace('*', '')
                songs = songs.replace('&', '')
                songs = songs.replace("/" , "")
                songs = songs.replace('vs', '')
                songs = songs.replace('@', '')
                md = "-".join(songs.split())
                mp3=".mp3"
                newstr = "-".join((mp, md))
                newstr.replace(" ", "")
                ok=link_rja+newstr+mp3
                print(ok)
                wget.download(ok ,"radiojavan_music/"+str(po)+" "+str(po1)+".mp3")
                os.system("notify-send Downlaod-done✅")
                time.sleep(3)
                os.system("mkdir radiojavan_music")
                os.system("mv *.mp3 radiojavan_music")
                os.system("clear")
        if next == "new":
             os.system("clear")
             artis = driver.find_element_by_xpath("""//*[@id="navContainer"]/div/a[2]""").click()
             ff = input("please Type (pop): ")
             if ff == "pop":
                 driver.find_element_by_xpath("""//*[@id="playlist_categories"]/div/a[5]""").click()
                 sd = input("New music Type(new): ")
                 if sd == "new":
                     driver.find_element_by_xpath("""//*[@id="featured_playlist"]/div/a[4]""").click()
                     sr = input("Please Type(play): ")
                     if sr == "play":
                         driver.find_element_by_xpath("""//*[@id="playlist"]/div/div[1]/div/div[2]/a[2]""").click()
        if next == "ls":
            os.system("ls radiojavan_music ")
            time.sleep(3)
except:
    print("please check install chromedriver (Line 26 Check and edit the chromedriver path) or run again")
driver.close()
