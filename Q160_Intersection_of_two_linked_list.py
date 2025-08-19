class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        p1, p2 = headA, headB

        # Traverse both lists
        while p1 != p2:
            # If a pointer reaches the end, redirect to the other list's head
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA

        return p1