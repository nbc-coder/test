# -*- coding:utf-8 -*-

''' 
   @ 功能：列表l=['a','b',1,'a','a']，列表元素均为不可变类型，去重得到新列表,且新列表需保持列表原来的顺序
   @ create:2020年2月7日

'''
l = ['a','b',1,'a','a']

list_new = []
for i in l:
    if i not in list_new:
        list_new.append(i)
print(list_new)
    
    


    

    




