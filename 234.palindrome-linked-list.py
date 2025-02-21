#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # BRUTE FORCE
        # temp = head
        # st = []
        # while temp:
        #     st.append(temp.val)
        #     temp = temp.next
        
        # temp = head
        # while temp:
        #     if temp.val != st.pop():
        #         return False
        #     temp = temp.next
        # return True
        
        # OPTIMAL: rev half of the LL
        if not head and not head.next: return True
        
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        secondHalf = self.reverseLL(slow)
        firstHalf = head
        while secondHalf:
            if firstHalf.val != secondHalf.val:
                return False 
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next
        return True

    def reverseLL(self, temp):
        if not temp or not temp.next:
            return temp
        
        prev = None
        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        
        return prev
        
        
        
            
# @lc code=end

