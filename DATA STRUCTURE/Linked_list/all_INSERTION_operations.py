# Single_Linked_list
#SUB TOPICS :
"""
INSERTION:
     1}insertion in the beginning
     2}insertion in the end
     3}insertion at the given position
DELETION:
     1}deletion in the beginning
     2}deletion in the end
     3}deletion at the given position
PRINTING
     1}elements in a list
     2}current size
"""
# ADARSH KUMAR
#------------------------------------------------------------------------------#

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0
    def getsize(self):
        print("size:",self.size,sep=" ")
    def add(self,d,pos):
        if(pos==0):   #this shows insertion in the beginning
            node=Node(d)
            if(self.head is None):
                self.head=node
            else:
                z=self.head    #self.head is same as k.next self.head means pointing to the next Node
                self.head=node
                node.next=z
            self.size=self.size+1
        else:
            node=Node(d)
            ze=pos
            self.size=self.size+1
            if(self.head is None):
                        self.head=node
            else:
                        cur=self.head
                        pos=pos-1
                        while(pos>0):
                            print(pos)
                            pos=pos-1
                            cur=cur.next
                        w=cur.next
                        cur.next=node
                        node.next=w
        """if(pos==self.size-1):   #insertion in the end
            node=Node(d)
            if(self.head is None):
                self.head=node
            else:
                cur=self.head
                while(cur.next is not None):
                    cur=cur.next
                cur.next=node
            self.size=self.size+1"""
        """#if(pos>0 and pos<self.size):#insertion at the given position"""
      
    def printlist(self):
        cur=self.head
        print("Head")
        while(cur.next is not None):
            print(cur.data,end="--->")
            cur=cur.next
        print(cur.data,end="--->None\n")
    def delete(self,pos):
        y=pos
        if(self.head is None): #if there is no element
            print("No element is present")
        elif(pos==self.size-1):# to remove Node element from last
            z=self.head
            while(z.next.next is not None):
                z=z.next
            z.next=None
            self.size-=1
        elif(pos==0): #to remove Node element from starting/beginning
            k=self.head
            yu=self.head.next
            self.head=yu
            self.size-=1
        elif(0<pos<self.size-1): #to remove element from any position in between
            e=self.head
            while(pos>1):
                pos=pos-1
                e=e.next
            k=e.next.next
            e.next=k
            self.size-=1
            
mylist=LinkedList()
mylist.add(1,0)
mylist.add(2,0)
mylist.add(3,1)
mylist.add(4,2)
mylist.add(5,4)
mylist.getsize()
mylist.printlist()
mylist.delete(3)
mylist.getsize()
mylist.printlist()
#______________________________________________________________________________#
#recursive way of counting elements
"""
    def getCountRec(self, node):
        if (not node): # Base case
            return 0
        else:
            return 1 + self.getCountRec(node.next)
 
    # A wrapper over getCountRec()
    def getCount(self):
       return self.getCountRec(self.head)

"""
