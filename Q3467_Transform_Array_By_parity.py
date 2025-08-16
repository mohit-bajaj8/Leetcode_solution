class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        odd=0
        even=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                even+=1
            else:
                odd+=1
        for i in range(len(nums)):
            if i<even:
                nums[i]=0
            else:
                nums[i]=1
        return nums