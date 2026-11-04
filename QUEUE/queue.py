queue=input("enter the stack:").split(",")
queue=[int(x) for x in queue[0:]]
print(queue)
size=int(input("enter ther size of the queue:"))
def enqueue(item):
    if size<=len(queue):
        print("queue overflow")
    else:
        queue.append(item)
        print(f"{item} has been inserted in queue: {queue}")
def dequeue():
    global queue
    if len(queue)==0:
        print("queue underflow")
    else:
        queue=queue[1:]
def display():
    global queue
    if len(queue)==0:
            print("queue underflow")
    else:
            print(queue)

while True:
     choice=int(input("enter the choice:"))
     if choice==1:
        n=int(input("enter the no"))
        enqueue(n)
     elif choice==2:
        dequeue()
     elif choice==3:
            display()
     elif choice==4:
          exit
     else:
          break

    