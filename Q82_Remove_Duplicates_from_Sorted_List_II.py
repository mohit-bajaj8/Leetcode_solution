# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # # solution - 2: TC:O(N) SC:O(1)
        if not head or not head.next:
            return head
        cur = head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next

        # # solution - 1: TC:O(2N) SC:O(N)
        # if not head:
        #     return None
        # temp=head
        # mydict=dict()
        # while temp:
        #     mydict[temp.val]=mydict.get(temp.val,0)+1
        #     temp=temp.next
        # head=None
        # prev=None
        # for key in mydict:
        #     if mydict[key]==1:
        #         node=ListNode(key)
        #         if head==None:
        #             head=node
        #         else:
        #             prev.next=node
        #         prev=node
        # return head