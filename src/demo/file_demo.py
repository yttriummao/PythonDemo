# coding=gbk

import os;

print("��ǰĿ¼Ϊ��" + os.getcwd());
#�л�Ŀ¼
os.chdir("D:\\Workspaces\\python");
print("��ǰĿ¼������Ϊ ===>>> " + str(os.listdir()));
#����windows������
os.system("calc");


file = open("D:\\Workspaces\\python\\p8_1\\record.txt");

##### print(file.readline());

server = [];
fish = [];

for each_line in file:
    #(role, spoken) = each_line.split(':');
    #print(role);
    #print(spoken);

    tuple = each_line.split(":");
    role = tuple[0];
    spoken = tuple[1];

    if role == 'С�ͷ�':
       server.append(spoken);
    elif role == 'С����':
         fish.append(spoken);
    else:
        print("split��������!!!");


print(server);
print(fish);

file_server = open("D:\\Workspaces\\python\\p8_1\\boy���.txt", "a");
for Sspoken in server:
    file_server.write(Sspoken);
file_server.close();


file_fish = open("D:\\Workspaces\\python\\p8_1\\fish���.txt", "a");
for Fspoken in fish:
    file_fish.write(Fspoken);
file_fish.close();

