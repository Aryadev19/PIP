def isSymmetric(str):
    return str[:len(str)//2] == str[len(str)//2:]

def main():
    str = input("enter a string\n")
    print(isSymmetric(str))
    
main()