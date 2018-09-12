# coding=gbk

import easygui as g
import sys


while True:
    g.msgbox("欢迎进入第一个节目小游戏");
    msg = "你希望学习什么知识 ?";
    title = "小游戏互动";
    choices = ["谈恋爱", "编程", "玩游戏"];
    choices_gui = g.choicebox(msg, title, choices);
    g.msgbox("你的选择是：" + str(choices_gui), "结果");
    msg = "你希望重新开始小游戏吗？";
    title = "选择";
    if g.ccbox(msg, title) : # show a countine/cancel dialog
        pass; # user chose continue
    else :
        sys.exit(0); # user chose cannel