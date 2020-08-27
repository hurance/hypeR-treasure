import requests
from lxml import etree
import re
import string
def delse(string,r,l):          #去首尾
    result=string.rstrip(r).lstrip(l)
    return result
def foundorder(t):
    num=re.search("(\d){1,3}",t)
    return num[0]
def cut(string):
    m=string.find(">")+1
    n=string.find("<",m)
    result=string[m:n]
    return result
def founddate(string):
    date=re.search("(\d){1,2}月(\d){1,2}",string)
    return date[0]
linkname={}
url='https://maoyan.com/'

head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'Referer':'https://maoyan.com/',
    'Cookie':'uuid_n_v=v1; uuid=5E059070E75911EA96A68775497B19D8EEEF482A6D0E4DCDB9A5468B42846CE4; _csrf=3641e591c9fc79cfca45c66f12f5b0b5e5653dcd917aaf6a89f82b8f5faac9e6; mojo-uuid=a279d21d5585dd8c8074b5bf2c779342; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1598418168; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; _lxsdk_cuid=1742925af31c8-064337d4491273-3323766-130980-1742925af31c8; _lxsdk=5E059070E75911EA96A68775497B19D8EEEF482A6D0E4DCDB9A5468B42846CE4; recentCis=845%3D1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598418752; __mta=19234311.1598418169733.1598418377871.1598418752512.5; _lxsdk_s=17429a09adc-b3c-d8-fb1%7C%7C1',
      'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'Host':'maoyan.com'
      }
res=requests.get(url,headers=head)
with open("moviedoc.txt","w",encoding='utf-8') as f:
    f.write(res.content.decode('utf-8'))
parser=etree.HTMLParser(encoding='utf-8')
html=etree.parse("moviedoc.txt",parser=parser)

title1=html.xpath("//h2")[5]

res1=etree.tostring(title1,encoding='utf-8').decode('utf-8')

res1=delse(res1,'</h2>','<h2>')
print(res1)

print("(最多显示8个)")

body1=html.xpath("//div/@title")

if int(foundorder(res1))>8:
    filmnum=8
else:
    filmnum=int(foundorder(res1))

for i in range(1,filmnum+1):
    print(str(i)+'.'+body1[i-1])
print()

'''title2=html.xpath("//h2")[6]

res2=etree.tostring(title2,encoding='utf-8').decode('utf-8')

res2=delse(res2,'</h2>','<h2>')

print(res2)

for i in range(1,int(foundorder(res2))+1):
    print(str(i)+'.'+body1[i+int(foundorder(res1))])'''

link=html.xpath("//dd/div/div/a/@href")

for i in range(filmnum):
    link[i]='https://maoyan.com'+link[i]
    linkname[body1[i]]=link[i]
for i in range(100):
    getname=input("请输入想要查询电影:")

    print()
    print("可选日期:")

    res5=requests.get(linkname[getname],headers=head)
    with open("datepage.txt","w",encoding='utf-8') as f:
        f.write(res5.content.decode('utf-8'))
    parser=etree.HTMLParser(encoding='utf-8')
    html3=etree.parse("datepage.txt",parser=parser)
    dateall=html3.xpath("//ul/li/a[@data-bid='b_beyqev3w']")
    for i in range(len(dateall)):
        res6=etree.tostring(dateall[i],encoding='utf-8').decode('utf-8')
        res6=founddate(res6)
        print("     "+str(i+1)+"."+str(res6))

    print()
    
    date=input("请输入查询日期(格式:**-**):")
    nextlink=linkname[getname]+'&showDate=2020-'+date

    res2=requests.get(nextlink,headers=head)
    with open("purchasepage.txt","w",encoding='utf-8') as f:
        f.write(res2.content.decode('utf-8'))

    parser2=etree.HTMLParser(encoding='utf-8')
    html2=etree.parse("purchasepage.txt",parser=parser2)

    print("影院列表:")

    place=html2.xpath("//div/a[@class='cinema-name']")
    adress=html2.xpath("//div/p[@class='cinema-address']")

    for i in range(len(place)):
        res3=etree.tostring(place[i],encoding='utf-8').decode('utf-8')
        res4=etree.tostring(adress[i],encoding='utf-8').decode('utf-8')
        print("    "+str(i+1)+"."+cut(res3))
        print("    "+cut(res4))
        print()














