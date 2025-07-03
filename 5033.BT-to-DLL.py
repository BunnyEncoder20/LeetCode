class Solution:
    def __init__(self):
        self.head = None 
        self.tail = None
        
    def bToDLL(self,root):
        if not root:
            return root
        self.link(root)
        return self.head
    
    def link(self, node):
        if node:
            self.link(node.left)
            
            if self.tail == None:
                self.head = node
            else:
                self.tail.right = node
                node.left = self.tail
            self.tail = node
                
            self.link(node.right)