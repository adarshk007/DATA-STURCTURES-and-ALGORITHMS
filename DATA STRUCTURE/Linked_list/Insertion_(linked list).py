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
import time

class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def traverse(self):
		printvalue = self.head
		while printvalue is not None:
			print(printvalue.data)
			printvalue = printvalue.next

	def insertAtBegining(self, head):
		newNode = Node(head)

		# updating the node
		newNode.next = self.head
		self.head = newNode

	def insertAtEnd(self, newNode):
		newNode = Node(5)
		if self.head is None:
			self.head = newNode
			return
		lastnode = self.head
		while (lastnode.next):
			lastnode = lastnode.next
		lastnode.next = newNode

linkedList = LinkedList()
headNode = linkedList.head = Node(1)

second = Node(2)
# Linking the node to previous node
headNode.next = second

third = Node(3)
# Linking the node to previous node
second.next = third

forth = Node(4)
# Linking the node to previous node
third.next = forth

fifth = Node(5)
# Linking the node to previous node
forth.next = fifth

sixth = Node(6)

linkedList.traverse()
