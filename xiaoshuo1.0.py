import urllib.request
import time
import urllib.parse
import re
print("!起点中文网小说爬爬爬<~.~>")
name=input('请输入小说名字：')
ename={'kw':name}
qs=urllib.parse.urlencode(ename)
nameurl='https://www.qidian.com/search?'+qs
res1=urllib.request.urlopen(nameurl)
html1=res1.read().decode('utf-8')
st1=html1.find('<h4><a')+13
ed1=html1.find('" target',st1)
url2='https:'+html1[st1:ed1]+'#Catalog'
res2=urllib.request.urlopen(url2)
html2=res2.read().decode('utf-8')
order=re.search(r"共(\d){1,5}章",html2)
print(order)
print("                 "+order[0])
st3=html2.find('JumpUrl')+28
ed3=html2.find('" data-eid=',st3)
url='https:'+html2[st3:ed3]
chapter=int(input('请输入所需要的章节(篇)数：'))
for i in range(chapter):
    response=urllib.request.urlopen(url)
    html=response.read().decode('utf-8')
    a=html.find('content-wrap">')+14
    b=html.find('</span>',a)
    head=html[a:b]
    c=html.find('readContent">')+13
    d=html.find('</div>',c)
    body=html[c:d].replace('<p>','\r\n')
    m=html.find('chapterNext" href=')+19
    n=html.find('" data-eid=',m)
    nextchapter=html[m:n]
    url='https:'+nextchapter
    txtname=head+'.txt'
    article=head+body
    article=article.replace(u'\u2022', u' ')
    with open(txtname,"w") as f:
        f.write(article.replace(u'\xa0', u' '))
    print('已完成：'+head)
    time.sleep(1)
print('已全部加载完成！')

