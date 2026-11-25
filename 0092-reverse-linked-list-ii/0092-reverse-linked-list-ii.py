# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: ListNode | None, left: int, right: int
    ) -> ListNode | None:

        if not head.next:
            return head
        l = 1
        head2 = ListNode()
        temp2 = head2
        temp1 = head

        while temp1 and l < left:
            newNode = ListNode(temp1.val)
            temp2.next = newNode
            temp2 = temp2.next
            temp1 = temp1.next
            l += 1

        while temp1 and l <= right:
            newNode = ListNode(temp1.val)
            if temp2.next:
                newNode.next = temp2.next
            temp2.next = newNode
            temp1 = temp1.next
            l += 1

        while temp2.next:
            temp2 = temp2.next

        while temp1:
            newNode = ListNode(temp1.val)
            temp2.next = newNode
            temp2 = temp2.next
            temp1 = temp1.next

        head2 = head2.next
        return head2