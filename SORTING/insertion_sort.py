'''arr=[7,4,2,69,-4,5,96]
comparison=0
def insertion_sort(arr):
    global comparison
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            comparison=comparison+1
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key

insertion_sort(arr)
print(arr)
print(comparison)'''
comparison=0
shift=0
def insertion_sort(arr):
    global comparison
    global shift
    n=len(arr)
    for i in range(1 , n ):
          for j in range(i,0,-1):
                comparison=comparison+1
                if arr[j]<arr[j-1]:
                    shift=shift+1
                    arr[j],arr[j-1]=arr[j-1],arr[j]
                    print(arr)

arr=[7,4,2,69,-4,5,96]
insertion_sort(arr)
print(arr)
print(shift)
print(comparison)