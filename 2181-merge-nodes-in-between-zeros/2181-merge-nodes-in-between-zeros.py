# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        temp1 = head.next
        head2 = ListNode()
        temp2 = head2
        add = 0
        while temp1:
            if temp1.val == 0:
                newNode = ListNode(add)
                temp2.next = newNode
                temp2 = temp2.next
                add = 0
            else:
                add += temp1.val
            temp1 = temp1.next
        head2 = head2.next
        return head2