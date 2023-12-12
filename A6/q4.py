def modify(str):
    temp = ''
    for i in range(len(str)):
        if str[i] == " " or i == len(str)-1:
            word = str[len(temp):i+1].lower()
            temp += word[0].upper()
            temp += word[1:].lower()
    return temp

def main():
    str = input("enter a string\n")
    print(modify(str))
    
main()

            