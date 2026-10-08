# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        head1 = list1
        head2 = list2
        list3 = ListNode()
        head3 = list3
        temp = head3
        while head1 and head2:
            newNode = ListNode()
            if head1.val <= head2.val:
                newNode.val = head1.val
                head1 = head1.next
            else:
                newNode.val = head2.val
                head2 = head2.next
            temp.next = newNode
            temp = temp.next
        while head1:
            newNode = ListNode(head1.val)
            head1 = head1.next
            temp.next = newNode
            temp = temp.next
        while head2:
            newNode = ListNode(head2.val)
            head2 = head2.next
            temp.next = newNode
            temp = temp.next
        head3 = head3.next
        return head3
