class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # # solution-1 TC:O(N),SC:O(N)
        # non_zero=[]
        # for i in nums:
        #     if i!=0:
        #         non_zero.append(i)
        # for i in range(len(nums)):
        #     if i<len(non_zero):
        #         nums[i]=non_zero[i]
        #     else:
        #         nums[i]=0

        # # Solution-2 TC:O(N)  SC:O(1)
        i=j=0
        while j<len(nums):
            if nums[i]!=0:
                i+=1
                j+=1
            elif nums[i]==0 and nums[j]==0:
                j+=1
            else:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
                i+=1
