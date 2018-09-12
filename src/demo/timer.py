# coding=gbk

import time;

''''''''''''''''''''''''''''''''''''''
#######  计时器

#######  在python idle中输入测试
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
        print("构造器....");
        # time.struct_time(tm_year=2018, tm_mon=8, tm_mday=27, tm_hour=15, tm_min=54, tm_sec=31, tm_wday=0, tm_yday=239, tm_isdst=0)
        self.year = time.localtime()[0];
        #print("年：" + str(self.year));
        self.mon = time.localtime()[1];
        #print("月：" + str(self.mon));
        self.day = time.localtime()[2];
        #print("日：" + str(self.day));
        self.hour = time.localtime()[3];
        #print("时：" + str(self.hour));
        self.min = time.localtime()[4];
        #print("分：" + str(self.min));
        self.sec = time.localtime()[5];
        #print("秒：" + str(self.sec));
        
        self.starttime = 0.0;
        self.endtime = 0.0;
        self.runtime = 0.0;
    
    def __sub__(self, other):
        return "总共运行了：" + str(self.runtime - other.runtime);
        
    
    def check(self):
        if self.starttime == 0.0:
            print("请先开始计时");
            return False;
        elif self.endtime == 0.0:
            print("请先结束计时");
            return False;
        else:
            return True;
    
    def __str__(self):
        if self.check():
            return "总共运行了: " + str(self.endtime - self.starttime);
        else:
            return "";
        
    
    def __repr__(self):
        if self.check():
            return "总共运行了: " + str(self.endtime - self.starttime);
        else:
            return "";
    
    def start(self):
        self.starttime = time.time();
        print("开始计时  >>> " + str(self.starttime));
        
    def stop(self):
        if self.starttime == 0.0:
            print("未开始计时....");
        else:
            self.endtime = time.time();
            self.runtime = self.endtime - self.starttime;
            print("结束计时  >>> " + str(self.endtime));
            












   