# -*- coding:utf-8 -*-

''' 
   @ 功能：按要求打印如下结果：
          1.使用while循环输出123456 8910
          2.求1-100的所有数的和
          3.输出1-100内的所有奇数
          4.输出1-100内的所有偶数
   @ author:张华雄
   @ create:2020年2月6日

'''
print("\n1.使用while循环输出123456 8910")
count = 0           # count的初始值为0
while count < 10:  # 如果count小于等于10
    count += 1
    if count == 7 :
        print(' ',end = ' ')
    else:
        print(count,end = ' ')
    
print("\n2.求1-100的所有数的和")
sum = 0 #将和的初始值0
for i in range(1,101):
    sum += i
print(sum)

print("\n3.输出1-100内的所有奇数")
sum = 0 #将和的初始值0
for i in range(1,101,2):
    sum += i
print(sum)

print("\n4.输出1-100内的所有偶数")
sum = 0 #将和的初始值0
for i in range(2,101,2):
    sum += i
print(sum)