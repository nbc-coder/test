# -*- coding:utf-8 -*-

''' 
   @ 功能：使用至少两种方法统计字符串 s='hello albert albert say hello world world'中每个单词的个数
   @ create:2020年2月7日

'''
s = 'hello albert albert say hello world world'
# 方式一
list1 = s.split()
print(list1)
dict1 = {}
for i in list1:
    if i not in dict1:
        dict1[i] = 1
    else :
        dict1[i] += 1

print(dict1)

# 方式二
list2 = s.split()
dict2 = {}
for j in list2:
    dict2[j] = s.count(j)

print(dict2)


