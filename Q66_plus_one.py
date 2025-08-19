class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # # solution - 2 TC:O(N) SC:O(1)
        if len(digits) == 0:
            return []
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

        # # solution - 1 TC:O(2N) SC:O(1)
        # if len(digits)==0:
        #     return []
        # num=0
        # for i in digits:
        #     num=num*10+i
        # num+=1
        # ans=[]
        # while num>0:
        #     n=num%10
        #     num=num//10
        #     ans.append(n)
        # ans.reverse()
        # return ans
