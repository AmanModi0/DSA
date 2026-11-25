# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head.next:
            return head
        n = 1
        temp1 = head
        arr = []
        while temp1:
            arr.append(temp1.val)
            temp1 = temp1.next
        n = len(arr) - (len(arr) % k)
        for i in range(0, n, k):
            arr[i : i + k] = reversed(arr[i : i + k])

        head2 = ListNode()
        temp2 = head2
        for i in arr:
            newNode = ListNode(i)
            temp2.next = newNode
            temp2 = temp2.next
        head2 = head2.next
        return head2
