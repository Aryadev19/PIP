def get_muls(arr):
    res=[]
    for i in range(len(arr)):
        temp = [arr[i] * j for j in range(1,6)]
        res.append(temp)
    return res
    
def main():
    n = int(input("enter the size of the array: "))
    arr= []
    for i in range(n):
        ele = int(input("enter element: "))
        arr.append(ele)
    res= get_muls(arr)
    print(res)
    
main()