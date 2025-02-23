from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree = {i: [] for i in range(n)}
        for node1, node2 in edges:
            tree[node1].append(node2)
            tree[node2].append(node1)
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in tree[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor):
                    return False
            return True

        return dfs(0, -1) and n == len(visited)
