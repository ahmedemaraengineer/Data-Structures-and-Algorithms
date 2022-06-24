class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)
    
    def print_stack(self):
        return self.items
    

class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):  # adds a new item to the rear of the queue
        self.items.insert(0, item)
        
    def dequeue(self):  # removes the front item from the queue and returns that item
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def print_queue(self):
        return self.items
    
class Deque:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def add_front(self, item):
        self.items.append(item)
        
    def add_rear(self, item):
        self.items.insert(0, item)
        
    def remove_front(self):
        return self.items.pop()
    
    def remove_rear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def print_deque(self):
        return self.items
    
class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next
        
class UnorderedList:
    def __init__(self):
        self.head = None
        # Uptill now the unordered list class returns an empty list
        # because the head(the first node in the class) is None
    
    def is_empty(self):
        return self.head == None
    
    # we need to add items in this unordered list
    # the specific location of the new item is not important , the new item can gow       anywhere 
    # the only way to specify the order of the list is by the next pointer
    # that points from a node to another
    def add(self, item):  
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp 
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
            
        return count
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found        
    
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
            
        else:
            previous.set_next(current.get_next())
            
    def print_list(self):
        a = []
        current = self.head
        while current is not None:
            nxt = current.get_next()
            a.append(current.data)
            current = current.get_next()
            
        return a    
                
        
        
class OrderedList:
    def __init__(self):
        self.head = None
   
    def is_empty(self):
        return self.head == None
    
    # we need to add items in this unordered list
    # the specific location of the new item is not important , the new item can gow anywhere 
    # the only way to specify the order of the list is by the next pointer
    # that points from a node to another
    def add(self, item):  
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp 
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
            
    def search(self, item):
        current = self.head
        found = False
        stop = False
        
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
        return found            
    
    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()
        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)
            
    def print_list(self):
        a = []
        current = self.head
        while current is not None:
            nxt = current.get_next()
            a.append(current.data)
            current = current.get_next()
            
        return a                        
    
    
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))
        
        if self.slots[hash_value] == None:  # If that slot is empty 
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:  # If it's not empty or empty but it's the wanted slot
                self.data[hash_value] = data  # Replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots))  
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))
                    
                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data  # replace
    
    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key, data)
    
    def hash_function(self, key, size):
        return key % size
    
    def rehash(self, old_hash, size):
        return (old_hash + 1) % size    