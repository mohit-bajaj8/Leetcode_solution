class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # # solution 1: TC:O(N^3) SC:O(No of triplets)
        # result=[]
        # myset=set()
        # for i in range(len(nums)-2):
        #     for j in range(i+1,len(nums)-1):
        #         for k in range(j+1,len(nums)):
        #             if nums[i]+nums[j]+nums[k]==0:
        #                 temp=[nums[i],nums[j],nums[k]]
        #                 temp.sort()
        #                 myset.add(tuple(temp))
        # result=[ list(ans) for ans in myset]
        # return result

        # # solution 2: TC:O(N^2) SC:O(N)+O(No. of triplets)
        # result=[]
        # myset=set()
        # no=set()
        # for i in range(len(nums)):
        #     no=set()
        #     for j in range(i+1,len(nums)):
        #         third=-(nums[i]+nums[j])
        #         if third in no:
        #             temp=[nums[i],nums[j],third]
        #             temp.sort()
        #             myset.add(tuple(temp))
        #         no.add(nums[j])

        # result=[list(ans) for ans in myset]
        # return result

        # # solution 3: TC:O(N^2) SC:O(1)
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]
                if total_sum < 0:
                    j += 1
                elif total_sum > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # while j<k and nums[k]==nums[k+1]:
                    #     k-=1
        return result