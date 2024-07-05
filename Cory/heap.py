from heapq import heapify, heappop, heappush

# left node 2k + 1
# rigt node 2k + 2
a_list = ['R', 'C', 'T', 'H', 'E', 'D', 'L']
heapify(a_list)
print(a_list)

heappop(a_list)
print('After popping')
print(a_list)

heappush(a_list, 'Z')
print('After push')
print(a_list)



#find min cost ropes
def find_min_cost(ropes):
    heapify(ropes)
    cost = 0
    while len(ropes) > 1:
        sum = heappop(ropes) + heappop(ropes)
        heappush(ropes, sum)
        cost += sum
    return cost

class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None
        
    def insert_right(self, value):
        node = BinaryTree(value)
        if not self.right_child:
            self.right_child = node
        else:
            node.right_child = self.right_child
            self.right_child = node
    
    def insert_left(self, value):
        node = BinaryTree(value)
        if not self.left_child:
            self.left_child = node
        else:
            node.left_child = self.left_child
            self.left_child = node
            
def check_heap(tree: BinaryTree):
    current = [tree]
    next = []
    while current:
        for node in current:
            if node.left_child:
                next.append(node.left_child)
            if node.right_child:
                next.append(node.right_child)
            try:
                if node.left_child.key <= node.key and \
                    node.right_child.key <= node.key:
                    return False
            except:
                pass
        current = next
        next = []
    return True

tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)
tree.left_child.insert_left(4)
tree.right_child.insert_right(6)
tree.left_child.insert_right(5)
check_heap(tree)