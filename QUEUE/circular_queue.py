
size=int(input("enter ther size of the circular queue:"))
queue=[None]*size
front=-1
rear=-1

def enqueue(item):
    global rear
    global front
    if (rear+1)%size==front:
        print("queue full")
    elif front==-1:
         front=front+1
         rear=rear+1
         queue[front]=item
    else:
        rear=(rear+1)%size
        queue[rear]=item
    print(queue)
def dequeue():
    global rear
    global front
    if queue[front]==None:
        print("queue is empty")
    else:
        queue[front]=None
        front=(front+1)%size
    print(queue)
def display():
    global rear
    global front
    if queue[front]==None:
            print("queue is empty")
    else:
        i=front
        while (i)%size!=rear+1:
              print(queue[(i)%size])
              i=i+1
        
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
