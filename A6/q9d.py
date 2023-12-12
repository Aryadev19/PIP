def isPalin(str):
    return str == str[::-1]

def main():
    str = input("enter a string\n")
    print(isPalin(str))
    
main()