class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x == y:
            return 0
        z = x ^ y
        count = 0
        for i in range(32):
            if z & (1 << i):
                count += 1
        return count
