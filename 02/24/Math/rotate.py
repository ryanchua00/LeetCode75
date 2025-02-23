from typing import List
import math


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Cant use another matrix - rotate in-place
        # rotate clockwise
        # rotation is not single element, it is 90 degrees clockwise
        # [[7,4,1]    []
        #  [8,5,2]
        #  [9,6,3]]
        # 1/2 -> 1 3/4 -> 2 5/6 -> 3
        layers = math.ceil(len(matrix)/2)

        queue = []
        for layer in range(layers):
            # edge case: 1 item
            if len(matrix[layer]) == 1:
                continue

            # top left to top right - 1
            for i in range(layer, len(matrix) - layer - 1):
                queue.append(matrix[layer][i])

            # top right to bottom right - 1
            for i in range(layer, len(matrix) - layer - 1):
                queue.append(matrix[i][len(matrix) - 1 - layer])
                matrix[i][len(matrix) - 1 - layer] = queue.pop(0)

            # bottom right to bottom left - 1
            for i in range(len(matrix) - 1 - layer, layer, -1):
                queue.append(matrix[len(matrix) - 1 - layer][i])
                matrix[len(matrix) - 1 - layer][i] = queue.pop(0)

            # bottom left to top left - 1
            for i in range(len(matrix) - 1 - layer, layer, -1):
                queue.append(matrix[i][layer])
                matrix[i][layer] = queue.pop(0)

            # top left to top right - 1
            for i in range(layer, len(matrix) - 1 - layer):
                matrix[layer][i] = queue.pop(0)

        return


'''
[[5, 1, 9, 11],
 [2, 4, 8, 10],
 [13, 3, 6, 7],
 [15, 14, 12, 16]]

 expected: [[15,13,2,5],
            [14,3,4,1],
            [12,6,8,9],
            [16,7,10,11]]

 result: [[15,13,2,5],
          [14,4,4,1],
          [12,3,8,9],
          [16,7,10,11]]
'''
