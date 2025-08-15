class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # TC:O(N/2)
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
