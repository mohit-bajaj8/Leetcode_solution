class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # solution - 2 TC:O(N/2) SC:O(1)
        if head==None or head.next==None:
            return head
        evenhead=head.next
        odd=head
        even=head.next
        while even and even.next:
            odd.next=odd.next.next
            odd=odd.next
            even.next=even.next.next
            even=even.next
        odd.next=evenhead
        return head

        # # solution 1 - TC:O(N) SC:O(N)
        # if head==None or head.next==None
        #    return head
        # temp=head
        # evenlist=[]
        # oddlist=[]
        # check=True
        # while temp:
        #     if check:
        #         oddlist.append(temp)
        #         check= not check
        #     else:
        #         evenlist.append(temp)
        #         check=(not check)
        #     temp = temp.next
        # head=oddlist[0]
        # temp=head
        # for i in range(1,len(oddlist)):
        #     temp.next=oddlist[i]
        #     temp=temp.next
        # for i in range(len(evenlist)):
        #     temp.next=evenlist[i]
        #     temp=temp.next
        # temp.next=None
        # return head
