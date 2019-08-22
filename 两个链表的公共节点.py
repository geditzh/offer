# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        length1 = self.GetLength(pHead1)
        length2 = self.GetLength(pHead2)
        if length1 > length2:
            lengthlong = pHead1
            lengthshort = pHead2
        else:
            lengthlong = pHead2
            lengthshort = pHead1
        lengthdiff = abs(length1 - length2)
        for i in range(lengthdiff):
            lengthlong = lengthlong.next
        while lengthlong is not None and lengthshort is not None and lengthlong != lengthshort:
            lengthlong = lengthlong.next
            lengthshort = lengthshort.next
        return lengthlong

    def GetLength(self, pHead):
        p = pHead
        count = 0
        while p is not None:
            count += 1
            p = p.next
        return count
