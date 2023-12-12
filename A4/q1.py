def remove_dup(arr):
    return list(set(arr))

def main():
    n = int(input("enter the size of the array: "))
    arr= []
    for i in range(n):
        ele = int(input("enter element: "))
        arr.append(ele)
    res= remove_dup(arr)
    print(res)

main()