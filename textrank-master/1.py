#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import tkinter
import os
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import END
from bs4 import BeautifulSoup
import datetime
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from summa.summarizer import summarize
from summa.keywords import keywords
import requests
# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_experimental_option("detach", True)
article_url = "https://theconversation.com/no-one-saw-apps-coming-but-their-future-will-be-unmissable-44914"


def url_data(web_url):
    # dr = webdriver.Chrome(chrome_options=options)
    # dr.get(web_url)
    # WebDriverWait(dr,15,0.5,ignored_exceptions=None).until(
	# 		EC.element_to_be_clickable((By.XPATH,'//*[@id="article"]'))
    #         )
    r = requests.get(article_url)
    time.sleep(5)
    # source = dr.page_source.encode('GBK', 'ignore')
    # source = r.text
    # strsource = source.decode('GBK','strict')
    soup = BeautifulSoup(r.content)
    # print(soup)
    article_body = []
    
    article_html = soup.find('div', attrs={'itemprop' : 'articleBody'})
    # print(article_html)
    article_html_p = article_html.find_all('p')
    # print(article_html)
    for i in article_html_p:
        print(i)
        if(str(i).find("<strong>") == -1):
            print("append success")
            article_body.append(i.text)
        else:
            print("Failed")
    # print(article_body)
    auto(str(article_body))



def auto(article_data):
    print("Open text file")
    with open('text.txt', 'r', encoding='gbk', errors='ignore') as f:
        if f:
            print("Open Success")
        else:
            print("Open Failed")
        text = f.read()
        f.close()
        # print(text)
    summary = summarize(text, ratio=0.2, words=100)
    print(summary)
    words = summary.split()
    print("Summary's lenth is ",len(words))
    # summary_2 = summarize(summary, ratio=0.6)
    # print(summary_2)
    with open('summary.txt', 'w+', encoding='gbk', errors='ignore') as f:
        f.write(summary)
        f.close()


url_data(article_url)