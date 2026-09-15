class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Optimal Solution #TC:O(M+N) SC:O(M)
        n = len(nums1)
        m = len(nums2)
        stack = []
        ans = [-1] * n
        mydict = dict()

        for i in range(m - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                # ans[i]=stack[-1]
                mydict[nums2[i]] = stack[-1]
            stack.append(nums2[i])

        for i in range(0, n):
            if nums1[i] in mydict:
                ans[i] = mydict[nums1[i]]
        return ans

        # Brute Force Solution TC:O(N ^ 2) SC:O(N)

        # n = len(nums1)
        # m = len(nums2)
        # ans = [-1] * n

        # for i in range(0,n):
        #     flag = False
        #     for j in range(0,m):
        #         if nums1[i] == nums2[j]:
        #             flag = True
        #             continue

        #         if flag:
        #             if nums2[j] > nums1[i]:
        #                 ans[i] = nums2[j]
        #                 break
        # return ans

