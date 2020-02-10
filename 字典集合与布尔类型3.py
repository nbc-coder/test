# -*- coding:utf-8 -*-

''' 
   @ 功能：实现简易购物程序
   @ create:2020年2月7日

'''
msg_dic = {
    'apple' : 10,
    'tesla' : 100000,
    'mac' : 10000,
    'iphone' : 8000,
    'chicken' : 30,
    'pen' : 3,
    'ruler' : 5
}
goods_list = []
while True:
    for product,price in msg_dic.items():
        print('product: %s ,price: %s'%(product,price))
    choice = input('please choose product:').strip()
    if choice == 'q':
        break
    elif choice not in msg_dic:
        print('The product you choose is invalid')
        continue
    else:
        while True:
            count = input('please input the number of the product:').strip()
            if not count.isdigit():
                print('The countent you input is not number')
                continue
            else:
                goods_list.append((choice,msg_dic[choice],count))
                print(goods_list)
                break