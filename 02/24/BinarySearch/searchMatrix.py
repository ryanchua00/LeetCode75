class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search vertically first
        # if target < matrix[i][0],
        # r = mid + 1
        # elif target > matrix[i][0]
        # l = mid
        # else:
        # return True

        vl, vr = 0, len(matrix) - 1
        while vl <= vr:
            mid = vl + (vr - vl) // 2
            if target < matrix[mid][0]:
                vr = mid - 1
            elif target > matrix[mid][0]:
                vl = mid + 1
            else:
                return True

        curr = -1
        if vr < 0:
            curr = vl
        elif vl >= len(matrix):
            curr = vr
        elif target > matrix[vr][0] and target < matrix[vl][0]:
            curr = vr
        else:
            curr = vl

        # search horizontally
        hl, hr = 0, len(matrix[0]) - 1
        while hl <= hr:
            mid = hl + (hr - hl) // 2
            if target < matrix[curr][mid]:
                hr = mid - 1
            elif target > matrix[curr][mid]:
                hl = mid + 1
            else:
                return True

        return False
