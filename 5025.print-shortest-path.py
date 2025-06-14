import heapq
from typing import List

class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # making adj list
        # edge[i] = [ai, bi, wti]
        adj = [[] for _ in range(n+1)]
        for n1, n2, wt in edges:
            adj[n1].append((n2, wt))
            adj[n2].append((n1, wt))

        # to keep track of parent node
        parent = list(range(n+1))

        def dijkstrasAlgo():
            '''func for Dijstra's algo'''
            while pq:
                distance, node = heapq.heappop(pq)
                for adjNode, wt in adj[node]:
                    if distance+wt < dist[adjNode]:
                        dist[adjNode] = distance + wt 
                        heapq.heappush(pq, (distance+wt, adjNode))
                        parent[adjNode] = node


        # perform dijkstra's algo
        # to fill parent's & dist list
        pq = []
        dist = [1e9] * (n+1)

        heapq.heappush(pq, (0,1))   # push src node
        dist[1] = 0

        dijkstrasAlgo()


        # check if we were able to reach end node
        if dist[n] == 1e9:
            return [-1]
        
        # traverse from end -> src node via parents
        # to get shortest path
        node = n     
        path = []
        while parent[node] != node:
            path.append(node)
            node = parent[node]
        path.append(1)
        path.reverse()

        # add the distance to starat of path
        path.insert(0, dist[n])
        
        return path