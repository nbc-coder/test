# -*- coding:utf-8 -*-

''' 
   @ 功能：用户猜年龄,要求：解决用户输入的不是数字的bug
   @ create:2020年2月7日

'''
print("\n猜年龄游戏\n")
age = 18           #提前定义好用户的年龄
count = 0          # count的初始值为1

while True: 
    if count  == 3:  
        print('是否继续？')
        answer = input('继续请输入Y，否则请输入N:')
        if answer == 'Y' or answer == 'y':
            count = 0 
        else:
            break

    input_age = input("请输入用户的年龄：")  # 获取用户输入的年龄
    if not input_age.isdigit():    # 对输入数据进行判断是否为数字
       print('输入必须为数字，请重新输入：')
       continue
    input_age = int(input_age)
    if age < input_age :                       # 如果猜大了
       print("\n猜大了!")
    elif age > input_age:                     #如果猜小了          
       print("\n猜小了！")
    else:                                       #如果猜对了 
       print("\n猜对了！") 
       break
    count += 1

    
    


    

    




