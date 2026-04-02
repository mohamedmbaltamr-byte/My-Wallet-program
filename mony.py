# * * * * * * * * * * * * * * * * * * * * * * * * * * * * My Wallet program * * * * * * * * * * * * * * * * * * * * * * * * * * * * # 
from operator import itemgetter
def get_number_only():
    while True:
        user_input = input("Enter a number : \n")
        try: return float(user_input)
        except ValueError: print("Input Error, Press Enter To re-enter")
##################################################################################----------------------------------------
def cop(cop_1):
    print("Choose one of the options:\n")
    for i in range(len(cop_1)):
        print(i, "- ", cop_1[i]," press (",i,")\n")
    while True:
        option_cop = get_number_only()

        if 0 <= option_cop <= len(cop_1):
            return int(option_cop)

        else:
            print("Input Error, Press Enter To re-enter.")
##################################################################################----------------------------------------
print("\n\n * * * * * * * * * * Welcome to My Wallet program * * * * * * * * * * \n\n")
list_expenses = [] ; list_added = [] # قائمة المصاريف وقائمة الاضافات
total_prices = 0 ; amount_of_money = 0
currency = input("Enter the currency you want to use in the program (e.g. USD, EUR, LYD....Etc.):\n").upper()
##################################################################################----------------------------------------
while True :###----------------------------------------------------------------###
    option = cop(["Financial Report :", "Add Expense :", "Add Income :", "Exit the program :"])




    if option == 0 : ###-----------------------------------------------------###

        list_expenses_big_to_small = sorted(list_expenses, key = itemgetter(1), reverse = True)
        list_added_big_to_small = sorted(list_added, key = itemgetter(1), reverse = True)
        allmony = amount_of_money

        print("Your expenses is:-\n")
        for cd, vd in enumerate(list_expenses_big_to_small , 1):
            print("\t",cd, "- ", vd)
        print("\t -----The Total is:   %d %s-----"%(total_prices, currency))

        print("\n\n\nYour added is:-\n" )
        for ce, ve in enumerate(list_added_big_to_small , 1):
            print("\t",ce, "- ", ve)
        print("\t -----The Total is:   %d %s-----"%(amount_of_money, currency))
        save_mony = amount_of_money - total_prices
        print("\n\n\n",(" The savings you have now are: %d %s "%(save_mony, currency)).center(80,"*"),"\n\n")
        input("Press ENTER if you need exit in this page \n\n")




    elif option == 1 : ###---------------------------------------------------###

        while True :
            option_a = cop(["Enter an item", "Exit this page"])
            if option_a == 0 :
                item = input("Enter the expense item :\n").title()
                print("How much was the",item,"?")
                item_Price = get_number_only()
                total_prices = item_Price + total_prices

                s01 = "%s:"%item
                a = (s01.ljust(20), item_Price, currency)
                list_expenses.append(a)

                print("Added Successfully\n")

            else :# option_b = 1
                break




    elif option == 2 : ###-----------------------------------------------------###

        while True :    
            option_b = cop(["Enter an addition", "Exit this page"])
            if option_b == 0 :
                Addition = input("Enter the add item :\n").title()
                print("What is the value of the addition?\n")
                Added_value = get_number_only()
                amount_of_money = amount_of_money + Added_value
                ss01 = "%s:"%Addition
                ab = (ss01.ljust(20), Added_value, "LYD")
                list_added.append(ab)
                print("Added successfully\n")

            else :  # option_b = 1
                break




    else: # option = 3
        print(" * * * * * * * * * * The program has ended * * * * * * * * * * \n\n")
        exit()
##################################################################################----------------------------------------