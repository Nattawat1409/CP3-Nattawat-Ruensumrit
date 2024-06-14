# Nattawat Ruensumrit #
print("--------------------------------------------------------------")
print("This program for convert other base number into Decimal number")
print("require base : 2,5,8,16 ")
print("--------------------------------------------------------------")
base = int(input("input your base number: "))
number = input("input value: ")
adding  = 0
i = len(number) - 1
if base == 2:
    for x in number:
        digit = int(x) * (2**i)
        adding += digit
        i -= 1

elif base == 5:
    for x in number:
        digit = int(x) * (5**i)
        adding += digit
        i -= 1

elif base == 8:
    for x in number:
        digit = int(x) * (10**i)
        adding += digit
        i -= 1

elif base == 10:
    for x in number:
        digit = int(x) * (10**i)
        adding += digit
        i -= 1

elif base == 16:
    hexa = { 'A':10 , 'B':11 ,'C': 12 ,'D': 13,'E':14,'F': 15}
    for x in number:
        if x.isdigit():
            digit = int(x)  * (16**i)
            adding += digit
        else:
            digit = hexa[x.upper()] * (16**i) # searching in element within array whichone is matched #
            adding += digit
        i -= 1

print("--------------------------------------------------------------")
print("                       CONVERTING                          ")
print("to Decimal number is ->",adding)
print("--------------------------------------------------------------")