#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, key=-1, val=None, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.mpp = {}
    
    def connectAtHead(self,node):
        back = self.head
        front = self.head.next
        
        back.next = node
        node.prev = back
        node.next = front
        front.prev = node
        return 
    
    def disconnect(self,node):
        back = node.prev
        front = node.next
        back.next = front
        front.prev = back
        return 
        

    def get(self, key: int) -> int:
        if key not in self.mpp: return -1
        node = self.mpp[key]
        # update to MRU
        self.disconnect(node)
        self.connectAtHead(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        # if node already present, update the value
        if key in self.mpp:
            node = self.mpp[key]
            node.val = value
            self.disconnect(node)
            self.connectAtHead(node)
        else: 
            if self.capacity == len(self.mpp):
                # remove lru
                lru = self.tail.prev
                self.disconnect(lru)
                del self.mpp[lru.key]

            node = Node(key, value)
            self.mpp[key] = node
            self.connectAtHead(node)
        return
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

