import requests
import time
from lxml import etree
def headers(n):
    header=[
{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
         'Referer':'https://www.55aqq.com/piclist/11/832-1.html'
        },{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
            'Referer':'https://www.55aqq.com/pic/820066_11.html'
        }
    ]
    return header[n]
def name(n):
    nam=n[63:70]
    return nam
url=input()
res=requests.get(url,headers=headers(0))

with open("gather.txt","w",encoding='utf-8') as f:
    f.write(res.content.decode('utf-8'))

parser=etree.HTMLParser(encoding='utf-8')

html=etree.parse("gather.txt",parser=parser)

divlist=html.xpath("//img/@src")


for div in divlist:
    pic=requests.get(div,headers=headers(1))
    with open(name(div),"wb") as f:
        f.write(pic.content)
    print(name(div))
    time.sleep(1)
print("已加载全部！")
