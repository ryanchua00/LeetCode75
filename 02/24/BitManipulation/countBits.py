from typing import List

'''
n = 4
0 1 2 3 4

0
1
10
11
100
'''


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(n+1):
            curr = i
            count = 0
            while curr > 0:
                if 1 & curr:
                    count += 1
                curr >>= 1
            res.append(count)

        return res
