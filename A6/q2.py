from collections import Counter
def isAnagram(s,t):
    return Counter(s) == Counter(t)
s = input("enter 1st string\n")
t = input("enter 2nd string\n")
res = isAnagram(s,t)
print(res)