# coding=gbk

import os;
import pickle;


print(os.curdir);
print(os.getcwd());

mydir = os.pardir + os.sep + 'mydir';
print(mydir);
mydir_file = mydir + os.sep + 'pickle_demo_file.pkl';
print(mydir_file);

my_list = ['毛钇', '兜兜', '猪本聪'];

'''
pickle 写 
将python对象已二进制的方式写入文本，注意：file要指定 wb（二进制）方式 !!
'''
pickle_file_write = open(mydir_file, 'wb');
pickle.dump(my_list, pickle_file_write);
pickle_file_write.close();


'''
pickle 读
注意：file要指定 rb（二进制）方式 !!
'''
pickle_file_read = open(mydir_file, 'rb');
my_list_read = pickle.load(pickle_file_read);
print("读取结果：" + "\n" + str(my_list_read));







