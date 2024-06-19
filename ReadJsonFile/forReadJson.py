import json

def searchKey():
    print("Select Key to know")
    print("1.) name")
    print("2.) age")
    print("3.) Is_programmer")
    print("4.) Goals")
    print("------------------")
    print("Select number from 1-4")
    key = input("Input keys : ")
    if key == "1":
        key = "name"
    elif key == "2":
        key = "age"
    elif key == "3":
        key = "Is_programmer"
    elif key == "4":
        key = "Goals"
    else:
        print("your selected key're wrong")

    return key


def readJsonFile():
    with open('newfile.json', 'r') as file:
        lines = json.load(file)

    print(lines[searchKey()])

readJsonFile()

