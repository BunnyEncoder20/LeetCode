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
        # get surr nodes
        headnext = self.head.next
        
        # conn
        self.head.next = node
        node.next  = headnext
        headnext.prev = node
        node.prev = self.head
    
    def disconnect(self,node):
        # get surr node 
        prevnode = node.prev
        nextnode = node.next
        
        # diconnect node
        node.next = None
        node.prev = None
        
        # connect next and prev
        if prevnode:
            prevnode.next = nextnode
        if nextnode:
            nextnode.prev = prevnode
        

    def get(self, key: int) -> int:
        # edge case
        if key not in self.mpp.keys():
            return -1
        
        # get node
        n = self.mpp[key]

        # make MRU
        self.disconnect(n)
        self.connectAtHead(n)

        # return
        return n.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.mpp.keys():
            # update val of node
            oldnode = self.mpp[key]
            oldnode.val = value
            
            # make MRU
            self.disconnect(oldnode)
            self.connectAtHead(oldnode)
            
            
        else:
            # check if DLL at capacity 
            if len(self.mpp) == self.capacity:
                # remove LRU
                lru = self.tail.prev
                self.disconnect(lru)        # del from DLL
                del self.mpp[lru.key]       # del from mpp
                
            # make new node
            newnode = Node(key, value)
            
            # conn
            self.connectAtHead(newnode)
            
            # entry into mpp
            self.mpp[key] = newnode
            
        return
            
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

