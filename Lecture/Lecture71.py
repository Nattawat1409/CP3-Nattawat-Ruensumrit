menulist = []
menuprice = []
total = 0
def showbill():
    print("Menu List".center(50,"-"))

    for i in range(len(menulist)):
        print("menu: %s %s THB."%(menulist[i],menuprice[i]))


def totalprice(price):
    print("TOTAL PRICE".center(50,"-"))

    for x in range(len(menulist)):
        if x == len(menulist) - 1:
            print("%s = %s THB"%(menulist[x],price))
            break

        else:
            print("%s"%(menulist[x]),end=" + ")

    print("You're Welcome".center(50, "-"))


while True:
    menu_name = input("input your menu :")
    if menu_name.lower() == "exit":
        break
    else:

        menu_price = int(input("input price :"))
        total += menu_price
        menulist.append(menu_name)
        menuprice.append(menu_price)

showbill()
totalprice(total)




