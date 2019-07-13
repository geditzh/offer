'''
题目：链表中倒数第k个节点

题：输入一个链表，输出该链表中倒数第k个结点。


解题思路：为了实现只遍历链表一次就能找到倒数第k个节点，我们可以定义两个指针。让第一个指针先向前走k-1步，第二个指针保持不动；
从第k步开始，第二个指针也开始从链表的头指针开始遍历.
由于两个指针的距离保持在k-1,当第一个指针到达链表的尾节点时，第二个指针刚好到达倒数第k个节点。
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k == 0:
            return
        fast, slow = head, head
        for i in range(k-1):
            if fast.next is not None:
                fast = fast.next
            else:
                return
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        return slow

        # method two

        # if not head or k == 0:
        #     return
        # count = 0
        # p = head
        # while p is not None:
        #     count += 1
        #     p = p.next
        # p = head
        # if k > count:
        #     return
        # for i in range(count-k):
        #     p = p.next
        # return p
