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

        carry = 0
        ans = []
        n = min(len(arr1), len(arr2))
        arr1.reverse()
        arr2.reverse()
        for i in range(n):
            temp = arr1[i] + arr2[i] + carry
            if temp >= 10:
                temp -= 10
                carry = 1
            else:
                carry = 0
            ans.append(temp)
        while len(arr1) > n:
            arr1[n] += carry
            if arr1[n] >= 10:
                arr1[n] -= 10
                carry = 1
            else:
                carry = 0
            ans.append(arr1[n])
            n += 1
        while len(arr2) > n:
            arr2[n] += carry
            if arr2[n] >= 10:
                arr2[n] -= 10
                carry = 1
            else:
                carry = 0
            ans.append(arr2[n])
            n += 1
        if carry == 1:
            ans.append(carry)
        ans.reverse()
        l3 = ListNode(ans[0])
        head = l3
        for i in ans[1:]:
            a = ListNode(i)
            head.next = a
            head = a
        return l3
