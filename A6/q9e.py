def removeChar(str,i):
    if i >= len(str):
        print("index out of range")
        return str
    left = str[:i]
    right = str[i+1:]
    return left + right


def main():
    str = input("enter a string\n")
    i = int(input("enter the position: "))
    print(removeChar(str,i))
    
main()