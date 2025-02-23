from typing import List
import math


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 1:
            return matrix
        # layer index
        layers = math.ceil(len(matrix)/2)
        print("layers", layers)
        for layer in range(layers):
            # case:
            # [[1],
            #  [2]]
            if len(matrix) - layer * 2 == 1:

            print("layer", layer)
            # top left to top right- 1
            for i in range(layer, len(matrix[0]) - 1 - layer):
                print(matrix[layer][i])
                res.append(matrix[layer][i])
            # top right to bottom right - 1
            for i in range(layer, len(matrix) - 1 - layer):
                print(matrix[i][len(matrix[0]) - 1 - layer])
                res.append(matrix[i][len(matrix[0]) - 1 - layer])
            # bottom right to bottom left - 1
            for i in range(len(matrix[0]) - 1 - layer, layer, -1):
                res.append(matrix[len(matrix) - 1 - layer][i])
            # bottom left to top left - 1
            for i in range(len(matrix) - 1 - layer, layer, -1):
                res.append(matrix[i][layer])
        return res
