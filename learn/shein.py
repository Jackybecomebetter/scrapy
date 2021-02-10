# -*- coding: utf-8-*-
import requests
from lxml import etree

if __name__ == "__main__":
    # url = "https://www.shein.com/user/auth/login?_lang=en"
    # url = "https://www.shein.com/user/index"
    url = "https://img.ltwebstatic.com/images3_pi/2020/12/18/16082942544a836602cd4f6245f1c3208b5ec9b4b3_thumbnail_220x293.webp"
    # header = {
    #     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    # }
    header = {
        # ':authority': 'www.shein.com',
        # ':method': 'POST',
        # ':path': '/user/auth/login?_lang=en',
        # ':scheme': 'https',
        # 'accept': '*/*',
        # 'accept-encoding': 'gzip, deflate, br',
        # 'accept-language': 'en-US,en;q=0.9',
        # 'canvas': 'Ny6AOxhsamgJbDaEFGDpuNtJlrRNgVQn',
        # 'content-length': '116',
        # 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '',
        # 'origin': 'https://www.shein.com',
        # 'referer': 'https://www.shein.com/user/auth/login',
        # 'smdeviceid': 'WHJMrwNw1k/EDRhXrNz02havVGVCj4LQTzLjiBe68gxRcLW4Y5glFaMS/jPdDvaTG05uG4+I1LMKtf8ZTj/F3RF8CBxsEebJQx3bvOoQ9weI1+djV4N+GQBRvPB5Vb+eRTZOJg5hGkZYfhwDCeHJsqFqRPoL7FhKirjl+d2XxfVhXtLse1/7YzpFZ8UT+V36ZNmwgTPXDoBVWrCipmMssb9YaSFlap+CIiDYKHVPenBw2kNF0emrW7C4Vc2T0mj05SBMZJRjFRB4=1487582755342',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Referer': 'https://www.shein.com/Tape-Crisscross-Tie-Back-Tank-Top-p-1933889-cat-1779.html?scici=navbar_WomenHomePage~~tab01navbar01menu01dir01~~1_1_1~~Special_dailyNew~~~~0~~50001'
        # 'webgl': 'Oaz0ggH3oLiCEhShRxAUBYWA6EHYQcGA',
        # 'x-csrf-token': 'GM7jX2aD-3gB8ksD8O5uBDGQ5FOuayivPrOc',
        # 'x-ftoken': 'b63ac90d7a9a1a1dbd110e992c589963',
        # 'x-requested-with': 'XMLHttpRequest'
    }
    response =  requests.get(url=url,headers=header)
    # print(response.cookies.get_dict())
    # print('\n\n')
    with open('./shein_login.jpg','wb') as fp:
        fp.write(response.content)

    # data = {
    #     'email': '1412165974@qq.com',
    #     'password': 'aaaa8885568',
    #     # 'challenge': 'ab7b8cac21fa8e593f6ee5c73fe92f4c',
    #     'challenge': '',
    #     'gtRisk': 'true',
    #     'clause_flag': '0'
    # }

    # playload_data = {
    #     pt: "110",
    #     w: "RP+juEIbMC7fQqB9VyN/FPLnPdT5QGGb04L9/Egyrx9FgWC6EB0QsBCZ4eZennIXwfFRMfE2Nx5lYR3yHFk1EP56ueDCvKozf9sog9I6ZKheKgFtZN77ul2tXHceMM90KRNhx6qxsfRLlFbok8KgmmWTZ4hNxDsqiVI3v5CfZj353jBXZw740eUox2bURLofzWStzYQf0OXKoCUj6eesqc35HWYdHa7BiURWpbmn1SqXgRejUfj85i4+Nc4MvpWF27SgCGezLjRNvHZwBOIyi1RlJsBvaW0JDMJMoMpTwltjoFLpgtBbxW20AyHuODRKB3frJ2ARp9ycR/oxvw99yCgEclPZlpejNYUK5MOHDbWOXFfxP8zBUNkIrNPG/d84tozUQYiet9EQR5vyrXdUKhn/m8Khdbo1p99KzvjxFHcFprHv7SBhIrc3mfEUtIRqGymiDkRNV4sJNIEM3X+XcuOtgQzqRWNtgtTjmTensYimzfOYclq02HyxlAjGFJFHEDnkbUFTKXiUvpv6l5OTp2gs+Fyc+YWEPLL9iIazq8RThJefB3V+VLorIYlo9PZvvJSj7yjwFYFZeUy5VOGnkAKlkkiFiU88s6AgqX5kYf9lrucz51/M9QWmte1AOG6N4bIvZFf1ypUU4yIEGKMju8MfoZWf9f3/cH2Daw664o3Dfi9BJdK/tKzIfRkTgvf1YInV45ynq2JMaio+Bfl2ItL47OgM536MPib5ufIeiUylN7JPratxufmKdPZKVcA/sJcBy35fbKzHuMcjAtQsXU72/E7wKZMPFSFiFaG7Ge4BO3jaC8W4Xi/CZO38hVGvrwU0kj4ZYiLSFAEi2KnUwy1h/hx+gOPmPEMnhjUQzhbzsNvAzHGiujVihK+/eWkZ41A877J8dhj5+jBXEc2KI2SkcPtb+euQ8M0aKctIwB+hz7W1n+e0UZpTBUxr8n8z40+84j6+dC8pGuctClWkv0VGVjoPtCO0PsAlGUUhU2iu3g2p062FYLsBmmiBViSIxwNfAKnDiHfk9RGRiA6x+RFttJ3VyYEX99d3PHnKE4shtxHxc22nYDvLdcUBGkPV9bwHR3w3lYAkGD76enOD0CzLlPutqWK9UIqZbkRIeavP2PDnwGBjL5qKAxiwzn4E/2PCuqXyLghhz25Fm9+NKZuLFEbLAHnke0uCmKkbtspxcpfDSkBoOr5gIVK53+YDtXiCxFLow5JX+Bd2b16ndDiXzLmEcdBCrBb8mTRP83sYli312hk5HZdtYXhEF5v4ZlszEavRO2b2zTh5Buu+6ciMIRUPa+Krt1RJA0P0UjWITqaySK8DnfJeFDqhjkW/Xv/6fzNiVG8dAwO0+Nmtkvvue6ZkCjFwu/1E4CdhfrfXVdBTg5pa9O+w0rdK94InbjmOQOfyYi/QJqTK/CCUttJ4H1Ybd8Zsa1pMfiv+1FgeNByUKKLGbd2eHeVk9kRU7DklsCtb2lzRz1l60n1fOXX6IaipDMT1T3NPyBnz5ye3LDiDkSqvk4qzNdidPijUflgwpueD/HZWBelzokN5Ej+DmbpnCFaOJdk/+cb4jZgS/MuRtACbuQYPPy2mr+cqdBLQsJzx9sw4Cf5SkjKDziIND0jVXLM/KePS+8j5oz58mi5ycElt/6fXITSnB92AQ3pInXizsYYPBCzmVut4ahZQM9ZFXp6JpumGSLLEhqzUhhhk/kU0hvtEnOjtIa3y/BUwyXOhuouL5bvbJkPvWXFISNv+WPoSjRpzatGylYU2dPcPtIQzOtSUgaWIuR32HP6+FmZ3OCIx2v7iJMBHHE1Sci82IjP9mNcoQ9yR6M2CXyh/3Pk53K+cz/79nFJ0Yarg/g2RTJXri54brsRM2TQVQJTDiywd6Srb9RWQPXyDM3RnflOGi5nYZo847F5qZF/sYFFKnHIz+HkfK9ecykURRu2zXmvRuuyJUpm6u8WJtzPfmefs2pSNf2Op+uTJZU2Zh71BNAFPqfXEg0vg1dNvoK//Lr/E+uqgr5Sbs5T9QnYCoeeNBpwOQvJ46tqC15gzHztYap1RXdkHFyUcNoyg1By+AmKY6l5osKdRpqarUFiwNxAkHKibsuMgv+ggsD5mH+g6sNrqcLNO9GFZ9Q=="
    # }

    # login_text = requests.post(url=url,data=data,headers=header)
    # print(login_text.status_code)
    # with open('./shein_login.txt','w',encoding='utf-8') as fp:
    #     fp.write(login_text.text)
    
