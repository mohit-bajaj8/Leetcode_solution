class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # solution - 2 TC:O(N) SC:O(1)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

        # # solution - 1 TC:O(N) SC:O(N)
        # temp=head
        # myset=set()
        # while temp:
        #     if temp in myset:
        #         return temp
        #     myset.add(temp)
        #     temp=temp.next
        # return None