arr=[]
def heapify(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2
    if left<n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        heapify(arr,n, largest)
def insert(item):
    arr.append(item)
    i=len(arr)-1
    while i>0:
        parent=(i-1)//2
        if arr[parent]<arr[i]:
            arr[parent],arr[i]=arr[i],arr[parent]
            i=parent
        else:
            break

def delete():
    if len(arr)==0:
        print("queue is empty.")
    else:
        n=len(arr)-1
        arr[n],arr[0]=arr[0],arr[n]
        arr.pop()
        for i in range(len(arr)//2-1,-1,-1):
            heapify(arr, len(arr),i )
def display():
    if len(arr)==0:
            print("queue is empty.")
    else:
        print(arr)

while True:
     choice=int(input("enter the choice:"))
     if choice==1:
        n=int(input("enter the no"))
        insert(n)
     elif choice==2:
        delete()
     elif choice==3:
            display()
     elif choice==4:
          exit()
     else:
          break
     