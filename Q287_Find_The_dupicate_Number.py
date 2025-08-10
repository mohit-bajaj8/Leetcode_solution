class Solution:
    def answer(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] != (i + 1):
                if nums[i] == nums[nums[i] - 1]:
                    return nums[i]
                else:
                    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

    def findDuplicate(self, nums: List[int]) -> int:
        ans = self.answer(nums)
        return ans