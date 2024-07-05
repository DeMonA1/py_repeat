from queue import Queue


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue1:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
        
    def enqueue(self, item):
        self._size += 1
        node = Node(item)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    
    def dequeue(self):
        if self.front is None:
            raise IndexError('pop from empty queue')
        self._size -= 1
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data

    def size(self):
        return self._size
    
queue = Queue1()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.size())
for i in range(3):
    print(queue.dequeue())
    
    

q = Queue()
q.put('a')
q.put('b')
q.put('c')
print(q.qsize())
for i in range(3):
    print(q.get())
    
    

class QueueStack:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def enqueue(self, item):
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        self.s1.append(item)
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())
    
    def enqueue1(self, item):
        self.s2.append(item)
        self.s1 = list(reversed(self.s2))
        
    def dequeue(self):
        if len(self.s1) == 0:
            raise Exception('Cannot pop from empty queue')
        return self.s1.pop()
    
queue = QueueStack()
queue.enqueue1(1)
queue.enqueue1(2)
queue.enqueue1(3)
for i in range(3):
    print(queue.dequeue())