# -*- encoding: utf8-*-

import time
import requests
import sys
from bs4 import BeautifulSoup

dataFile = open('all_articles.txt','w',encoding='utf8')
popFile = open('all_popular.txt','w',encoding='utf8')
# url = "https://www.ptt.cc/bbs/Beauty/index2662.html"
# re = requests.get(url)
# content = re.text
# soup = BeautifulSoup(content,'html.parser')
# article = soup.find_all(class_="r-ent")
# for i in range(0,len(article)):
#     subUrl = article[i].find('a')
#     date = article[i].find(class_="date")
#     tmpStr = ""
#     if (date != None):
#         # print(date.string[1]+date.string[3:5])
#         tmpStr = date.string[1]+date.string[3:5]+","
#     if( subUrl != None):
#         tmpStr += subUrl.text+","+"https://www.ptt.cc"+subUrl.get('href')
#         print(tmpStr,file=dataFile)
#         # dataFile.writelines(tmpStr)
#         # print(subUrl.text)
#         # print(subUrl.get('href'))
#         # print ("None")
#     print (tmpStr)
#     print (i)
#aTags = soup.find_all('a')
#print()

if sys.argv[1] == 'crawl':
    #
    # all article in 2017
    #
    for k in range(1992,2341):
        url = "https://www.ptt.cc/bbs/Beauty/index"
        url = url+str(k)+".html"
        print (url)
        re = requests.get(url)
        content = re.text
        soup = BeautifulSoup(content,'html.parser')
        article = soup.find_all(class_="r-ent")
        for i in range(0,len(article)):
            subUrl = article[i].find('a')
            date = article[i].find(class_="date")
            tmpStr = ""
            if (date != None):
                subDate = str(date.string).strip().replace("/","")
                if (k == 1992 and int(subDate)>1000) or (k == 2340 and int(subDate)<200):
                    continue
                tmpStr = subDate+","
            if( subUrl != None):
                if(str(subUrl.text).find("[公告]") == 0):
                    print("announcement")
                    continue
                tmpStr += subUrl.text+","+"https://www.ptt.cc"+subUrl.get('href')
                print(tmpStr,file=dataFile)
                pop = article[i].find(class_="hl f1")
                if(pop != None):
                    print(tmpStr,file=popFile)
    # dataFile.writelines(tmpStr)
    # print(subUrl.text)
    # print(subUrl.get('href'))
    # print ("None")
            print (tmpStr)
            print (i)
        time.sleep(0.5)





