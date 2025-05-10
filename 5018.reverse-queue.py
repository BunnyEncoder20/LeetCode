from queue import Queue
class Solution:
    #Function to reverse the queue.
    def reverseQueue(self, q):
        stack = []
        
        while not q.empty():
            stack.append(q.get())
            
        while stack:
            q.put(stack.pop())
        
        return q

if __name__ == "__main__":
    q = Queue()
    elements = [4,3,1,10,2,6]
    print(Solution().reverseQueue(q))
