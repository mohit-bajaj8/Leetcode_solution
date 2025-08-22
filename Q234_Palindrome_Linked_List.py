# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # # solution - 2 TC:O(N) SC:O(1)
        if not head or not head.next:
            return True
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = self.reverseList(slow)
        start = head
        while mid:
            if start.val != mid.val:
                return False
            start = start.next
            mid = mid.next
        return True

    def reverseList(self, head):
        temp = head
        prev = None
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

    # # solution - 1 TC:O(2N) SC:O(N)
    # if not head or not head.next:
    #     return True
    # arr=[]
    # temp=head
    # while temp:
    #     arr.append(temp.val)
    #     temp=temp.next
    # left=0
    # right=len(arr)-1
    # while left<=right:
    #     if arr[left]!=arr[right]:
    #         return False
    #     left+=1
    #     right-=1
    # return True