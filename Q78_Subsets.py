# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:

#         # # TC:O(2^N * N) SC:O(2^N * N)
#         n=len(nums)
#         total_sub=1<<n
#         result=[]
#         for num in range(total_sub):
#             lst=[]
#             for i in range(n):
#                 if num & (1 << i):
#                     lst.append(nums[i])
#             result.append(lst)
#         return result

# # solution - 2 TC:O(2^N) SC:O(N+1) =~ SC:O(N) Stack Space
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = self.solve(0, nums, [], [])
        return result

    def solve(self, ind, nums, subset, result):
        if ind >= len(nums):
            result.append(subset.copy())
            return
        subset.append(nums[ind])
        self.solve(ind + 1, nums, subset, result)
        subset.pop()
        self.solve(ind + 1, nums, subset, result)
        return result
