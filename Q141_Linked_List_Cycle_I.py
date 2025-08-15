class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # # solution 2
        # # TC:O(N) SC:O(1)
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

        # # solution 1
        # # TC: O(N) , SC: O(N)
        # temp=head
        # myset=set()
        # while temp:
        #     if temp in myset:
        #         return True
        #     myset.add(temp)
        #     temp=temp.next
        # return False
