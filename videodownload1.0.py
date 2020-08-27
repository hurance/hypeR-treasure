import sys
from you_get import common as you_get       #导入you-get库
print("welcome to use bilibili video downloader!")
print("默认下载路径为C盘bilibili video")
directory=r'C:\bilibili video'
n=int(input("请输入需要下载视频的个数:"))
for i in range(n):
    url=input('请输入需要下载视频的url:')  
    sys.argv = ['you-get','-o',directory,url]       #sys传递参数执行下载，就像在命令行一样
    you_get.main()
