class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # solution 1: TC: O(N^2) SC:O(1)
        # max=0
        # for i in range(len(prices)-1):
        #     profit=0
        #     for j in range(i+1,len(prices)):
        #         profit=prices[j]-prices[i]
        #         if profit>max:
        #             max=profit
        # return max

        # # solution 2: TC:O(N) SC:O(1)
        max=0
        min_pric=float("inf")
        for i in range(len(prices)):
            if prices[i]<min_pric:
                min_pric=prices[i]
            else:
                profit=prices[i]-min_pric
                if profit>max:
                    max=profit
        return max