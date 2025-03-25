from typing import List
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flightMap = {}
        for flight in flights:
            src, dst, cost = flight
            if src in flightMap:
                dstMap = flightMap[src]
                dstMap[dst] = cost
            else:
                dstMap = {}
                dstMap[dst] = cost
                flightMap[src] = dstMap
        pq = []
        dist = [float('inf')] * n
        heapq.heappush(pq, (0, 0, src))
        minCost = 1001
        for i in range(k):
            currCost, count, curr = heapq.heappop()
            if curr == dst:
                min(minCost, currCost)
            if count >= k:
                continue
            for flight, cost in flightMap[curr].items():
                heapq.heappush(pq, (cost+currCost, count + 1, flight))

        return minCost if minCost != 1001 else -1

        '''
        # start from dst, bfs outwards to src
        # sort flights
        # index in a dict<int, dict<int, int>>
        # [[1, 0, 100], [1, 2, 200], [0, 2, 100]]
        flights = sorted(flights, key=lambda x: x[0])
        flightMap = {}
        for flight in flights:
            src, dst, cost = flight
            if src in flightMap:
                dstMap = flightMap[src]
                dstMap[dst] = cost
            else:
                dstMap = {}
                dstMap[dst] = cost
                flightMap[src] = dstMap

        # loop k times
        minCost = 1001
        queue = []
        queue.append((src, [src], 0))
        while len(queue) > 0:
            # each loop, step out once from dst to neighbours, and maintain a cost
            # bfs with a local seen(), where each traversal only hits nodes once.
            curr, path, currCost = queue.pop(0)

            if curr == dst:
                minCost = min(minCost, currCost)
                continue

            if len(path) - 1 >= k:
                continue

            for flight, cost in flightMap[curr].items():
                if flight not in path:
                    # update cost
                    newCost = currCost + cost
                    path = path.copy()
                    path.append(flight)
                    # make neighbor
                    queue.insert((curr, path, newCost))

        return minCost if minCost != 1001 else -1
        '''
