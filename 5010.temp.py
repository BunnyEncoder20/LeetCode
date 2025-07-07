import heapq
class Solution:
    def dijkstra(self, V, adj, S):
        pq = []
        dist = [int(1e9)] * V

        # init minheap with Source node
        dist[S] = 0
        heapq.heappush(pq, (dist[S], S))

        while pq:
            distance2here, node = heapq.heappop(pq)

            for adjnode, distance2next in adj[node]:
                if distance2here + distance2next < dist[adjnode]:
                    dist[adjnode] = distance2here + distance2next
                    heapq.heappush(pq, (dist[adjnode], adjnode))
        
        return dist