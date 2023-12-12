def get_freq(s):
    hashmap = {}
    for i in range(len(s)):
        hashmap[s[i]] = hashmap.get(s[i],0) + 1
    return hashmap

def main():
    string = input("enter a string: ")
    res = get_freq(string)
    print(res)
    
main()