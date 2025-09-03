class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # # TC:O(16)
        if n > 0 and n & (n - 1) == 0:
            for i in range(0, 32, 2):
                if n & (1 << i):
                    return True
            else:
                return False
        return False


