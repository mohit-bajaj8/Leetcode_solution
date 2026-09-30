class Solution:
    def canJump(self, nums: list[int]) -> bool:
        #TC:O(N) SC:O(1)
        max_index = 0
        n = len(nums)
        for i in range(0,n):
            if i > max_index:
                return False
            max_index = max(max_index, nums[i]+i)
        return True