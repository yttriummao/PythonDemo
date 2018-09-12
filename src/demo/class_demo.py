# coding=gbk

import random as R;

''''''''''''''''''''''''''''''''''''''
#######  继承 举例
''''''''''''''''''''''''''''''''''''''
print("继承 举例  -------------------------> 开始");

# 父类
class Fish:
    def __init__(self):
        self.x = R.randint(0, 10);
        self.y = R.randint(0, 10);
    
    def mov(self):
        self.x = self.x - 1;
        print("我现在的位置是：" + str(self.x));

# 子类        
class GoldenFish(Fish):
    pass;

class Carp(Fish):
    pass;


class Shark(Fish):
    def __init__(self):
        super().__init__();
        self.hungry = 100;
        
    def eat(self):
        self.hungry = self.hungry - 1;
        print("我现在的饥饿度为：" + str(self.hungry));
        

gfish = GoldenFish();
gfish.mov();

shark = Shark();
shark.mov();
shark.eat();

print("继承 举例  -------------------------> 结束");
print();
        
        
        
''''''''''''''''''''''''''''''''''''''
#######  算术操作符 举例
# 当对象之间进行算术操作时，会自动触发
''''''''''''''''''''''''''''''''''''''        
print("算术操作符 举例  -------------------------> 开始");

### 继承int
class NewInt(int):
    def __add__(self, other):
        # 将"加法操作"定义为"相减"
        return int(self) - int(other);
    
    def __sub__(self, other):
        # 将"减法操作"定义为"相加"
        return int(self) + int(other);

a = NewInt(5);

b = NewInt(2);

print("a : " + str(a));
print("b : " + str(b));
print("a + b : " + str(a + b));
print("a - b : " + str(a - b));            
        
print("算术操作符 举例  -------------------------> 结束");
print();        
        
        
        
        
        
        
        
        
        
        