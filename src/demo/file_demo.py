# coding=gbk

import os;

print("当前目录为：" + os.getcwd());
#切换目录
os.chdir("D:\\Workspaces\\python");
print("当前目录的内容为 ===>>> " + str(os.listdir()));
#弹出windows计算器
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

    if role == '小客服':
       server.append(spoken);
    elif role == '小甲鱼':
         fish.append(spoken);
    else:
        print("split出错，请检查!!!");


print(server);
print(fish);

file_server = open("D:\\Workspaces\\python\\p8_1\\boy结果.txt", "a");
for Sspoken in server:
    file_server.write(Sspoken);
file_server.close();


file_fish = open("D:\\Workspaces\\python\\p8_1\\fish结果.txt", "a");
for Fspoken in fish:
    file_fish.write(Fspoken);
file_fish.close();

