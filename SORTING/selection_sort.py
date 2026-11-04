'''arr=[7,4,2,69,-4,5,96]
def selection_sort(arr,n):
    for i in range(0,n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<=arr[min_index]:
                min_index=j

        arr[i],arr[min_index]=arr[min_index],arr[i]

selection_sort(arr,len(arr))
print(arr)'''
comparison=0
shift=0
def selection_sort(arr):
    global comparison
    global shift
    n=len(arr)
    for i in range(n-1):
        min=i
        for j in range(i+1, n):
            comparison=comparison+1
            if arr[j]<arr[min]:
                min=j
        print(arr[min])
        if i!=min:
            arr[i],arr[min]=arr[min],arr[i]
            shift=shift+1
        print(arr)
arr=[7,4,2,69,96,5,-4]
selection_sort(arr)
print(shift)
print(comparison)