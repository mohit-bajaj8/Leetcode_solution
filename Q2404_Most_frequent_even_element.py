class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # TC:O(N logN) and SC:O(1)
        if len(nums) == 0:
            return -1
        count = 0
        max_count = 0
        nums.sort()
        ans = -1
        n = float("-inf")
        for i in nums:
            if i % 2 == 0 and n == i:
                count += 1
                if count > max_count:
                    max_count = count
                    ans = n
            elif i % 2 == 0:
                count = 1
                n = i
                if count > max_count:
                    max_count = count
                    ans = n
            else:
                count = 0
        return ans












