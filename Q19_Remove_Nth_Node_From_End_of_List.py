class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # # solution - 2: TC:O(N) SC:O(1)
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if fast == None:
            return head.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head

        # # solution - 1: TC: O(2N)  SC:O(1)
        # temp=head
        # count=0
        # while temp is not None:
        #     count+=1
        #     temp=temp.next

        # if n==count:
        #     new_head=head.next
        #     del head
        #     return new_head
        # i=1
        # temp=head
        # while i < count - n:
        #     temp=temp.next
        #     i+=1
        # temp.next=temp.next.next
        # temp=temp.next
        # del temp
        # return head
