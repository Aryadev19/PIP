from collections import Counter
import operator
def maxChar(str):
    count = Counter(str)
    return max(count.items(), key=operator.itemgetter(1))[0]

def main():
    str = input("enter a string\n")
    print(maxChar(str))
    
main()