def Vending_machine():
    print('Welcome To Vending Machine')
    print('\nitems available \n***************')

    a = {'Item': 'Coke', 'Price': 25}
    b = {'Item': 'Pepsi', 'Price': 35}
    c = {'Item': 'Soda', 'Price': 45}

    items=[a,b,c]
    for i in items:
        print(i)

    
    print('Coke  : Press 1')
    print('Pepsi : Press 2')
    print('Soda  : Press 3')

    def cho():
        while(True):
        # import pdb; pdb.set_trace()
            drink_choice=int(input('Please Enter Your Drink Choice: '))
        
        
            if drink_choice == 1:
                    print('Your Selected Coke')
                    print('******Only For 1,5,1o Or 25 Coins Are Accepted*****')
                    p=1
                    total_input_coins = 0
                    while p <= 25:
                        coins_format = int(input('Please Enter Your Coin Format : '))
                        if coins_format == 1 or coins_format == 5 or coins_format == 10 or coins_format == 25:
                            coins_count = int(input('How Many Coins Are Insert : '))
                            total_input_coins=total_input_coins+(coins_count*coins_format)
                            print("Total inserted coins is ", total_input_coins)
                            if total_input_coins >= 25:
                                    remaining_amount = total_input_coins-25
                                    print('Your Remaning Amount Is : ', remaining_amount)
                                    print('Your Coke is ready ')
                                    print('********THANK YOU********')
                                    break                   
                        else:
                            print('******Only For 1,5,1o Or 25 Coins Are Accepted*****')
                        p = +1      
                        

            elif drink_choice == 2:
                    print('Your Selected Pepsi')
                    print('******Only For 1,5,1o Or 25 Coins Are Accepted*****')                    
                    p = 1
                    total_input_coins = 0
                    while p <= 35:
                        coins_format = int(input('Please Enter Your Coin Format : '))                   
                        if coins_format == 1 or coins_format == 5 or coins_format == 10 or coins_format == 25:
                            coins_count = int(input('How Many Coins Are Insert : '))
                            total_input_coins = total_input_coins+(coins_count*coins_format)                    
                            print("Total inserted coins is ",  total_input_coins)
                        if total_input_coins >= 35:
                            
                                remaining_amount = total_input_coins-35
                                print(' Your Remaning Amount Is : ', remaining_amount)
                                print('Your Pepsi is ready')                                                        
                                print('********THANK YOU********')
                                break
                        else:
                            print('******Only For 1,5,1o Or 25 Coins Are Accepted*****')
                        p = +1        
        
            elif drink_choice == 3:
                    print('Your Selected Soda')
                    print('******Only For 1,5,1o Or 25 Coins Are Accepted*****')
                    p = 1
                    total_input_coins = 0
                    while p <= 45:
                        coins_format = int(input('Please Enter Your Coin Format : '))
                        if coins_format == 1 or coins_format == 5 or coins_format == 10 or coins_format == 25:
                            coins_count = int(input('How Many Coins Are Insert : '))
                            total_input_coins = total_input_coins+(coins_count*coins_format)
                            print("Total inserted coins is ",  total_input_coins)
                        if total_input_coins >= 45:
                            
                                remaining_amount = total_input_coins-45
                                print('Your Remaning Amount Is : ', remaining_amount)
                                print(('Your Soda is ready '))                                                        
                                print('********THANK YOU********')
                                break
                        else:
                            print('******Only For 1,5,1o Or 25 Coins Are Accepted*****')
                        p = +1
            else:
                print('You Did Not Make A Vaild Selection Please Enter 1, 2, or 3')

    cho()
Vending_machine()





 