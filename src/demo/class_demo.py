# coding=gbk

import random as R;

''''''''''''''''''''''''''''''''''''''
#######  �̳� ����
''''''''''''''''''''''''''''''''''''''
print("�̳� ����  -------------------------> ��ʼ");

# ����
class Fish:
    def __init__(self):
        self.x = R.randint(0, 10);
        self.y = R.randint(0, 10);
    
    def mov(self):
        self.x = self.x - 1;
        print("�����ڵ�λ���ǣ�" + str(self.x));

# ����        
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
        print("�����ڵļ�����Ϊ��" + str(self.hungry));
        

gfish = GoldenFish();
gfish.mov();

shark = Shark();
shark.mov();
shark.eat();

print("�̳� ����  -------------------------> ����");
print();
        
        
        
''''''''''''''''''''''''''''''''''''''
#######  ���������� ����
# ������֮�������������ʱ�����Զ�����
''''''''''''''''''''''''''''''''''''''        
print("���������� ����  -------------------------> ��ʼ");

### �̳�int
class NewInt(int):
    def __add__(self, other):
        # ��"�ӷ�����"����Ϊ"���"
        return int(self) - int(other);
    
    def __sub__(self, other):
        # ��"��������"����Ϊ"���"
        return int(self) + int(other);

a = NewInt(5);

b = NewInt(2);

print("a : " + str(a));
print("b : " + str(b));
print("a + b : " + str(a + b));
print("a - b : " + str(a - b));            
        
print("���������� ����  -------------------------> ����");
print();        
        
        
        
        
        
        
        
        
        
        