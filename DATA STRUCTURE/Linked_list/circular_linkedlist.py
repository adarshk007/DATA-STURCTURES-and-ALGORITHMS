#Circular_linked_list
#SUB TOPICS :
"""

   * Insertion in an empty list
   * Insertion at the beginning of the list
   * Insertion at the end of the list
   * Insertion in between the nodes

"""
# ADARSH KUMAR
#--------------------------------Description-----------------------------------#
"""
Circular linked list:
Is a linked list where all nodes are connected to form a circle.
There is no NULL at the end.
A circular linked list can be a singly or doubly circular linked list.
"""
#APPLICATION
"""
Used in queues
Used in Fibonacci Heap. 
"""
#__________________________________CODE________________________________________#

class Node(object):     #not necessary to use define object
    def __init__(self,data):
        self.data=data
        self.next=None
class Circular_Linked_List(object):
    def __init__(self):     #self has always the last with none instance
        self.last=None      #here we have initialised with last only
        self.size=0
#therefore,only last will be available after object function calling
    def add1(self,data):
        """Insertion in an empty list"""
        node=Node(data)
        self.last=node
        node.next=node
        self.size=self.size+1
    def add(self,data,pos):
        if(self.last is None):
            self.add1(data)
        elif(self.last is not None):
            if(pos==0):
            #Insertion in beginning of the list
                
                node=Node(data)
                node.next=self.last.next
                self.last.next=node
            #insertion in the end
            elif(pos==self.size):
                node=Node(data)
                node.next=self.last.next
                self.last.next=node
                self.last=node
                
            elif(pos>0 and pos<self.size):
            #insertion in between 2 nodes
            
                node=Node(data)
                cur=self.last
                while(pos>0):
                    pos=pos-1
                    cur=cur.next
                y=cur.next
                cur.next=node
                node.next=y
            self.size=self.size+1
    def getsize(self):   #to print size
        print("size",self.size,sep=" ")
    def printele(self):   #to print elements
        e=self.size
        cur=self.last.next
        print("circular_linked_list :",end=" ")
        while(e>0):
            e=e-1
            print(cur.data,end=" ")
            cur=cur.next
        print()
n=Circular_Linked_List()
n.add(5,0)
n.add(4,0)
n.add(3,1)
n.getsize()
n.printele()
