arr=[7,4,2,69,-4,5,96]
comparison=0
def bubble_sort(arr,n):
    global comparison
    for i in range(0,n-1):
        for j in range(0,n-1-1):
            if arr[j]>arr[j+1]:
                comparison=comparison+1
                arr[j],arr[j+1]=arr[j+1],arr[j]

bubble_sort(arr,len(arr))
print(arr)
print(comparison)