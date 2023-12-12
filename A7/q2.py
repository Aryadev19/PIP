def sum_arr(arr):
    res = [arr[0]]
    for i in range(1,len(arr)):
        val = res[-1]+arr[i]
        res.append(val)
    return res
    

def main():
    n = int(input("enter the size of the array: "))
    arr= []
    for i in range(n):
        ele = int(input("enter element: "))
        arr.append(ele)
    res = sum_arr(arr)
    print(res)
    
main()
