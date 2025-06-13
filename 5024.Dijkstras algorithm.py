import heapq

class Solution:
    # Solution1: Using PQ
    def dijkstraAlgo(self, V, adj, S):
        # PQ minheap = [(dist, node)]
        pq = []
        heapq.heappush(pq, (0,S))

        # distance list
        dist = [int(1e9)]*V
        dist[S] = 0

        while pq:
            distance, node = heapq.heappop(pq)
            for adjNode, edgeWt in adj[node]:

                # if dist shorter to adj, update dist[adj] and append into PQ
                if distance + edgeWt < dist[adjNode]:
                    dist[adjNode] = distance + edgeWt
                    heapq.heappush(pq, (dist[adjNode], adjNode))
        
        return dist
