class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # TC: O(log N) SC: O(1)
        if num == 1 or num == 0:
            return True
        low = 0
        high = num
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = mid + 1
            else:
                high = mid - 1
        if mid * mid == num or (mid + 1) * (mid + 1) == num or (mid - 1) * (mid - 1) == num:
            return True
        else:
            return False

