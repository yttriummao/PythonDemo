# coding=gbk

import easygui as g
import sys


while True:
    g.msgbox("��ӭ�����һ����ĿС��Ϸ");
    msg = "��ϣ��ѧϰʲô֪ʶ ?";
    title = "С��Ϸ����";
    choices = ["̸����", "���", "����Ϸ"];
    choices_gui = g.choicebox(msg, title, choices);
    g.msgbox("���ѡ���ǣ�" + str(choices_gui), "���");
    msg = "��ϣ�����¿�ʼС��Ϸ��";
    title = "ѡ��";
    if g.ccbox(msg, title) : # show a countine/cancel dialog
        pass; # user chose continue
    else :
        sys.exit(0); # user chose cannel