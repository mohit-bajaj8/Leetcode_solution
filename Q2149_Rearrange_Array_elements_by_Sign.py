class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        i=j=0
        k=1
        while i<len(nums):
            if nums[i]>=0:
                result[j]=nums[i]
                i+=1
                j+=2
            else:
                result[k]=nums[i]
                i+=1
                k+=2
        return result