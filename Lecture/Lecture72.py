menulist = []
total = 0
def showbill():
    print("Menu List".center(50,"-"))

    for i in range(len(menulist)):
        print("%s => %s THB."%(menulist[i][0] , menulist[i][1])) # read only inner list in menu name channel on index 0 inner list #


def totalprice(price): # read only inner list on index 1 for express prices list of each
    print("TOTAL PRICE".center(50,"-"))

    for x in range(len(menulist)):
        if x == len(menulist) - 1:
            print("%s = %s THB"%(menulist[x][1],price))
            break

        else:
            print("%s"%(menulist[x][1]),end=" + ")

    print("You're Welcome".center(50, "-"))


while True:
    menu_name = input("input your menu :")
    if menu_name.lower() == "exit":
        break
    else:
        menu_price = int(input("input price :"))
        total += menu_price
        menulist.append([menu_name,menu_price]) # append all together in 1 box consist of name of menu and price of menu #

showbill()
totalprice(total)



