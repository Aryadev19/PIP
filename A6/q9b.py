def revWords(s):
    words = s.split()
    words.reverse()
    res = ' '.join(words)
    return res
 
def main():
    str = input("enter a string\n")
    print(revWords(str))
    
main()