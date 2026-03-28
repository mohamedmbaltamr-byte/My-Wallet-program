# * * * * * * * * * * * * * * * * * * * * * * * * * * * * My Wallet program * * * * * * * * * * * * * * * * * * * * * * * * * * * * # 
from operator import itemgetter
def get_number_only():
    while True:
        user_input = input("Enter a number : \n")
        try: return float(user_input)
        except ValueError: print("Error: Numbers only allowed (No letters or symbols).")
##################################################################################----------------------------------------

print("\n\n * * * * * * * * * * Welcome to My Wallet program * * * * * * * * * * \n\n")
input("To start the program, press Enter")
eroor01 = "Input Error, Press Enter To re-enter\n"
list_expenses = [] # قائمة المصاريف
list_added = [] # قائمة الاضافات
total_prices = 0
amount_of_money = 0

##################################################################################----------------------------------------
while True :###----------------------------------------------------------------###

    option = input("""Choose One Of These Options\n
 1- Financial Report \n \t Enter (a)\n
 2- Add Expense \n \t Enter (b)\n
 3- Add Income \n \t Enter (c)\n
 4- Exit the program \n \t Enter (d)\n""").lower()  

    if option == "a" : ###-----------------------------------------------------###
        list_expenses_big_to_small = sorted(list_expenses, key = itemgetter(1), reverse = True)
        list_added_big_to_small = sorted(list_added, key = itemgetter(1), reverse = True)
        allmony = amount_of_money


        print("Your expenses is:-\n")
        for cd, vd in enumerate(list_expenses_big_to_small , 1):
            print("\t",cd, "- ", vd)
        print("\t -----The Total is:   %d LYD-----"%total_prices)


        print("\n\n\nYour added is:-\n" )
        for ce, ve in enumerate(list_added_big_to_small , 1):
            print("\t",ce, "- ", ve)
        print("\t -----The Total is:   %d LYD-----"%amount_of_money)
        save_mony = amount_of_money - total_prices
        print("\n\n\n",(" The savings you have now are: %d LYD "%save_mony).center(80,"*"),"\n\n")
        input("Press ENTER if you need exit in this page \n\n")



    elif option == "b" : ###---------------------------------------------------###



        while True :
            option_a = input("If you want to enter an item, Enter         (a)\nIf you want to exit this page, Enter        (b)\n").lower()
            if option_a == "a" :
                item = input("Enter the expense item :\n").title()
                print("How much was the",item,"?")
                item_Price = get_number_only()
                total_prices = item_Price + total_prices

                s01 = "%s:"%item
                a = (s01.ljust(20), item_Price, "LYD")
                list_expenses.append(a)

                print("Added Successfully\n")

            elif option_a == "b" :
                break

            else :
                input(eroor01)



    elif option == "c": ###-----------------------------------------------------###



        while True :    
            option_b = input("If you want Enter the added value, Enter    (a)\nIf you want to exit this page, Enter        (b)\n").lower()
            if option_b == "a" :
                Addition = input("Enter the add item :\n").title()
                print("What is the value of the addition?\n")
                Added_value = get_number_only()
                amount_of_money = amount_of_money + Added_value
                ss01 = "%s:"%Addition
                ab = (ss01.ljust(20), Added_value, "LYD")
                list_added.append(ab)
                print("Added successfully\n")

            elif option_b == "b" :
                break
                
            else :
                input(eroor01)



    elif option == "d" : ###----------------------------------------------------###   
        print(" * * * * * * * * * * The program has ended * * * * * * * * * * \n\n")
        exit()

    else :###-------------------------------------------------------------------###
        input(eroor01)        
##################################################################################----------------------------------------