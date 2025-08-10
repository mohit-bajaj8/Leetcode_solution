class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # # solution 1: TC:O(N^2) SC:O(1)
        # maxi=float("-inf")
        # if len(nums)==1:
        #     return nums[0]
        # for i in range(len(nums)-1):
        #     sum=nums[i]
        #     for j in range(i+1,len(nums)):
        #        sum+=nums[j]
        #        if maxi<sum:
        #         maxi=sum
        #     if maxi<sum:
        #         maxi=sum
        # return maxi

        # # solution 2: TC:O(N) SC:O(1)
        maxi=float("-inf")
        total=0
        for i in range(len(nums)):
            total +=nums[i]
            if maxi<total:
                maxi=total
            if total < 0:
                total = 0
        return maxi