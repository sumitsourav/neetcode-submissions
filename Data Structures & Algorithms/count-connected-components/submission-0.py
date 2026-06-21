class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visited = set()
        component = 0
        def dfs(i):
            for nei in adj[i]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                component += 1
        return component

            
            


