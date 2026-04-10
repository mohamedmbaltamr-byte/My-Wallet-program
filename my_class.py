#لخذ الرقم فقط من المستخدم
def get_number_only():
    while True:
        user_input = input("Enter a number : \n")
        try: return float(user_input)
        except ValueError: print("Input Error, Press Enter To re-enter")



##################################################################################----------------------------------------
#لإظهار الخيارات للمستخدم
def cop(cop_1):
    print("Choose one of the options:\n")
    for i in range(len(cop_1)):
        print(i, "- ", cop_1[i]," press (",i,")\n")
    while True:
        option_cop = get_number_only()

        if 0 <= option_cop < len(cop_1):
            return int(option_cop)

        else:
            print("Input Error, Press Enter To re-enter.")



##################################################################################----------------------------------------
#لإدخال المصاريف أو المبالغ المضافة
def get_add(name, value, currency = "LYD"):

    item = input(name).title()
    print(value)
    item_price = get_number_only()
    the_add = (("%s:"%item).ljust(20), item_price, currency)
    return item, item_price, the_add
