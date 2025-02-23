from typing import List

# The pair [0, 1], indicates that must take course 1 before taking course 0.
#

# [[2,1], [5,2], [3,2], [2,4]]


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqMap = {i: [] for i in range(numCourses)}
        seen = set()
        for crs, pre in prerequisites:
            reqMap[crs].append(pre)

        def dfs(crs):
            if crs in seen:
                return False
            if reqMap[crs] == []:
                return True
            seen.add(crs)
            for pre in reqMap[crs]:
                if not dfs(pre):
                    return False
            seen.remove(crs)
            reqMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
