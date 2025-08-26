class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # # TC:O(N) SC:O(N) if we consider new ans list in space complexity.
        if len(nums) <= 2:
            return nums
        ans = []
        i = 0
        j = len(nums) // 2
        k = 0
        while k < len(nums):
            if k % 2 == 0:
                ans.append(nums[i])
                i += 1
            else:
                ans.append(nums[j])
                j += 1
            k += 1
        return ans




