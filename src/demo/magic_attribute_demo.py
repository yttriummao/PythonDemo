# coding=gbk

''''''''''''''''''''''''''''''''''''''
#######  ������ص�ħ������
from builtins import setattr
''''''''''''''''''''''''''''''''''''''


class C:
    def __getattribute__(self, name):
        print("__getattribute__ >>> ���������Ա�����ʱ����");
        return super().__getattribute__(name);
    
    def __setattr__(self, name, value):
        print("__setattr__ >>> ���������Ա�����ʱ����");
        super().__setattr__(name, value);
        
    def __delattr__(self, name):
        print("__delattr__ >>> ���������Ա�ɾ��ʱ����");
        super().__delattr__(name);
        
    def __getattr__(self, name):
        print("__getattr__ >>> ���û���ͼ��ȡһ�����಻���ڵ�����ʱ����");

c = C();

# ��ȡ���� and ��ȡһ�������ڵ�����
c.x;
print();

# ��������
c.x = 1;
setattr(c, "y", 500);   ## �ڽ�����BIF
print();


# ɾ������
del c.x;
delattr(c, "y");   ## �ڽ�����BIF
print();



