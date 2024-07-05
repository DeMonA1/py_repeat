class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None
        
    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree
    
    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree
            
    # breadth-first traversal for a tree
    def breadth_first_search(self, n):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.key == n:
                    return True
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
            current = next
            next = []
        return False
    
    def invert(self):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
                tmp = node.left_child
                node.left_child = node.right_child
                node.right_child = tmp
            current = next
            next = []
    
    def has_leaf_nodes(self):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
                if not node.left_child and not node.right_child:
                    return True
            current = next
            next = []
        return False
    
    def invert_preorder(self):
        if self:
            tmp = self.right_child
            self.right_child = self.left_child
            self.left_child = tmp
            print(tree.key)
            preorder(self.left_child)
            preorder(self.right_child)

             
    
# direct order
def preorder(tree):
    if tree:
        print(tree.key)
        preorder(tree.left_child)
        preorder(tree.right_child)

# reverse order
def postorder(tree):
    if tree:
        postorder(tree.left_child)
        postorder(tree.right_child)
        print(tree.key) 

def inorder(tree):
    if tree:
        inorder(tree.left_child)
        print(tree.key)
        inorder(tree.right_child)           
            
tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)
tree.insert_left(4)
tree.left_child.insert_right(6)
tree.insert_right(5)
preorder(tree)
postorder(tree)
tree.invert()
tree.has_leaf_nodes()
tree.invert_preorder()