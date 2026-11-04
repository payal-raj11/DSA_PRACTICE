'''
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
'''
comparison=0
shift=0
def bubble_sort(arr):
    n =len(arr)
    for i in range(0,n-1):
        for j in range(0, n-i-1):
            comparison=comparison+1
            if arr[j]>arr[j+1]:
                shift=shift+1
                arr[j], arr[j+1]=arr[j+1],arr[j]
            print(arr)

arr=[7,4,2,69,-4,5,96]
bubble_sort(arr)
print(arr)
print(shift)
print(comparison)