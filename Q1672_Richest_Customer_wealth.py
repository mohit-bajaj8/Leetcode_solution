class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        row = len(accounts)
        richest = 0
        for r in range(0,row):
            wealth = sum(accounts[r])
            if wealth > richest:
                richest = wealth
        return richest