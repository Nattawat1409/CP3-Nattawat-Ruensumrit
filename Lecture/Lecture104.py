class Customer:
    # attribute #
    name = ""
    lastname = "" # for prepare #
    age = 0

    # behavior #
    def addCart(self):
        print("Added product to %s %s's cart."%(self.name , self.lastname))
buyer_list = []
customer_member = int(input("Amount of customer :"))

for x in range(0,customer_member):
    buyer_list = Customer()
    buyer_list.name = input("Input name:").capitalize()
    buyer_list.lastname = input("input surname:").capitalize()
    buyer_list.age = input("age :")
    buyer_list.addCart()