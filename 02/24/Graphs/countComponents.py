from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adjMap = {i: [] for i in range(n)}
        for edge in edges:
            adjMap[edge[0]].append(edge[1])
            adjMap[edge[1]].append(edge[0])

        def dfs(node):
            if node not in visited:
                visited.add(node)
                for edge in adjMap[node]:
                    dfs(edge)

        components = 0
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)

        return components
