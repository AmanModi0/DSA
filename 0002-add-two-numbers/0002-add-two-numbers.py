# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        temp1 = l1
        temp2 = l2
        arr1 = []
        arr2 = []
        while temp1:
            arr1.append(temp1.val)
            temp1 = temp1.next
        while temp2:
            arr2.append(temp2.val)
            temp2 = temp2.next
        ans = list(
            map(
                int,
                str(
                    int("".join(map(str, arr1[::-1])))
                    + int("".join(map(str, arr2[::-1])))
                ),
            )
        )[::-1]

        l3 = ListNode(ans[0])
        head = l3
        for i in ans[1:]:
            a = ListNode(i)
            head.next = a
            head = a
        print(ans)
        return l3
