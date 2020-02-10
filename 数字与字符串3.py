# -*- coding:utf-8 -*-

''' 
   @ 功能：打印金字塔图形
   @ create:2020年2月7日

'''
for i in range(1,6):             # 外层循环，控制行数
    for j in range(5-i):         # 内层循环，控制空格位数
        print(' ',end = '')
    for j in range(i*2-1):       # 内层循环，控制*的个数
        print('*',end = '')
    print('')

    
    


    

    




