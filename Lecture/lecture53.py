def Vatcalculate(price):
    result = price + (price *7/100)
    return result

totalprices = int(input("input price : "))

print("including vat :",Vatcalculate(totalprices))