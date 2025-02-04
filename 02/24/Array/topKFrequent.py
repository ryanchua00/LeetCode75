from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count frequency of integers - map
        numFreq = {}
        for num in nums:
            numFreq[num] = numFreq.get(num, 0) + 1

        # sort map
        sorted_freq = sorted(numFreq, key=lambda kv: (
            kv[1], kv[0]), reverse=True)

        # return first k values
        return sorted_freq.values()[:k]
