class Solution:
    def findMin(self, nums: List[int]) -> int:
        # TC : O(Log N) SC: O(1)
        low = 0
        high = len(nums) - 1
        mini = float("inf")
        while low <= high:
            mid = (low + high) // 2
            if mini >= nums[mid]:
                mini = nums[mid]
            if nums[mid] <= nums[high]:
                if mini >= nums[mid]:
                    mini = nums[mid]
                high = mid - 1
            else:
                if mini >= nums[low]:
                    mini = nums[low]
                low = mid + 1
        return mini
