class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value   

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)                             


class Node:
    def __init__(self, value):
        self.value = value 
        self.right = None 
        self.left = None 


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preordered_print(self.root, "")

        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")

        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")  

        elif traversal_type == "levelorder":
            return self.levelorder_print(self.root)

        elif traversal_type == 'reverse_levelorder':
            return self.reverse_levelorder_print(self.root)

        else:
            print("Traversal type " + str(traversal_type) + "is not supported")    
            return False

    def preordered_print(self, start, traversal):
        """Root -> Left -> Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preordered_print(start.left, traversal)
            traversal = self.preordered_print(start.right, traversal)
        return traversal    

    def inorder_print(self, start, traversal):
        """Left -> Root -> Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal  

    def postorder_print(self, start, traversal):
        """Left -> Right -> Node"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def levelorder_print(self, start):
        if start is None:
            return 
        queue = Queue()
        queue.enqueue(start)  
        traversal = ""    
        while len(queue) > 0:
            traversal +=  str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left) 

            if node.right:
                queue.enqueue(node.right)

        return traversal

    def reverse_levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ""

        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)

            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"
        return traversal

    def height(self, node):
        if node is None:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def size(self):

        start = self.root
        if start is None:
            return 0

        stack = Stack()
        queue = Queue()
        queue.enqueue(start)
        stack.push(start.value)

        while len(queue) > 0:
            node = queue.dequeue()
            if node.right:
                stack.push(node.right)
                queue.enqueue(node.right)
            if node.left:
                stack.push(node.left)
                queue.enqueue(node.left)

        return len(stack)

    def size_recursive(self, node):
        if node is None:
            return 0

        return 1 + self.size_recursive(node.left) + self.size_recursive(node.right)


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)
print(tree.print_tree('preorder'))
print(tree.print_tree('inorder'))
print(tree.print_tree('postorder'))
print(tree.print_tree('levelorder'))
print(tree.print_tree('reverse_levelorder'))
print(tree.height(tree.root))
print(tree.size())
print(tree.size_recursive(tree.root))
