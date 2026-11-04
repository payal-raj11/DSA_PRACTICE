stack=input("enter the stack:").split(",")
stack=[int(x) for x in stack[0:]]
print(stack)

def pop():
    if len(stack)<=0:
        print("underflow")
    else:
        item=stack.pop()
        print("popped:",item)
        print("new stack:",stack)

while True:
    print("do you want to  pop?Y/N")
    choice=input("enter your choice:")
    if choice=="Y":
        
        pop()
    else:
        print("no input")
        break
