
stack=[]
size=5

def push(n):
    
    if len(stack)>=size:
        print(size)
        print(len(stack))
        print("stack oveflow")
    else:
        stack.append(n)
        print(f"{n} has been inserted in the stack:{stack} ")

while True:
    print("do you want to  push?Y/N")
    choice=input("enter your choice:")
    if choice=="Y":
        item=int(input("enter the number:"))
        push(item)
    else:
        print("no input")
        break

