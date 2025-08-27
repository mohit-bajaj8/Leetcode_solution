class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        # # solution - 3 TC:O(N logN) SC:O(1)
        nums.sort()
        i = 0
        j = 1
        count = 0
        pair = 0
        while j < len(nums):
            if nums[i] == nums[j]:
                count += 1
                j += 1
                continue
            else:
                pair += (count + 1) * (count) // 2
                count = 0
                i = j
                j = j + 1
        pair += (count + 1) * (count) // 2
        return pair

        # # solution - 1  TC: O(N^2) SC:(1)
        # pair=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             pair+=1
        # return pair

        # # solution - 2 TC:O(2N) SC:O(N)
        # mydict=dict()
        # for i in nums:
        #     mydict[i]=mydict.get(i,0)+1
        # pair=0
        # for k in mydict:
        #     if mydict[k]>1:
        #         pair+= mydict[k] * (mydict[k]-1)//2
        # return pair






