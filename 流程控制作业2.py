# -*- coding:utf-8 -*-

''' 
   @ 功能：用户猜年龄游戏，判断用户是否猜对？
   @ author:张华雄
   @ create:2020年2月6日

'''
print("\n猜年龄游戏\n")
age = 36           #提前定义好用户的年龄
input_age = int(input("请输入用户的年龄："))  # 获取用户输入的年龄，并转换为整型

if age < input_age :                       # 如果猜大了
    print("\n猜大了!")
elif age > input_age:                     #如果猜小了          
    print("\n猜小了！")
else:                                       #如果猜对了 
    print("\n猜对了！")   
