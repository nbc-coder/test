# -*- coding:utf-8 -*-

''' 
   @ 功能：用户登录认证程序，判断用户名和密码是否正确？
   @ author:张华雄
   @ create:2020年2月6日

'''
print("\n用户登录认证\n")
name = input("请输入用户名：")   # 获取用户输入的用户名
password = input("请输入密码：")  # 获取用户输入的密码，并转换为整型

if 'Albert' == name and '1' == password :                       # 如果用户名和密码正确
    print("\n登录成功!")
else:                               
    print("\n用户名或者密码错误！")
    

