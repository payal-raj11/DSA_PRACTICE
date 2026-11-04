def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    i=0
    j=0
    ans=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            ans.append(left[i])
            i=i+1
    
        else:
            ans.append(right[j])
            j=j+1
    while i<len(left):
        ans.append(left[i])
        i=i+1
    while j<len(right):
        ans.append(right[j])
        j=j+1
    return ans
arr=[7,4,2,69,7,-4,5,96]
print(arr)
arr=merge_sort(arr)
print(arr)
