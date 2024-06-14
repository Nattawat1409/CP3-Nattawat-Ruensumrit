def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():

    userSelected = int(input(">> "))
    choice = userSelected
    if userSelected == 1:
        print("--------------------------------")
        print("You require to find only raw vat")
        print("--------------------------------")
        return 1

    elif userSelected == 2:
        print("------------------------------------------------------------")
        print("You require to know overall price from 2 items including vat")
        print("------------------------------------------------------------")
        return 2



def rawprice_vat():
    price = int(input("input product price: "))
    vat = 7
    result = price + (price * vat / 100)
    result -= price

    return result
def vatCalculator(totalPrice):
    vat = 7
    return totalPrice + (totalPrice * vat / 100)

def priceCalculator():
    print("Input price of 2 products ")
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)


if login() == True:
    showMenu()
    choice = menuSelect()
    if choice == 1:

        print("your vat is :",rawprice_vat(),"THB")

    if choice == 2:

        print("your totalprice is :", priceCalculator(), "THB")


    print("                                                   ")
    print("---------------------------------------------------")
    print("                    thank you                      ")
    print("---------------------------------------------------")

else:
    print("your username and password might be wrong, Try again")
    print("you could try again for only 1 round")
    login()
