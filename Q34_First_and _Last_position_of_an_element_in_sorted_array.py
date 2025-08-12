class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        lb = self.lowerbound(nums, target)
        if nums[lb] != target:
            return [-1, -1]
        up = self.upperbound(nums, target)
        return [lb, up - 1]

    # code to find lower bound or starting index of occurence
    def lowerbound(self, nums, target):
        low = 0
        high = len(nums) - 1
        lb = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb

    # code to find upper bound or ending index of occurence
    def upperbound(self, nums, target):
        low = 0
        high = len(nums) - 1
        ub = len(nums)
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub