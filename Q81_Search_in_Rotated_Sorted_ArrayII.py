class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # TC: O(Log N) for best/average case, O(N/2) for worst case
        # SC: O(1)
        if len(nums) == 0:
            return False
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            elif nums[low] == nums[mid] == nums[high]:
                low = low + 1
                high = high - 1
            else:
                if nums[mid] <= nums[high]:
                    if nums[mid] <= target <= nums[high]:
                        low = mid + 1
                    else:
                        high = mid - 1
                else:
                    if nums[low] <= target <= nums[mid]:
                        high = mid - 1
                    else:
                        low = mid + 1
        return False
