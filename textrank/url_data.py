#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
from bs4 import BeautifulSoup
from summa.summarizer import summarize
from summa.keywords import keywords
import requests
article_url = "https://theconversation.com/surgical-corsets-respirators-a-new-exhibition-showcases-the-art-hidden-in-medical-devices-147087"


def url_summary(web_url, words_limit):
    r = requests.get(web_url)
    time.sleep(5)
    soup = BeautifulSoup(r.content)
    article_body = ""
    article_html = soup.find('div', attrs={'itemprop' : 'articleBody'})
    article_html_p = article_html.find_all('p')
    for i in article_html_p:
        # print(i.text)
        if(str(i).find("<strong>") == -1):
            # print("append success")
            article_body += i.text
    summary = summarize(str(article_body), ratio=0.2, words=words_limit)
    words = summary.split()
    # print(summary)
    return summary, len(words)



# url_summary(article_url, 100)