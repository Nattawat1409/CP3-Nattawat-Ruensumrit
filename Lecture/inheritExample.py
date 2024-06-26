class Vehicle:
    licenseCode = ""
    serialnumber = ""
    def turnOnAirConditioner(self):
        print("Turn on : Air conditioner")

class Car(Vehicle): # inherit done from Class Vehicle above it #
    seat_number = 4
    def Opensunroof(self):
        print("Opened sunroot done")

class PickUp(Vehicle):
    def Openpickup(self):
        print("open pickup")

class Van(Vehicle):
    seat_number = 12

class EstateCar(Vehicle):
    seat_number = 6
    def Opensunroof(self):
        print("Opened sunroot done")

list_car = ["normal_car", "pickup_car" , "van_car" , "Estatecar"]
for x in range(len(list_car)):
    if x == 0:
        list_car[x] = Car()
        print("normal_car is ")
    if x == 1:
        list_car[x] = PickUp()
        print("pickup_car is")
    if x == 2:
        list_car[x] = Van()
        print("van_car is")
    if x == 3:
        list_car[x] = EstateCar()
        print("Estatecar is")
    (list_car[x].turnOnAirConditioner())
