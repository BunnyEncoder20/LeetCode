from collections import defaultdict

class Solution:
    # backtracking
    def isHamiltonianPath(self, N, Edges):
        def backtracking(node, vis, count):
            # base case: all nodes covered
            if count == N:
                return True
            
            for i in adj[node]:
                if i not in vis:
                    vis.add(i)
                    if backtracking(i, vis, count+1):
                        return True
                    
                    # backtrack
                    vis.remove(i)
            
            return False

        # construct adj
        adj = defaultdict(list)
        for u,v in Edges:
            adj[u].append(v)
            adj[v].append(u)
        
        for node in range(N):
            if backtracking(node, set(), 1):
                return True
        
        return False
    
# Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Hamiltonian Path Exists (Simple Chain)
    V1 = 4
    edges1 = [(0, 1), (1, 2), (2, 3)]
    print("Test Case 1:", sol.isHamiltonianPath(V1, edges1))  # Expected: True

    # Test Case 2: Hamiltonian Path Exists (Cycle Graph)
    V2 = 5
    edges2 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
    print("Test Case 2:", sol.isHamiltonianPath(V2, edges2))  # Expected: True

    # Test Case 3: Hamiltonian Path Does NOT Exist (Disconnected Graph)
    V3 = 5
    edges3 = [(0, 1), (1, 2), (3, 4)]  # No connection between (2,3)
    print("Test Case 3:", sol.isHamiltonianPath(V3, edges3))  # Expected: False

    # Test Case 4: Hamiltonian Path Exists (Tree Graph)
    V4 = 6
    edges4 = [(0, 1), (1, 2), (1, 3), (3, 4), (4, 5)]
    print("Test Case 4:", sol.isHamiltonianPath(V4, edges4))  # Expected: True


    # Test Case 5: Large Graph (Checking Performance)
    V5 = 10
    edges5 = [(i, i+1) for i in range(9)]  # Linear chain 0-1-2-...-9
    print("Test Case 5:", sol.isHamiltonianPath(V5, edges5))  # Expected: True