# coding=gbk

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#######  ��ʱ��

# property()����������һ�������������Ե�����
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
        
    ### property ����
    MyProperty = property(getX, setX, delX);
    

c = C();

# ����MyProperty���൱�ڵ���getX
print(c.MyProperty);

# ����MyProperty���൱�ڵ���setX
c.MyProperty = 10;
print(c.MyProperty);

# ɾ��MyProperty���൱�ڵ���delX
del c.MyProperty;
print(c.MyProperty);









