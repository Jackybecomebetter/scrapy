### 一、什么是爬虫

#### １、什么是爬虫

　　爬虫：通过编写代码，模拟浏览器上网，去互联网中抓取目标数据的过程。

​		爬虫价值：通过爬取互联网海量的高价值数据，构建数据银行，让这些数据为我们所用，建立数据商品化和产品化。

#### 2、爬虫的合法性

（１）法律不禁止爬虫

（２）具有违法风险（利用爬虫攻击某个网站或者通过非法接口获取网站的后台数据）

**爬虫的风险主要体现两个方面：**

（１）干扰了被访问网站的正常运营　（时常优化自己的爬虫）

（２）爬虫抓取了收到法律保护的私密数据或者信息

### 二、爬虫介绍

#### 1、爬虫分类

（１）通用爬虫：　爬去整个页面。

（２）聚焦爬虫：	爬取页面的局部数据。

（３）增量式爬虫：　检测网站中最新更新的数据。

#### ２、爬虫的反爬虫机制和反反爬机制

（１）反爬虫机制：　制定策略和技术手段，防止爬虫程序抓取数据。

（２）反反爬虫机制：　爬虫通过制定策略和技术手段，以破解门户网站的反爬虫机制，获取相关的数据。

#### ３、robots.txt 协议（君子协议）

（１）规定网站哪些数据可以被爬取，哪些不能爬取。

### 三、http和https协议常见字段

#### １、常用的请求头

user-agent：　请求方的身份标识

connection：　是否长连接

#### 2、常用的响应头

content-type：服务器响应的数据类型

### 四、相关python网络库

#### １、requests

python中原生的基于网络请求的模块，功能强大，使用简单、高效。

**作用：模拟浏览器发送请求**

（１）如何使用

指定url　——>　发起请求　——> 获取相应数据　——> 数据解析——> 持久化存储

（２）安装

```
pip install requests
```

#### 2、数据解析

**原理：**我们需要的局部内容存储在标签之间或者是标签对应的属性值之中进行存储。

主要通过两个步骤：

步骤１：进行指定标签的定位。

步骤２：对标签或者标签对应的属性中存储的数据值进行提取（解析）

##### （１）正则表达式

##### （２）bs4

安装：

```
pip install bs4
pip install lxml
```



**解析原理：**

a 实例化一个beautifulSoup对象，并且把页面数据加载到该对象当中。

from bs4 import BeautifulSoup

对象实例化：

​		fp = open('.test.html','r',encoding='utf-8')

​		soup = BeautifulSoup(fp,'lxml')

​		

​		page_text = response.text

b 通过调用beautifulSoup对象中相关的属性和方法进行标签定位和数据提取。

**提供数据解析的方法：**

1）soup.tapName (这里的tagName就是html中第一个tagName对应的标签内容)

２）soup.find(tagName) 　等同于　1)

soup.find(tagName,class=className)：找出第一个带有className属性的tagName标签

3）soup.find_all(tagName)

4）soup.select(’某种选择器，可以是id, class, 标签...‘)，返回的是一个符合选择器要求的列表

soup.select('.tang > url > li > a')	：　层级选择器，选择tang标签下面的url再下面的a标签

soup.select('.tang > url a')　：　空格跳过li层级，选择a层级

５）获取标签之间的文本数据：

​	soup.a.text/string/get_text()：获取a标签的属性

​	text/get_text()：获取该标签下面的所有文本内容

​	string：只获取该标签的直系内容



##### （３）xpath

**xpath：**最常用，最方便的一种解析方法，同时通用性也很强，多种语言都可以适用。

**xpath安装:**

```
pip instal lxml
```



**xpath的解析原理：**

1)　实例化一个etree对象，同时把从互联网获取的数据加载到etree对象当中。

```python
from lxml import etree
object = etree.parse(filepath) # 从本地html文件进行加载
object = etree.HTML(page_text) # 从互联网获取的源码数据进行加载
```

2)　调用etree对象的xpath方法，结合xpath表达式实现标签的定位和内容的捕获。

```python
object.xpath('xpath表达式')	# 模板
object.xpath('/html/head/title')	# 根标签定位：从根标签节点路径加载，这里的/html表示html是跟标签，如果有多个符合该表达式的标签，会用列表进行存储
object.xpath('//div')	#　//　多个层级定位：表示div标签前面有多个层级
object.xpath('//div[@class="song"]')	# 属性定位：表示找到多个div后，选择某个div属性值是song的div标签数据　//tagName[@class='song']
object.xpath('//div[@class="song"]/p[3]')	# 索引定位：获取到属性值为song的div标签下面的p标签的第三个标签的数据
object.xpath('//div[@class="song"]/p[3]/text()')	# /text()，取直系标签文本内容
object.xpath('//div[@class="song"]/p[3]//text()')	# //text()，取该标签下面的所有文本内容，包括所有子标签的文本内容
object.xpath('//div[@class="song"]/p[3]/＠attrName')		#　取属性值
```

www.aqistudy.cn/historydata/



#### 3、验证码识别

（１）为啥需要验证码识别？

在登录的时候，很多时候网站为了反爬虫，设置了验证码。我们在设计爬虫的时候，如果遇到需要验证码才能登录的网站就需要对验证码进行识别，跳过网站验证获取数据。

（２）如何识别验证码

人工识别：不推荐

第三方线上平台：推荐

（３）第三方验证码识别线上平台

云打码平台



#### 4、模拟登陆

（１）为啥要登录？

a. 有的时候需要获取登录用户的个人信息

b. 有些页面只有登录之后，才能进行获取相关的信息

（２）手工登录的流程

a. 点击登录按钮之后会发起一个post请求

b. post请求会携带在登录界面用户录入的相关登录信息（用户名、密码、验证码等等）

（３）编程流程

a. 如果有验证码的话，获取验证码对应的文字数据

b. 发送post请求（携带用户名、密码、验证码...）

ｃ、对响应数据进行持久化存储



