# coding=utf-8

import urllib.request
import re
import urllib.parse
from bs4 import BeautifulSoup

from urllib.parse import quote
import string

def main():
    keyword = input("输入关键词：")
    keyword = urllib.parse.urlencode({"word" : keyword})
    
    url = "http://baike.baidu.com/search/word?%s" %keyword
    #print("url : ", url)
    
    response = urllib.request.urlopen(url)
    html = response
    soup = BeautifulSoup(html, "html.parser")
    
    for each in soup.find_all(href = re.compile("view")):
        content = "".join([each.text])
        print("content 初始 --> ", content)
        
        url2 = "".join(["http://baike.baidu.com", each["href"]])
        print("url2 中文 --> ", url2)
        url2 = quote(url2,safe=string.printable)
        print("url2 --> ", url2)
        
        response2 = urllib.request.urlopen(url2)
        html2 = response2.read()
        soup2 = BeautifulSoup(html2, "html.parser")
        
        if soup2.h2:
            print("h2 --> ", soup2.h2)
            content = "".join([content, soup2.h2.text])
        
        content = "".join([content, " >>>>>> ", url2])
        print(content)
        
        
        print("=============================================================================================")
        print()
        








if __name__ == "__main__":
    main()