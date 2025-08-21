# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # # solution - 1 by creating new linked List
        # TC:O(sum of length of both linked list) SC:O(sum of length of both linked list)
        if not list1 and not list2:
            return None
        p1 = list1
        p2 = list2
        p3 = None
        new_head = None
        while p1 and p2:
            temp = p3
            p3 = ListNode()
            if p1.val <= p2.val:
                p3.val = p1.val
                p1 = p1.next
            else:
                p3.val = p2.val
                p2 = p2.next
            if not temp:
                new_head = p3
            else:
                temp.next = p3
        if not p1:
            while p2:
                temp = p3
                p3 = ListNode(p2.val)
                p2 = p2.next
                if not temp:
                    new_head = p3
                else:
                    temp.next = p3
        else:
            while p1:
                temp = p3
                p3 = ListNode(p1.val)
                p1 = p1.next
                if not temp:
                    new_head = p3
                else:
                    temp.next = p3
        return new_head


