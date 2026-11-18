# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        temp = head
        while temp and temp.next:
            newNode = ListNode(math.gcd(temp.val, temp.next.val))
            newNode.next = temp.next
            temp.next = newNode
            temp = temp.next.next
        return head