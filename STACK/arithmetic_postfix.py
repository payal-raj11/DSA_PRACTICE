exp=input("enter the arithmetic expression:")
stack=[]
for i in range(len(exp)):
    if exp[i]=="+" or exp[i]=="-" or exp[i]=="/" or exp[i]=="*":
        a=stack.pop()
        b=stack.pop()
        if  exp[i]=="+":
            stack.append(a+b)
        elif exp[i]=="-":
            stack.append(a-b)
        elif exp[i]=="*":
            stack.append(a*b)
        else:
            stack.append(a//b)
        
    else:
        stack.append(int(exp[i]))
    print(stack)
