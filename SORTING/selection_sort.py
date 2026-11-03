arr=[7,4,2,69,-4,5,96]
def selection_sort(arr,n):
    for i in range(0,n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<=arr[min_index]:
                min_index=j

        arr[i],arr[min_index]=arr[min_index],arr[i]

selection_sort(arr,len(arr))
print(arr)