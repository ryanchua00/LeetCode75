class Solution:
    def reverseBits(self, n: int) -> int:
        new = 0
        for i in range(32):
            curr = n >> i
            new &= curr
            new << 1
        return new
