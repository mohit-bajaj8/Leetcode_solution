class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # solution 1: TC:O(N^2) SC:O(1)
        # max_count=0
        # for i in range(len(nums)):
        #     count=1
        #     num=nums[i]
        #     while num+1 in nums:
        #         count+=1
        #         num=num+1
        #     if max_count<count:
        #         max_count=count
        # return max_count

        # # Solution 2: TC:O(N * logN) SC:O(1)
        # nums.sort()
        # max_count=0
        # count=1
        # if len(nums)==1:
        #     return 1
        # for i in range(len(nums)-1):
        #     if nums[i+1]==nums[i]+1:
        #         count+=1
        #     if max_count<count:
        #         max_count=count
        # return max_count

        # # solution 3: TC:O(N) SC:O(N)
        myset=set()
        count=0
        max_count=0
        for i in range(len(nums)):
            myset.add(nums[i])
        for num in myset:
            if num-1 not in myset:
                count=1
                x=num
                while x+1 in myset:
                    count+=1
                    x+=1
                max_count=max(max_count,count)
        return max_count