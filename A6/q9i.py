def removeDups(str):
    res = ''
    hashmap = set()
    for i in range(len(str)):
        if str[i] in hashmap:
            continue
        res += str[i]
        hashmap.add(str[i])
    return res   
def main():
    str = input("enter a string\n")
    print(removeDups(str))
    
main()