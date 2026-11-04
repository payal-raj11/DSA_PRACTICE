stack=input("enter the stack:").split(",")
stack=[int(x) for x in stack[0:]]
print(stack)

def display():
    if len(stack)<=0:
        print("underflow")
    else:
        
        print("stack elements:",stack)
        

while True:
    print("do you want to  display?Y/N")
    choice=input("enter your choice:")
    if choice=="Y":
        
        display()
    else:
        print("no input")
        break