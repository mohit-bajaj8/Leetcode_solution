class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 0 or nums[0] == nums[len(nums) - 1]:
            return 0
        count = 0
        for i in range(len(nums)):
            if nums[i] != nums[0] and nums[i] != nums[len(nums) - 1]:
                count += 1
        return count






