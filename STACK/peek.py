stack=input("enter the stack:").split(",")
stack=[int(x) for x in stack[0:]]
print(stack)

def peek():
    if len(stack)<=0:
        print("underflow")
    else:
        
        print("top element:",stack[-1])
        

while True:
    print("do you want to  peek?Y/N")
    choice=input("enter your choice:")
    if choice=="Y":
        
        peek()
    else:
        print("no input")
        break