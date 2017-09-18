#!usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import time
def getHTMLText(url):
    try:
        res = requests.get(url,timeout=30)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        return res.text
    except:
        return "error"

def main():
    url = "http://www.baidu.com"
    start = time.clock()
    # for i in range(100):
    getHTMLText(url)
    end = time.clock()
    run_time = end - start
    print (run_time)


if __name__ == "__main__":
    main()
