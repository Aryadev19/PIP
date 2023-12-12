def change_form(num):
    hashmap={
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine',
    }
    
    temp = str(num)
    arr = []
    for i in range(len(temp)):
        arr.append(hashmap[temp[i]])
    return ' '.join(arr)

def main():
    string = int(input("enter a number: "))
    res = change_form(string)
    print(res)
    
main()
    