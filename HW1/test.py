# -*- encoding: utf8-*-

import time
import requests
import sys
from bs4 import BeautifulSoup


if sys.argv[1] == 'crawl':
    dataFile = open('all_articles.txt','w',encoding='utf8')
    popFile = open('all_popular.txt','w',encoding='utf8')
    #
    # all article in 2017
    #
    for k in range(1992,2341):
        url = "https://www.ptt.cc/bbs/Beauty/index"
        url = url+str(k)+".html"
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
                    continue
                tmpStr += subUrl.text+","+"https://www.ptt.cc"+subUrl.get('href')
                print(tmpStr,file=dataFile)
                pop = article[i].find(class_="hl f1")
                if(pop != None):
                    print(tmpStr,file=popFile)
        time.sleep(0.5)
    dataFile.close()
elif sys.argv[1] == 'push':
    try :
        dataFile = open('all_articles.txt','r',encoding='utf8')
        start = str(sys.argv[2])
        end = str(sys.argv[3])
        if( int(start) > int (end) ):
            raise EOFError('[Error] \"Start date must small than end date\"')
    except FileNotFoundError as e:
        sys.exit()
    except IndexError as e:
        sys.exit()
    except EOFError as e:
        sys.exit()

    fileName = "push["+str(start)+"-"+str(end)+"].txt"
    pushFile = open(fileName,'w',encoding='utf8')
    lineList = list(dataFile)
    UrlList = list()
    for i in lineList :
        tmp = str(i).split(',')
        if(int(tmp[0]) >= int(start) and int(tmp[0]) <= int(end)):
            UrlList.append(str(tmp[-1]).replace('\n',''))
    
    likeCount = 0
    booCount = 0
    likesDict = dict()
    boosDict = dict()
    for Url in UrlList :
        re = requests.get(str(Url))
        content = re.text
        soup = BeautifulSoup(content,'html.parser')
        pushes = soup.find_all(class_="push")
        # likes = soup.find_all(class_="hl push-tag")
        # likeCount += len(likes)
        for push in pushes :
            name = push.find(class_="f3 hl push-userid")
            if(name == None):
                continue
            boo = push.find(class_="f1 hl push-tag")
            if (boo == None):
                if str(name.string) not in likesDict :
                    likesDict.update( { str(name.string) : 1} )
                else :
                    likesDict.update( { str(name.string) : likesDict[str(name.string)]+1 } )
                likeCount += 1
            elif (boo.string == "噓 ") :
                if str(name.string) not in boosDict:
                    boosDict.update( { str(name.string) : 1 } )
                else :
                    boosDict.update( { str(name.string) : boosDict[str(name.string)]+1 })
                booCount += 1
        time.sleep(0.1)

    print("all like: "+str(likeCount),file = pushFile)
    print("all boo: " +str(booCount),file =pushFile)
    boosDict = dict(sorted(boosDict.items(),key =lambda d: d[0]))
    sorted_boos_dict = sorted(boosDict.items(),key =lambda d: d[1],reverse=True)
    likesDict = dict(sorted(likesDict.items(),key =lambda d: d[0]))
    sorted_likes_dict = sorted(likesDict.items(),key =lambda d: d[1],reverse=True)
    for i in range(0,10,1):
        print("like #"+str(i+1)+": "+str(sorted_likes_dict[i][0])+" "+str(sorted_likes_dict[i][1]),file=pushFile)
    for i in range(0,10,1):
        print("boo #"+str(i+1)+": "+str(sorted_boos_dict[i][0])+" "+str(sorted_boos_dict[i][1]),file=pushFile)






