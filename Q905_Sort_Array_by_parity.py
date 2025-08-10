class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # # solution 1: TC:O(N) SC:O(N)
        # if len(nums)<=1:
        #     return nums
        # even=[]
        # odd=[]
        # for i in nums:
        #     if i%2==0:
        #         even.append(i)
        #     else:
        #         odd.append(i)
        # for i in odd:
        #     even.append(i)
        # return even

        # # Solution TC:O(N) SC:O(1)
        if len(nums) <= 1:
            return nums
        i = 0
        for j in range(len(nums)):
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums