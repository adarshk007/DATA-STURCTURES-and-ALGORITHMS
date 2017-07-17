# Single_Linked_list
#SUB TOPIC :
"""
     1}insertion in the beginning
     2}insertion in the end
     3}insertion at the give position
"""
# ADARSH KUMAR
"""
Start by thinking of a class as an object.  Imagine a class as a container,
like that glass or plastic bottle you drink your favorite beverage from.
Even something this simple has specifications - it has a size.
It can only hold so much.
A beverage company puts something in it.
You take it out.
It's used for storing something.
"""#More commonly, classes can store things and do things.
"""
Think about a modern digital camera as an object.
You take pictures with it - it captures images and stores them.
They also let you do things with the stored images, like cropping and stitching.
Both of these objects, a bottle and a camera, can be represented as classes.
"""
#------------------------------------------------------------------------------#
import copy
class Node:
    def __init__(self,d):
        self.data=d
        self.next=None
class LinkedList:
    def __init__(self,head=None):
        self.head=head
        self.size=0 # or directly initialise with size=0 on top as a regular initialisation in a variable
    def getsize(self):
         print("size:",self.size,sep=" ")
    def add(self,d):
        node=Node(d)
        cur=(self.head)
        if(self.head==None):  #or self.head is None
            self.head=node
        else:
            while(cur.next!= None): # or self.head is Not None
                cur=cur.next
            cur.next=node
        self.size+=1
    def printlist(self):
        cur=self.head
        print("Head")
        while(cur.next is not None):
            print(cur.data,end="--->")
            cur=cur.next
        print(cur.data,end="--->None\n")
mylist=LinkedList()
mylist.add(5)
mylist.add(6)
mylist.printlist()
mylist.getsize()
