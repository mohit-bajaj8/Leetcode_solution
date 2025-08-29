class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # # solution - 2 TC:O(N) SC:O(1)
        ans = 0
        for i in nums:
            ans = ans ^ i
        return ans
        # # solution - 1 TC:O(N) SC:O(n/2 + 1)
        # mydict=dict()
        # for i in nums:
        #     mydict[i]=mydict.get(i,0)+1
        # for i in mydict:
        #     if mydict[i]==1:
        #         return i

