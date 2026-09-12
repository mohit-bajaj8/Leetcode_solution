class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        # TC:O(M+N) SC:O(M+N)

        s1 = []
        s2 = []
        for i in s:
            if i == '#' and s1:
                s1.pop()
            else:
                if i != '#':
                    s1.append(i)

        for i in t:
            if i == '#' and s2:
                s2.pop()
            else:
                if i != '#':
                    s2.append(i)

        return ("".join(s1) == "".join(s2))

