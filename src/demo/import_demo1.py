# coding=gbk

def func1():
    print("我是func1");
    
def test():
    print("开始测试...." + str(func1()));

#### 重点，这一句是为了让python知道，只有作为程序运行时才执行if下面的语句
if __name__ == "__main__":
    test();