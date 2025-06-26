from collections import deque

class Solution:
    def findOrder(self, dict, N, K):
        dag = {chr(ord('a')+i):[] for i in range(K)} # could also be defaultdict
        indeg = {chr(ord('a')+i): 0 for i in range(K)}

        # construct dag and indeg
        for i in range(N-1):
            w1,w2 = dict[i], dict[i+1]
            length = min(len(w1), len(w2))

            # find the first diff ch 
            # and make edge, break off (cause me know why this word before)
            for j in range(length):
                if w1[j] != w2[j]:
                    dag[w1[j]].append(w2[j])
                    indeg[w2[j]] += 1
                    break
        
        # Topo Sort | Kahn's Algo
        topo_order = []
        q = deque([ch for ch in indeg if indeg[ch] == 0])

        # BFS
        while q:
            ch = q.popleft()
            topo_order.append(ch)

            for next_ch in dag[ch]:
                indeg[next_ch] -= 1
                if indeg[next_ch] == 0:
                    q.append(next_ch)
        
        # only return if topo order is possible
        if len(topo_order) == K:
            return "".join(topo_order)
        else:
            return ""
        
            

print(Solution().findOrder(["baa","abcd","abca","cab","cad"], 5, 4))
# output: b d a c (one possibility)