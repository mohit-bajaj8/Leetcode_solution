class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # solution 1 : TC: O(N^2) SC:O(1)
        # i=0
        # while i<len(nums)-1:
        #     j=i+1
        #     while j< len(nums):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        #         else:
        #             j+=1
        #     i+=1
        # # solution 2: TC: O(N) SC:O(N)
        freq={}
        for i in range(len(nums)):
            sub=target-nums[i]
            if sub in freq:
                return [i,freq[sub]]
            else:
                freq[nums[i]]=i