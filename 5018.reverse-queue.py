from queue import Queue
class Solution:
    def reverseQueue(self, q:Queue):
        # base case
        if q.empty(): return

        front = q.get()
        self.reverseQueue(q)
        q.put(front)
        return

if __name__ == "__main__":
    q = Queue()
    elements = [4,3,1,10,2,6]
    for e in elements: q.put(e)
    Solution().reverseQueue(q)
    while not q.empty():
        print(q.get(), end=" - ")
