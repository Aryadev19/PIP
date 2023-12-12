def replace(str):
    temp = str[0]
    for i in range(1,len(str)):
        if str[i-1] == str[i]:
            temp = temp + '*'
        else: temp += str[i] 
              
    return temp;

def main():
    str = input("enter a string\n")
    print(replace(str))
    
main()