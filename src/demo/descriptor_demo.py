# coding=gbk

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#######  描述符 (property方法 原理)
# 将某种特殊类型的类的实例指派给另一个类的属性
# 其中，"特殊类型的类"是指至少定义__get__()、__set__()、__delete() 三个方法中的任意一个
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

######################### 例1
class MyDescriptor:
    def __get__(self, instance, owner):
        print("__get__ >>> 用于访问属性，它返回属性的值", self, instance, owner);
        
    def __set__(self, instance, value):
        print("__set__ >>> 将在属性分配操作中调用，不返回任何内容", self, instance, value);
        
    def __delete__(self, instance):
        print("__delete__ >>> 控制删除操作，不返回任何内容");
        

class Test:
    x = MyDescriptor(); ### 将特殊类MyDescriptor（描述符）的实例，赋值给Test类的x属性


print("----------------------------------- 例1 begin -----------------------------");   
 
test = Test();

# __get__()
print(test.x);

#__set__()
test.x = "毛钇";

#__delete__
del test.x;

print("------------------------------------ 例1 end ------------------------------"); 
print();   
print(); 




######################### 例2
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# 根据描述符，实现property()方法
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class MyProperty:
    def __init__(self, myget, myset, mydel):
        self.myget = myget;
        self.myset = myset;
        self.mydel = mydel;
        
    def __get__(self, instance, owner):
        return self.myget(instance);
        
    def __set__(self, instance, value):
        self.myset(instance, value);
        
    def __delete__(self, instance):
        print("毛删除");
        self.mydel(instance);
        



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
    myproperty = MyProperty(getX, setX, delX);



print("----------------------------------- 例2 begin -----------------------------");   
c = C();

# 访问MyProperty，相当于调用getX
print(c.myproperty);

# 设置MyProperty，相当于调用setX
c.myproperty = 10;
print(c.myproperty);

# 删除MyProperty，相当于调用delX
del c.myproperty;
print(c.myproperty);

print("------------------------------------ 例1 end ------------------------------"); 
print();   
print(); 
















