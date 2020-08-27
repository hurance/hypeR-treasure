import urllib.request as a
import urllib.parse as b
import json
for i in range(100):
    content=input("请输入需要翻译的内容：")
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    head={}
    head['user-agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    data={}
    data['i']=content
    data['from']=' en'
    data['to']=' zh-CHS'
    data['smartresult']=' dict'
    data['client']='fanyideskweb'
    data['salt']='15973948109720'
    data['sign']= 'fb00f85bdf7badcc641e0e508548c771'
    data['lts']=' 1597394810972'
    data['bv']=' 9ef72dd6d1b2c04a72be6b706029503a'
    data['doctype']='json'
    data['version']=' 2.1'
    data['keyfrom']='fanyi.web'
    data['action']=' FY_BY_CLICKBUTTION'
    data=b.urlencode(data).encode('utf-8')
    rep=a.Request(url,data,head)
    response=a.urlopen(rep)
    html=response.read().decode('utf-8')
    target=json.loads(html)
    print("翻译结果: %s" %(target['translateResult'][0][0]['tgt']))
    
