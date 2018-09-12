# coding=utf-8

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#### 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def main():
    high = int(input("下落高度：\n"))
    count = int(input("下落次数：\n"))
    mcount = count
    
    downProcess = [high]
    count = count - 1
    
    while count > 0:
        high = high / 2
        downProcess.append(high)
        count = count - 1
     
    print()    
    print("路径经历：", downProcess)
    print()
        
    distance = 0.0
    
    for dis in downProcess:
        distance = distance + dis
    
    print()
    print(mcount, "次落地时，共经过：", distance, "米")
    print("在第", mcount, "次落地时反弹高度为：", downProcess[mcount - 1])
    
    
if __name__ == "__main__":
    main()  

