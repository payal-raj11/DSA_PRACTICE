array=[-12,1,2,8,11,14,17,20]
def fibonacci_search(arr,n,target):
    fib2=0
    fib1=1
    fib=fib2+fib1
    while fib<n:
        fib2=fib1
        fib1=fib
        fib=fib2+fib1
    offset =-1
    while fib>1:
        i=min(offset+fib2, n-1)
        if arr[i]>target:
            fib=fib1
            fib1=fib1-fib2
            fib2=fib-fib1
        elif arr[i]<target: 
            fib=fib1
            fib1=fib2
            fib2=fib-fib1
            offset=i
        else:
            return i
    if fib1 and offset+1<n and arr[offset+1]==target:
        return offset+1
    return -1

print(fibonacci_search(array,8,17))
