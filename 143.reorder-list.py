class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        midHead = self.revLL(slow.next)
        slow.next = None        # remember to break this link to avoid loops

        # merge the 2 halves (second could be one shorter)
        p1, p2 = head, midHead
        while p2:
            nextp1 = p1.next
            nextp2 = p2.next

            p1.next = p2
            p2.next = nextp1

            p1 = nextp1
            p2 = nextp2

        return

    def revLL(self,head):
        temp = head
        prev = None
        while temp:
            nextnode = temp.next
            temp.next = prev
            prev = temp
            temp = nextnode
        return prev
