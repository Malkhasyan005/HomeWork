class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def push_front(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
    
    def pop_front(self):
        if self.head is not None:
            self.head = self.head.next_node
    
    def push_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            current.next_node = new_node

    def pop_back(self):
        if self.head is None:
            return
        if self.head.next_node is None:
            self.head = None
            return
        current = self.head
        while current.next_node.next_node is not None:
            current = current.next_node
        current.next_node = None
    
    def front(self):
        if self.head is not None:
            return self.head.value
        return None
    
    def back(self):
        if self.head is None:
            return None
        current = self.head
        while current.next_node is not None:
            current = current.next_node
        return current.value
    
    def insert_after(self, node, value):
        if node is None:
            return
        new_node = Node(value, node.next_node)
        node.next_node = new_node
    
    def erase_after(self, node):
        if node is not None and node.next_node is not None:
            node.next_node = node.next_node.next_node
    
    def is_empty(self):
        return self.head is None
    
    def clear(self):
        self.head = None
    
    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next_node
        return result
    

lst = SinglyLinkedList()

print(lst.is_empty())

lst.push_front(10)
lst.push_front(20)
print("After push_front 20, 10:", lst.to_list())

lst.push_back(30)
lst.push_back(40)
print("After push_back 30, 40:", lst.to_list())

print("Front:", lst.front())
print("Back:", lst.back())

lst.pop_front()
print("After pop_front:", lst.to_list())

lst.pop_back()
print("After pop_back:", lst.to_list())

first_node = lst.head
lst.insert_after(first_node, 99)
print("After insert_after(first_node, 99):", lst.to_list())

lst.erase_after(first_node)
print("After erase_after(first_node):", lst.to_list())

lst.clear()
print("After clear:", lst.to_list())
print("Empty: ", lst.is_empty())