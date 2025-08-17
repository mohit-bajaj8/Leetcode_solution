class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # TC:O(1) SC:O(1)
        node.val = node.next.val
        node.next = node.next.next
