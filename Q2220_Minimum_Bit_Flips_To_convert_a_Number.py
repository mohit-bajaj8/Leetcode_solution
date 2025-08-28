class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # # TC:O(32) SC:O(1)
        ans = start ^ goal
        count = 0
        for i in range(32):
            if ans & (1 << i):
                count += 1
        return count

