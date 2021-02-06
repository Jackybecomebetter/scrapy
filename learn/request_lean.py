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

    # # 3. 获取百度翻译的结果
    # # 阿贾克斯请求（ajax）：　无需请求整个页面，只是更新页面的部分信息，请求获取部分信息进行更新。
    # # 如何判断是不是阿贾克斯请求：当网页数据刷新的时候，浏览器中的网址没有变化，这就是一个阿贾克斯请求，通过发送其他的请求去获取更新的数据
    # # 　
    # # (1)发送携带参数的post请求
    # # (2)响应数据是json格式的数据（这里是从网页源码的response和response headers的content-type得到
    # url = "https://fanyi.baidu.com/sug" # 这个ｕｒｌ是使用f12通过network下面的ＸＨＲ过滤，找到对应的请求发送的url和回复信息
    # search_word = input("input a english word\n")
    # header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    # data = {"kw":search_word}
    # response = requests.post(url=url,data=data,headers=header)

    # result = response.json()
    # with open("./baidufanyi","w",encoding="utf-8") as fp:
    #     json.dump(result,fp=fp)
    # print(result)

    # 4. 国家药品监督局信息　（通过对网页进行分析，发现不同的公司详情页对应的ｕｒｌ通过ｉｄ进行区分，所以可以通过ｉｄ值去获取不同公司详情页的ｕｒｌ）
    # (1)动态加载数据
    # (2)阿贾克斯动态请求
    #　
    #  如何验证某个url获取到的数据是静态的页面还是动态加载的（静态就是通过ｕｒｌ可以直接获取所有网页看到的数据，动态就是ｕｒｌ只是一个简单的框架，里面的数据还通过阿贾克斯请求进行动态加载）
    # (1)抓包：　通过网页源码，进入network，选择ａｌｌ，然后ｃｌｅａｒ所有原来的数据，再重新刷新。然后找到对应的请求（该网页ｕｒｌ的请求），在ｒｅｓｐｏｎｓｅ里面看是否能找到我们想要的信息
    # (2)爬虫
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    detail_url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    list_json = []
    id_data = {"id": ""}
    for page in range(1,369):
        
        data = {
            "on": "true",
            "page": str(page),
            "pageSize": "15",
            "productName": "",
            "conditionType" : "1",
            "applyname" : "",
            "applysn" : "" ,
        }
        # 获取id
        response = requests.post(url=url,data=data,headers=header)
        json_ids = response.json()
        # print(json_ids)

        # 对每个每个ＩＤ单独取出来，配置成对应的详情页的阿贾克斯请求
        for ids in json_ids["list"]:
            id_data["id"] = ids["ID"]
            response = requests.post(url=detail_url,headers=header,data=id_data)
            # print(response.json())
            list_json.append(response.json())
        
        print("compelete %.3f" %(page / 368 * 100) , "%")
    
    with open("./yaopinjianduju","w",encoding="utf-8") as fp:
        fp.write(list_json.__str__())