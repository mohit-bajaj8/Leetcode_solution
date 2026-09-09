class Solution:
    def removeStars(self, s: str) -> str:
        # TC:O(2N) ~ O(N)  SC:O(N)
        stack = []
        for i in s:
            if not stack or (i != '*'):
                stack.append(i)
            else:
                stack.pop()
        return "".join(stack)