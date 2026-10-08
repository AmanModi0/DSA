# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head
        temp = head
        l = ListNode(temp.val)
        h = l
        while temp.next:
            temp = temp.next
            newNode = ListNode(temp.val)
            newNode.next = h
            h = newNode
        return h
