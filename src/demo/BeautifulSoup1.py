# coding=utf-8

import urllib.request
import re
from bs4 import BeautifulSoup

def main():
    url = "http://baike.baidu.com/view/284853.htm"
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    #print(soup)
    
    for each in soup.find_all(href = re.compile("view")):
        ## 'sep'.join(seq)
        ## sep：分隔符。可以为空
        ## seq：要连接的元素序列、字符串、元组、字典
        ## 上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串

        print(each)
        print( each.text, "-->", ''.join(["http://baike.baidu.com", each["href"]]) )
        print("---------------------------------------------------------------")

        
        
if __name__ == "__main__":
    main()