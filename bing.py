#!/bin/python3
# code by Dinar fb.com/dinar1337
import requests
import re

def search(dork):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0'}
        maxs = 300
        for x in range(1,maxs):
            np = x * 10
            req = requests.get("http://www.bing.com/search?q=" + dork + "&first=" + str(np), headers=headers)
            result = re.findall('<h2><a target="_blank" href="(.*?)"',str(req.content))
            for i in result:
                o = i.split('/')
                print(o[2])
                save(o[2])
    except Exception as e:
        print(e)
    except ConnectionError as e:
        print(e)

def save(ss):
    s = open('result.txt', 'a+')
    for u in ss:
        s.write(u + "\n")
    s.close()

s = input('INPUT ANJING: ')
search(s)
