class Solution:
    def answer(self, nums):
        # # solution 2: Without Sorting
        n = len(nums)
        sum = 0
        for i in nums:
            sum += i
        return int((n * (n + 1) / 2) - sum)

        # # Solution 1: Using cyclic sort
        # i=0
        # while i < len(nums):
        #     if nums[i] < len(nums) and nums[i] != i:
        #         nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        #     else:
        #         i+=1

        # i=0
        # while i<len(nums):
        #     if nums[i]!=i:
        #         return i
        #     else:
        #         i+=1
        # if i==len(nums):
        #     return i

    def missingNumber(self, nums: List[int]) -> int:
        ans = self.answer(nums)
        return (ans)