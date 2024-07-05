from collections import deque
import random


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
        return ''
            
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)
    
    def search(self, target):
        current = self.head
        while current.next:
            if current.data == target:
                return True
            else:
                current = current.next
        return False
    
    def remove(self, target):
        if self.head == target:
            self.head = self.head.next
            return
        current = self.head
        previous = None
        while current:
            if current.data == target:
                previous.next = current.next
            previous = current
            current = current.next

    def reverse_list(self):  # 1 2 3
        current = self.head  # current =       1 
        previous = None      # prev =          None  
        while current:          
            next = current.next     # next =   2     3    
            current.next = previous # cur.next None  1   
            previous = current      # prev =   1     2   
            current = next          # cur =    2     3   
        self.head = previous        #      2-3-1-N | 3-2-1-N  
    
    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while True:
            try:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
            except:
                return False
            
    
a_list = LinkedList()
a_list.append('Tuesday')
a_list.append('Wednesday')

a_list = LinkedList()
for i in range(0, 20):
    j = random.randint(1, 30)
    a_list.append(j)
    print(j, end=' ')
    
    
    
d = deque()
d.append('Harry')
d.append('Potter')
for i in d:
    print(i)
    
    
    
    
# exercise
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
        
class LinkedListNoCycle:
    
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        return ''
    
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        else:
            current = self.head
            while True:
                if not current.next:
                    current.next = Node(data)
                    return
                else:
                    current = current.next
                    
    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while True:
            try:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
            except:
                return False
            
            
class LinkedListWithCycle:
    
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        current = self.head
        while True:
            print(current.data)
            current = current.next
            if current.next is self.head:
                return ''
    
    def append(self, data):
        if not self.head:
            self.head = Node(data) 
            return
        else:
            current = self.head
            while True:
                if not current.next or current.next is self.head:
                    current.next = Node(data)
                    current.next.next = self.head
                    return
                else:
                    current = current.next 
                       
    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while True:
            try:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
            except:
                return False
         
                       
a_list = LinkedListNoCycle()
for i in range(1, 101):
    a_list.append(i)
print(a_list)
a_list.detect_cycle()

list2 = LinkedListWithCycle()
for i in range(1, 102):
    list2.append(i)
    print('success - ',i)
print(list2)
list2.detect_cycle()