class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            corr_index = nums[i] - 1
            if nums[i] != nums[corr_index]:
                nums[i], nums[corr_index] = nums[corr_index], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]
        return [-1, -1]