from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input: list of strings
        # outputs: list of list of anagrams strings
        result_map = {}
        for value in strs:
            word_count = [0] * 26
            for char in value:
                word_count[int(char) - int('a')] += 1
            result_map[word_count] = result_map.get(
                word_count, []).append(value)
        return list(result_map.values())
