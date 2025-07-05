class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push(self, num):
        new_node = Node(num)

        if self.isEmpty():
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = self.tail.next


    def pop(self):
        if self.isEmpty():
            return -1

        else:
            popped_node = self.head
            self.head = self.head.next
            return popped_node.val

    def peek(self):
        if self.isEmpty():
            return -1
        
        else:
            return self.head.val

    def isEmpty(self):
        return self.head == None
