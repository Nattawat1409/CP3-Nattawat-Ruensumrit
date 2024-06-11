username = input("Enter your username :")
password = input("Enter your password : ")
if username != "nattawat" and password != "123456789":
    print("Apologize, your username and password probably wrong!! ")
else:
    print("Hello Mr.",username,",How can i help you?")
    lay_price = int(100)
    oreo_price = int(50)
    water_price = int(15)
    bread_price = int(30)

    print("Your Welcome!! to Taitech Shop")
    print("==============================")
    print("         Product List         ")
    print("1.) lay = " ,lay_price, "THB")
    print("2.) Oreo = ",oreo_price, "THB")
    print("3.) Water = " ,water_price, "THB")
    print("4.) Bread butter = ",bread_price, "THB")
    print("==============================")

    product = int(input("Select Order number >> "))

    if product == 1:

        quantity1 = int(input("quantity : "))
        total = lay_price*quantity1
        print("Total Price is : ",total ,"THB")

    elif product == 2:

        quantity2 = int(input("quantity : "))
        total = oreo_price * quantity2
        print("Total Price is : ", total,"THB")

    elif product == 3:

        quantity3 = int(input("quantity : "))
        total = water_price * quantity3
        print("Total Price is : ", total,"THB")

    elif product == 4:

        quantity4 = int(input("quantity : "))
        total = bread_price * quantity4
        print("Total Price is : ", total,"THB")

    else:
        print("Aplogize,Your require number aren't exist..")
        print("Back to menu ?? (yes or no)")
        decide = str(input("pick choice : "))
        if decide == "yes" :
            print("Your Welcome!! to Taitech Shop")
            print("==============================")
            print("         Product List         ")
            print("1.) lay = ", lay_price, "THB")
            print("2.) Oreo = ", oreo_price, "THB")
            print("3.) Water = ", water_price, "THB")
            print("4.) Bread butter = ", bread_price, "THB")
            print("==============================")
            product = int(input("Select Order number >> "))

            if product == 1:

                quantity1 = int(input("quantity : "))
                total = lay_price * quantity1
                print("Total Price is : ", total, "THB")

            elif product == 2:

                quantity2 = int(input("quantity : "))
                total = oreo_price * quantity2
                print("Total Price is : ", total, "THB")

            elif product == 3:

                quantity3 = int(input("quantity : "))
                total = water_price * quantity3
                print("Total Price is : ", total, "THB")

            elif product == 4:

                quantity4 = int(input("quantity : "))
                total = bread_price * quantity4
                print("Total Price is : ", total, "THB")

        else :
            print("Sign-out from system automate")

    print("Thank you for buying")


