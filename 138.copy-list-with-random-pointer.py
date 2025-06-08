#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # insert copy nodes in between
        self.putCopy(head)
        
        # connect the random pointers
        self.connRandom(head)
        
        # return deep copy
        return self.getCopy(head)

    def putCopy(self, head):
        temp = head
        while temp:
            tempcopy = Node(temp.val)   # make copy node
            nextnode = temp.next
            temp.next = tempcopy        # connect the nodes
            tempcopy.next = nextnode
            temp = temp.next.next       # move to next node
        return
    
    def connRandom(self, head):
        temp = head
        while temp:
            if temp.random:
                tempcopy = temp.next
                tempcopy.random = temp.random.next
            temp = temp.next.next
        return
    
    def getCopy(self, head):
        dummy = Node(-1)
        temp1 = head
        temp2 = dummy
        while temp1:
            temp2.next = temp1.next         # tempcopy
            temp1.next = temp1.next.next    # next node
            
            # move pointers forward
            temp1 = temp1.next
            temp2 = temp2.next
        return dummy.next

            
            
        
# @lc code=end

