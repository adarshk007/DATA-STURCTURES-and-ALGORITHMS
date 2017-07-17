# STACKS
#SUB TOPICS :
"""
    PUSH()        #to push element in last
    POP()         #to remove last element
    PEEK()        #to peek the top element
    PRINTSTACK()  #to print all the elements of stack
"""
# ADARSH KUMAR

#Pros: Easy to implement. Memory is saved as pointers are not involved.
#Cons:  #It is not dynamic.
        #It doesn’t grow and shrink depending on needs at runtime
#Time Complexity:O(1) for each case except print stack it yakes O(n)

#__________________________________CODE________________________________________#

def createstack():
    newstack=[]
    size=0
    return(newstack,size)
def push(stack,element,size):
    stack.append(element)
    size=size+1
    return(size)
def pop(stack,size):
    if(size==0):
        print("Stack Is Empty")
    else:
        stack.pop(-1)
        size=size-1
        return(size)
def peek(stack):
    print("top element is",stack[-1],sep=" ")
def printstack(stack,size):
    for i in range(size-1,-1,-1):
        print(stack[i],"||",sep=" ",end=" ")
    print("start",end=" ")
    print()
stack,size=createstack()
size=push(stack,5,size)
size=push(stack,6,size)
size=push(stack,7,size)
printstack(stack,size)
peek(stack)
size=pop(stack,size)
print(size)
printstack(stack,size)
