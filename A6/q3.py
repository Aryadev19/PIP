def countWords(str):
    count = 0
    for i in range(len(str)):
        if str[i] == " ": count += 1
    return count+1

str = input("enter a sentence\n")
res = countWords(str)
print("there are ",res," number of words in the given sentence")