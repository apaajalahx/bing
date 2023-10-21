#!/bin/python3
from selenium import webdriver
import re

def save(text):
    z = open('result-bing.txt', 'a+')
    z.write(text + "\n")
    z.close()

def reg(source, page):
    search = re.findall("<cite>(.*?)</cite>", source)
    if len(search) > 0:
        print("GET {} DOMAIN FROM PAGE {}".format(len(search), str(page)))
        save("\n".join(search))

def main(dork):
    for x in range(0,300):
        np = (x * 10) + 1
        driver = webdriver.Chrome()
        driver.get('https://www.bing.com/search?q='+ dork +'&first='+str(np)+'&rdr=1&rdrig=7784A68910F94CDE9DFA1DBF740D3A29')
        reg(driver.page_source, np)
        driver.close()
    driver.quit()

z = input("DORK : ")
main(z)
