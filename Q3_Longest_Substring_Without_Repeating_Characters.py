class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        # Optimal solution TC:O(N) SC:O(N)

        n = len(s)
        maxi = 0
        left = 0
        right = 0
        mydict = {}

        while right < n:
            if s[right] in mydict:
                left = max(left, mydict[s[right]] + 1)
            maxi = max(maxi, right - left + 1)
            mydict[s[right]] = right
            right = right + 1

        return maxi

        # Brute Force Approach TC:O(N ^ 2) SC:O(N)
        # n = len(s)
        # maxi = 0

        # for i in range(0,n):
        #     myset = set()
        #     for j in range(i,n):
        #         if s[j] in myset:
        #             break
        #         maxi = max(maxi,j-i+1)
        #         myset.add(s[j])

        # return maxi