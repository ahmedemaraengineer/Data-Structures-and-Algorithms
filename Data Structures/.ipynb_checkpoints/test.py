class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


    def append(self, data):

        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        cur = self.head

        while cur.next:
            cur = cur.next

        cur.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        new_node = Node(data)
        if not prev_node:
            print("This Node Isn't Available")

        new_node.next = prev_node.next
        prev_node.next = new_node


    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None





















ls = LinkedList()

ls.append('A')
ls.append('H')
ls.append('M')
ls.append('E')
ls.append('D')
ls.prepend('Mr/')
ls.insert_after_node(Node('D'), 'E')
ls.delete_node('H')
ls.print_list()
