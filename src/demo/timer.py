# coding=gbk

import time;

''''''''''''''''''''''''''''''''''''''
#######  ��ʱ��

#######  ��python idle���������
# t1 = MyTimer()
# t1
# t1.stop()
# t1.start()
# t1
# t1.start()
# t2 = MyTimer()
# t2.start()
# t2.stop()
# t2-t1
''''''''''''''''''''''''''''''''''''''

class MyTimer:
    def __init__(self):
        print("������....");
        # time.struct_time(tm_year=2018, tm_mon=8, tm_mday=27, tm_hour=15, tm_min=54, tm_sec=31, tm_wday=0, tm_yday=239, tm_isdst=0)
        self.year = time.localtime()[0];
        #print("�꣺" + str(self.year));
        self.mon = time.localtime()[1];
        #print("�£�" + str(self.mon));
        self.day = time.localtime()[2];
        #print("�գ�" + str(self.day));
        self.hour = time.localtime()[3];
        #print("ʱ��" + str(self.hour));
        self.min = time.localtime()[4];
        #print("�֣�" + str(self.min));
        self.sec = time.localtime()[5];
        #print("�룺" + str(self.sec));
        
        self.starttime = 0.0;
        self.endtime = 0.0;
        self.runtime = 0.0;
    
    def __sub__(self, other):
        return "�ܹ������ˣ�" + str(self.runtime - other.runtime);
        
    
    def check(self):
        if self.starttime == 0.0:
            print("���ȿ�ʼ��ʱ");
            return False;
        elif self.endtime == 0.0:
            print("���Ƚ�����ʱ");
            return False;
        else:
            return True;
    
    def __str__(self):
        if self.check():
            return "�ܹ�������: " + str(self.endtime - self.starttime);
        else:
            return "";
        
    
    def __repr__(self):
        if self.check():
            return "�ܹ�������: " + str(self.endtime - self.starttime);
        else:
            return "";
    
    def start(self):
        self.starttime = time.time();
        print("��ʼ��ʱ  >>> " + str(self.starttime));
        
    def stop(self):
        if self.starttime == 0.0:
            print("δ��ʼ��ʱ....");
        else:
            self.endtime = time.time();
            self.runtime = self.endtime - self.starttime;
            print("������ʱ  >>> " + str(self.endtime));
            












   