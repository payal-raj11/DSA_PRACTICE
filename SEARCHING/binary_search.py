array=[-1,12,13,40,72,89,90,91,200,204,234,890]
target=int(input("enter the target:"))
def binary_search(array, n,target):
    start=0
    end=n
   
    while start<=end:
        mid=(end-start)//2 +start
        if array[mid]==target:
          return mid
        elif  array[mid]<target:
           start=mid+1
        else:
           end=mid-1
    return -1




result =binary_search(array, len(array),target)
print("result:", result)