# -*- coding: utf-8-*-
import requests
import json

if __name__ == "__main__":

    # # 1. 爬取搜狗首页的页面数据 : 指定url,发送请求，获取响应对象，持久化存储
    # url = "https://www.sogo.com/"
    # response = requests.get(url=url)
    # page_text = response.text
    # with open("./sogou.page","w",encoding="utf-8") as fp:
    #     fp.write(page_text)

    # 2. 使用搜索引擎搜索，并且获取搜索到的网页 
    # 当使用到url中某个参数的时候，把该参数对应的关键词封装成字典，并且输入到request.get的params字段当中
    # ＵＡ伪装：user agent 伪装，伪装成浏览器
    # 如果这里没有伪装浏览器的话，有可能对应的网站会把这个请求当成是爬虫的请求，无法正确的接收数据       
    # key_word = input("input a key word\n")
    # header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    # param = {"wd" : key_word}
    # url = "https://www.baidu.com"
    # response = requests.get(url=url,params=param,headers=header)
    # page_text = response.text
    # print(page_text)

    # 3. 获取百度翻译的结果
    # 阿贾克斯请求（ajax）：　无需请求整个页面，只是更新页面的部分信息，请求获取部分信息进行更新。
    # 如何判断是不是阿贾克斯请求：当网页数据刷新的时候，浏览器中的网址没有变化，这就是一个阿贾克斯请求，通过发送其他的请求去获取更新的数据
    # 　
    # (1)发送携带参数的post请求
    # (2)响应数据是json格式的数据（这里是从网页源码的response和response headers的content-type得到
    url = "https://fanyi.baidu.com/sug" # 这个ｕｒｌ是使用f12通过network下面的ＸＨＲ过滤，找到对应的请求发送的url和回复信息
    search_word = input("input a english word\n")
    header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    data = {"kw":search_word}
    response = requests.post(url=url,data=data,headers=header)

    result = response.json()
    with open("./baidufanyi","w",encoding="utf-8") as fp:
        json.dump(result,fp=fp)
    print(result)

    # 4. 豆瓣电影排行榜获取