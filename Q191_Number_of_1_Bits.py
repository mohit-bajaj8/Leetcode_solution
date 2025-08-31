# # Optimal Solution
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         # # TC : O(32)
#         count=0
#         for i in range(32):
#             if n & (1<<i)!=0:
#                 count+=1
#         return count