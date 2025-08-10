class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        # # solution 1 with TC:O(N) SC:O(N)
        # unique_element={}
        # for num in nums:
        #     unique_element[num]=0
        # j=0
        # for k in unique_element:
        #     nums[j]=k
        #     j+=1
        # return j

        # # solution 2 with TC:O(N) SC:O(1) (This is more optimal.)
        i = 0
        j = 1
        while j < n:
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j = j + 1
        return i + 1