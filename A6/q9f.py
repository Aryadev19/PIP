def countChar(str):
    vowels = ['a','e','i','o','u']
    vowels = set(vowels)
    
    vow,cons = 0,0
    
    for i in range(len(str)):
        if str[i] in vowels: vow += 1
        else: cons += 1
    return [vow,cons]

def main():
    str = input("enter a string\n")
    print(countChar(str))
    
main()