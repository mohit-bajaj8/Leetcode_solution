class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        # # solution - 3 TC:O(N) SC:O(1) in place change in nums.
        if len(nums) == 0:
            return []
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

        # # solution - 1 TC:O(N) SC:O(1) without considering ans list.
        # if len(nums)==0:
        #     return []
        # ans=[]
        # ans.append(nums[0])
        # for i in range(1,len(nums)):
        #     ans.append(ans[-1]+nums[i])
        # return ans

        # # solution - 2 using recursion
        # if len(nums)==0:
        #     return []
    #     ans=[]
    #     ans.append(nums[0])
    #     ans=self.add(nums,1,ans)
    #     return ans

    # def add(self,nums,i,ans):
    #     if len(nums)==i:
    #         return ans
    #     ans.append(ans[-1]+nums[i])
    #     self.add(nums,i+1,ans)
    #     return ans


