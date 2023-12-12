import re
def countWords(string):
    val = re.findall(r'\w+',string)
    return len(val)

str = input("enter a sentence\n")
res = countWords(str)
print("there are ",res," number of words in the given sentence")