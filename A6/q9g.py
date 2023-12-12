import re
def countLength(string):
    val = re.findall(r'.',string)
    res = 0
    for v in val:
        res+=1
    return res

str = input("enter a sentence\n")
res = countLength(str)
print(res)