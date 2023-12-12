def isContain(str):
    isnum= False
    isChar = False
    for i in range(len(str)):
        if str[i].isnumeric():
            isnum = True
        if str[i].isalpha():
            isChar = True
    return isnum and isChar

def main():
    str = input("enter a string\n")
    print(isContain(str))
    
main()