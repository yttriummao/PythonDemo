# coding=gbk

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#######  计时器

# property()方法：返回一个可以设置属性的属性
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


class C:
    def __init__(self):
        self.x = 0;
    
    def getX(self):
        return self.x;
    
    def setX(self, value):
        self.x = value;
        
    def delX(self):
        del self.x;
        
    ### property 方法
    MyProperty = property(getX, setX, delX);
    

c = C();

# 访问MyProperty，相当于调用getX
print(c.MyProperty);

# 设置MyProperty，相当于调用setX
c.MyProperty = 10;
print(c.MyProperty);

# 删除MyProperty，相当于调用delX
del c.MyProperty;
print(c.MyProperty);









