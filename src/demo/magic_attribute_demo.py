# coding=gbk

''''''''''''''''''''''''''''''''''''''
#######  属性相关的魔法方法
from builtins import setattr
''''''''''''''''''''''''''''''''''''''


class C:
    def __getattribute__(self, name):
        print("__getattribute__ >>> 当该类属性被访问时触发");
        return super().__getattribute__(name);
    
    def __setattr__(self, name, value):
        print("__setattr__ >>> 当该类属性被设置时触发");
        super().__setattr__(name, value);
        
    def __delattr__(self, name):
        print("__delattr__ >>> 当该类属性被删除时触发");
        super().__delattr__(name);
        
    def __getattr__(self, name):
        print("__getattr__ >>> 当用户视图获取一个该类不存在的属性时触发");

c = C();

# 获取属性 and 获取一个不存在的属性
c.x;
print();

# 设置属性
c.x = 1;
setattr(c, "y", 500);   ## 内建函数BIF
print();


# 删除属性
del c.x;
delattr(c, "y");   ## 内建函数BIF
print();



