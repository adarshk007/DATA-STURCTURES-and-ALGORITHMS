# Single_Linked_list
# ADARSH KUMAR
#------------------------------------------------------------------------------#
#Linked List is a linear data structure.
"""
Unlike arrays,
linked list:
elements are not stored at contiguous location;
the elements are linked using pointers.
"""
#Advantages over arrays
"""
1) Dynamic size
2) Ease of insertion/deletion
"""
#Drawbacks:
"""
1) Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do binary search with linked lists.
2) Extra memory space for a pointer is required with each element of the list.
"""
#_____________________________________________________________________________#

class Node:
 
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
 
 
# Linked List class contains a Node object
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data,)
            temp = temp.next
# Code execution starts here
if __name__=='__main__':
 
    # Start with the empty list
    llist = LinkedList()
   #--->> here llist have all the properties shared by linked list class
   #--->>Now we can access the Linkedlist property head by typing llist.head
    # or Linkedlist().head
    """
    The first argument of every class method, including __init__,
    is always a reference to the current instance of the class.
    By convention, this argument is always named self. In the __init__ method,
    self refers to the newly created object; in other class methods,
    it refers to the instance whose method was called.
    """
 
    llist.head  = Node(1)
    
    second = Node(2)
    third  = Node(3)
 
    '''
    Three nodes have been created.
    We have references to these three blocks as first,
    second and third
 
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+
    '''
 
    llist.head.next = second; # Link first node with second 
 
    '''
    Now next of first Node refers to second.  So they
    both are linked.
 
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  | null |     |  3 | null |
    +----+------+     +----+------+     +----+------+ 
    '''
 
    second.next = third; # Link second node with the third node
 
    '''
    Now next of second Node refers to third.  So all three
    nodes are linked.
 
    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->|  3 | null |
    +----+------+     +----+------+     +----+------+ 
    '''
