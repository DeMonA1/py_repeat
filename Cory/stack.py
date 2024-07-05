class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        return self.items[-1]
    
# Stack via LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        
    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
            
    def pop(self):
        if self.head is None:
            raise IndexError('ppo from empty stack')
        poppednode = self.head
        self.head = self.head.next
        return poppednode.data
    
    stack = Stack()
    for i in range(0, 4):
        stack.push(i)
        print(stack.pop())
        
# simple list
stack = []
print(stack)
stack.append('Kanye West')
print(stack)
stack.append('Jay-Z')
print(stack)
stack.append('Chance the Rapper')
print(stack)
stack.pop()
print(stack)


#stack for list reversing
a_string = 'a string'
a_string[::-1]

''.join(reversed('a string'))

def reverse_string(a_string):
    stack = []
    string = ''
    for c in a_string:
        stack.append(c)
    for c in a_string:
        string += stack.pop()
    return string

print(reverse_string('Bieber'))


# Minimum stack
class MinStack():
    def __init__(self):
        self.main = []
        self.min = []
        
    def push(self, n):
        if len(self.main) == 0:
            self.min.append(n)
        elif n <= self.min[-1]:
            self.min.append(n)
        else:
            self.min.append(self.min[-1])
        self.main.append(n)
    
    def pop(self):
        self.min.pop()
        return self.main.pop()
    
    def get_min(self):
        return self.min[-1]
    
min_stack = MinStack()
min_stack.push(10)
print(min_stack.main)
print(min_stack.min)
min_stack.push(15)
print(min_stack.main)
print(min_stack.min)
print(min_stack.get_min())
min_stack.pop()
print(min_stack.main)
print(min_stack.min)



# BALANCE OF PARANTHESES
def check_parantheses(a_string):
    stack = []
    for c in a_string:
        print(c)
        if c == '(' or c == '{':
            stack.append(c)
        if c == ')':
            if len(stack) == 0:
                return False
            elif '(' in stack:
                stack.remove('(')
                continue
            if len(stack):
                return False
        if c == '}':
            if len(stack) == 0:
                return False
            elif '{' in stack:
                stack.remove('{')
                continue
            if len(stack):
                return False
    return len(stack) == 0

a_string = '{((()()}()))'
check_parantheses(a_string)

class MaxStack:
    def __init__(self):
        self.max = []
        self.real = []
        
    def append(self, data):
        if not self.real:
            self.max.append(data)
        elif data >= self.max[-1]:
            self.max.append(data)
        else:
            self.max.append(self.max[-1])
        self.real.append(data)
    
    def get_max(self):
        return self.max[-1]
    
    def pop(self):
        self.max.pop()
        return self.real.pop()
        

stack = MaxStack()
stack.append(10)
print(stack.max)
print(stack.real)
stack.append(20)
print(stack.max)
print(stack.real)
stack.append(2)
print(stack.max)
print(stack.real)
print(stack.get_max())
stack.pop()
print(stack.max)
print(stack.real)