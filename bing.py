import requests
import json
import time
import datetime
import os
from pathlib import Path
mktlist = ["en-US", "zh-CN", "ja-JP", "de-DE"]

proxies = {'http': 'http://127.0.0.1:7890',
               'https': 'http://127.0.0.1:7890',
           }

bingdomain = "https://cn.bing.com"

for dirname in mktlist:
    if not Path("./"+dirname).is_dir():
        os.makedirs(dirname)

while True:
    for mkt in mktlist:
        jsonurl = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=" + mkt
        dljson = requests.get(jsonurl, proxies=proxies).text
        dict = json.loads(dljson)
        image = bingdomain + dict['images'][0]['url']
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"  "+dict['images'][0]['enddate']+" "+ mkt)
        with open("./"+mkt+"/"+dict['images'][0]['enddate']+" "+mkt+".png","wb") as file:
            file.write(requests.get(image).content)
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"  "+"sleep 1 day")
    time.sleep(72000)















