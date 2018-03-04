'''
豆瓣top250的爬取存储
显示爬去进度条
三部分：
1获取html
2找到所有li
3打印所有内容
4保存文件
'''
import requests
from bs4 import BeautifulSoup
import time

def getHtml(url):
    try :
        kv = {'user-agent': 'Mozilli/5.0'}
        r = requests.get(url, kv)
        r.status_code
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getNeed(list,listLinks,html):
    soup = BeautifulSoup(html,"html.parser")
    items = soup.find_all("li")
    for item in items :
        t = item.find("span",{"class":"title"})
        score = item.find("span",{"class":"rating_num"})
        links = item.find("a")
        if t is not None:
            listLinks.append(links["href"])
            list.append([t.get_text(),score.get_text()])

def printNeed(list,listLinks):
    tplt = "{0:^5}\t{1:{3}^15}\t{2:^10}\t"
    print(tplt.format("排名","名字","评分",chr(12288)))
    cout = 0
    for i in range(len(list)):
        cout = cout + 1
        u = list[i]
        print(tplt.format(cout,u[0], u[1], chr(12288)))
        print(listLinks[i])

'''
打开链接获取内容数据，以国家等信息
'''

if __name__ == "__main__":
    url = "https://movie.douban.com/top250"
    fpath = "D:/"
    list = []
    listLinks = []
    for i in range(20):
        url1 = url +"?start="+str(i*25)
        html = getHtml(url1)
        getNeed(list,listLinks,html)
        time.sleep(2)
    printNeed(list,listLinks)






