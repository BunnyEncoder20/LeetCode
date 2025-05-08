#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
from queue import Queue
class MyStack:

    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        self.q.put(x)

        # rotate all elements of queue
        # so new element in front of queue
        for i in range(self.q.qsize()-1):
            self.q.put(self.q.get())

    def pop(self) -> int:
        if self.q.empty(): 
            print("Stack empty. Cannot pop")
            return -1
        return self.q.get()

    def top(self) -> int:
        if self.q.empty():
            print("Stack empty. Cannot peek")
            return -1
        return self.q.queue[0]

    def empty(self) -> bool:
        return self.q.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

