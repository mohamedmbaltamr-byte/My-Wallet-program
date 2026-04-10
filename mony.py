# * * * * * * * * * * * * * * * * * * * * * * * * * * * * My Wallet program * * * * * * * * * * * * * * * * * * * * * * * * * * * * # 
from operator import itemgetter
from my_class import get_number_only, cop, get_add

print("\n\n * * * * * * * * * * Welcome to My Wallet program * * * * * * * * * * \n\n")

list_expenses = [] # قائمة المصاريف
list_added = [] # قائمة المبالغ المضافة
total_prices = 0 # مجموع المصاريف
amount_of_money = 0 # مجموع المبالغ المضافة

currency = "LYD" if cop(["TO Libyan Dinar 'LYD'", "TO US Dollar 'USD'"]) == 0 else "USD"

##################################################################################----------------------------------------
while True :###----------------------------------------------------------------###
    option = cop(["Financial Report :", "Add Expense :", "Add Income :", "Exit the program :"])

    if option == 0 : ###-----------------------------------------------------###


        print("Your expenses is:-\n")
        for price, currency_1 in enumerate(sorted(list_expenses, key = itemgetter(1), reverse = True) , 1):
            print("\t",price, "- ", currency_1)
        print("\t -----The Total is:   %.2f %s-----"%(total_prices, currency))

        print("\n\n\nYour added is:-\n" )
        for price, currency_1 in enumerate(sorted(list_added, key = itemgetter(1), reverse = True) , 1):
            print("\t",price, "- ", currency_1)
        print("\t -----The Total is:   %.2f %s-----"%(amount_of_money, currency))
        
        print("\n\n\n",(" The savings you have now are: %.2f %s "%((amount_of_money - total_prices), (currency))).center(80,"*"),"\n\n")
        input("Press ENTER if you need exit in this page \n\n")


    elif option == 1 : ###---------------------------------------------------###


        while True :
            option_a = cop(["Enter an item", "Exit this page"])
            if option_a == 0 :

                item, item_price, the_add = get_add(("Enter the expense item :\n"), ("How much was these ?"), currency)
                total_prices = item_price + total_prices
                list_expenses.append(the_add)
                print("Added Successfully\n")

            else :# option_b = 1
                break


    elif option == 2 : ###-----------------------------------------------------###


        while True :    
            option_b = cop(["Enter an addition", "Exit this page"])
            if option_b == 0 :

                item, item_price, the_add = get_add(("Enter the add item :\n"), ("What is the value of the addition?\n"), currency)
                amount_of_money = amount_of_money + item_price
                list_added.append(the_add)
                print("Added successfully\n")

            else :  # option_b = 1
                break


    else: # option = 3
        print(" * * * * * * * * * * The program has ended * * * * * * * * * * \n\n")
        exit()
##################################################################################----------------------------------------