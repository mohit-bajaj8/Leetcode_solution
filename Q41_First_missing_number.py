class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=0
        while i < len(nums):
            correct_index=nums[i]-1
            if nums[i]>0 and nums[i]<=len(nums) and nums[i]!=nums[correct_index]:
                nums[correct_index],nums[i]=nums[i],nums[correct_index]
            else:
                i+=1
        i=0
        while i<len(nums):
            if nums[i]!=i+1:
                return i+1
            else:
                i+=1
        return i+1