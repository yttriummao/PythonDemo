# coding=gbk

import os;
import pickle;


print(os.curdir);
print(os.getcwd());

mydir = os.pardir + os.sep + 'mydir';
print(mydir);
mydir_file = mydir + os.sep + 'pickle_demo_file.pkl';
print(mydir_file);

my_list = ['ë��', '����', '����'];

'''
pickle д 
��python�����Ѷ����Ƶķ�ʽд���ı���ע�⣺fileҪָ�� wb�������ƣ���ʽ !!
'''
pickle_file_write = open(mydir_file, 'wb');
pickle.dump(my_list, pickle_file_write);
pickle_file_write.close();


'''
pickle ��
ע�⣺fileҪָ�� rb�������ƣ���ʽ !!
'''
pickle_file_read = open(mydir_file, 'rb');
my_list_read = pickle.load(pickle_file_read);
print("��ȡ�����" + "\n" + str(my_list_read));







