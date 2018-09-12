# coding=gbk

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#######  ������ (property���� ԭ��)
# ��ĳ���������͵����ʵ��ָ�ɸ���һ���������
# ���У�"�������͵���"��ָ���ٶ���__get__()��__set__()��__delete() ���������е�����һ��
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

######################### ��1
class MyDescriptor:
    def __get__(self, instance, owner):
        print("__get__ >>> ���ڷ������ԣ����������Ե�ֵ", self, instance, owner);
        
    def __set__(self, instance, value):
        print("__set__ >>> �������Է�������е��ã��������κ�����", self, instance, value);
        
    def __delete__(self, instance):
        print("__delete__ >>> ����ɾ���������������κ�����");
        

class Test:
    x = MyDescriptor(); ### ��������MyDescriptor������������ʵ������ֵ��Test���x����


print("----------------------------------- ��1 begin -----------------------------");   
 
test = Test();

# __get__()
print(test.x);

#__set__()
test.x = "ë��";

#__delete__
del test.x;

print("------------------------------------ ��1 end ------------------------------"); 
print();   
print(); 




######################### ��2
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# ������������ʵ��property()����
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
        print("ëɾ��");
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
        
    ### property ����
    myproperty = MyProperty(getX, setX, delX);



print("----------------------------------- ��2 begin -----------------------------");   
c = C();

# ����MyProperty���൱�ڵ���getX
print(c.myproperty);

# ����MyProperty���൱�ڵ���setX
c.myproperty = 10;
print(c.myproperty);

# ɾ��MyProperty���൱�ڵ���delX
del c.myproperty;
print(c.myproperty);

print("------------------------------------ ��1 end ------------------------------"); 
print();   
print(); 
















