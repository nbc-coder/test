# -*- coding:utf-8 -*-

''' 
   @ 功能：购物商城项目
   @ create:2020年2月8日

'''
product_list = [
    ['IphoneXR', 9800],
    ['Coffee', 30],
    ['Mac Pro 2019', 25000],
    ["Albert's Python Book", 99],
    ['Bike', 199],
    ['ViVo X20', 2499],
]

shopping_cart = {}
current_user_info = []
user_info = []
while True:
    print('''
    1：Register
    2：Login
    3：Shop
    ''')

    choice = input("""
    Please choose the function by inputting corresponding number, 
    if you input q, you'll quit the program>>:""").strip()

    # user registering
    if choice == '1':

        username = input('please input your username>>:').strip()

        while True:
            password1 = input('please input your password>>:').strip()
            password2 = input('please verify your password>>:').strip()
            if password1 == password2:
                print('Register successfully, input 2 to login')
                user_info.append([username, password1])
                break

            else:
                print('The twice password are inconsistent. Please input again')


    # user logining
    elif choice == '2':
        count = 0
        tag = True
        while tag:
            if count == 3:
                print("You've tried too many times. You'll quit the program")
                break
            username = input('username>>:').strip()
            password = input('password>>:').strip()

            # read the user data

            for data in user_info:
                username_db = data[0]
                password_db = data[1]

                # verify user data
                if username == username_db and password == password_db:
                    print('Login successfully')

                    # update current user info
                    current_user_info.append(username)
                    while True:
                        salary = input('please input your salary>>:').strip()
                        if not salary.isdigit():
                            continue
                        salary = int(salary)
                        balance = salary
                        current_user_info.append(balance)
                        break

                    # update all user info
                    data.append(balance)
                    print('Hello %s, your balance is %s, input 3 to start shopping' % (
                        data[0], data[1]))
                    tag = False
                    break

            else:
                print('username or password is invalid')
                count += 1

    # user shopping
    elif choice == '3':
        if not current_user_info:
            print('Please login first')
        else:
            # get user's balance, and then shop
            username_of_db = current_user_info[0]
            balance = current_user_info[1]
            print(balance, type(balance))

            print('Dear user[%s], your balance is [%s], wish you enjoy your shopping' % (
                username_of_db,
                balance
            ))

            tag = True
            while tag:
                for index, product in enumerate(product_list):
                    print(index, product)
                choice = input("Input the numbers of product. if you input q, you'll quit the program>>:").strip()
                if choice.isdigit():
                    choice = int(choice)
                    if choice < 0 or choice >= len(product_list):
                        continue

                    product_name = product_list[choice][0]
                    product_price = product_list[choice][1]

                    if balance > product_price:
                        if product_name in shopping_cart:  # You've bought the product
                            shopping_cart[product_name]['count'] += 1
                        else:
                            shopping_cart[product_name] = {'product_price': product_price, 'count': 1}

                        balance -= product_price  # deduct money
                        current_user_info[1] = balance  # update user's balance
                        print(
                            "Added product " + product_name + " into shopping cart,your current balance " + str(
                                balance))

                    else:
                        print(
                            "You can't afford the product. The price of the product is %s, and you're lack of %s yuan"
                            % (
                                product_price,
                                product_price - balance
                            ))
                    print('your shopping cart is %s' % shopping_cart)
                elif choice == 'q':
                    print(
                        "--------------------------------The goods list you've bought--------------------------------")

                    total_cost = 0
                    for i, key in enumerate(shopping_cart):
                        print('%s%23s%23s%23s%23s' % (
                            i,
                            key,
                            shopping_cart[key]['count'],
                            shopping_cart[key]['product_price'],
                            shopping_cart[key]['product_price'] * shopping_cart[key]['count']
                        ))
                        total_cost += shopping_cart[key]['product_price'] * shopping_cart[key]['count']

                    print("""
                    your total expenditure: %s
                    your balance: %s
                    """ % (total_cost, balance))

                    while tag:
                        inp = input('Confirm purchase(yes/no?)>>: ').strip()
                        if inp not in ['Y', 'N', 'y', 'n', 'yes', 'no']:
                            continue
                        if inp in ['Y', 'y', 'yes']:

                            # read user info
                            for data in user_info:
                                if data[0] == username_of_db:
                                    if len(data) == 3:
                                        data[2] = balance
                                    else:
                                        data.append(balance)

                            print("You've bought successfully. Please wait for the goods patiently")

                        shopping_cart = {}
                        current_user_info = []
                        tag = False

                else:
                    print('Invalid operation')
    elif choice == 'q':
        break

    else:
        print('Invalid operation')


    

    




