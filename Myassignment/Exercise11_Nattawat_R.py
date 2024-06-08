## create pyramid related to user input ##

level = int(input("Define the height of pyramid : "))
for x in range(level):
    text = ""
    space = ""
    for z in range(level-(x+1)):
        space += " "

    for y in range((2*x)+1):
        text += "*"
    print(space+text)

# nattawat ruensumrit #