# QUEUE
#SUB TOPICS :
"""
    1}Enqueue
    2}Dequeue
    3}Print: rear element
             front element
"""
# ADARSH KUMAR
#__________________________________CODE________________________________________#

class queue:
    def __init__(self):
        self.new_queue=[]
        self.size=0
        self.front=0
        self.rear=0
    def enqueue(self,data):
        self.new_queue.append(data)
        self.rear=self.rear+1
        self.size=self.size+1
    def dequeue(self):
        self.new_queue.pop(0)
        self.front=self.front+1
        self.size=self.size-1
    def printque(self):
        print("front is on",self.front,sep=" ")
        print("rear is on",self.rear,sep=" ")
        print("size:",self.size,"and queue is:",self.new_queue,sep=" ")
que=queue()
que.enqueue(4)
que.enqueue(5)
que.printque()
que.dequeue()
que.printque()
        
