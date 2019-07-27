'''
题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点）
，返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''

######解法1
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return None
        dic = dict()
        pCloneNode = pCloneHead = RandomListNode(pHead.label)
        dic[pHead] = pCloneHead
        p = pHead.next
        while p is not None:
            pCloneNode.next = RandomListNode(p.label)
            dic[p] = pCloneNode.next
            p = p.next
            pCloneNode = pCloneNode.next
        p = pHead
        pCloneNode = pCloneHead
        while p is not None:
            if p.random is not None:
                pCloneNode.random = dic[p.random]
            p = p.next
            pCloneNode = pCloneNode.next
        return pCloneHead

######解法2
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead == None:
            return None
        self.CloneNodes(pHead)
        self.ConnectRandomNodes(pHead)
        return self.ReconnectNodes(pHead)

    def CloneNodes(self, pHead):
        p = pHead
        while p is not None:
            pclone = RandomListNode(0)
            pclone.label = p.label
            pclone.next = p.next
            p.next = pclone
            p = pclone.next

    def ConnectRandomNodes(self, pHead):
        p = pHead
        while p is not None:
            pclone = p.next
            if p.random is not None:
                pclone.random = p.random.next
            p = pclone.next

    def ReconnectNodes(self, pHead):
        p = pHead
        pcloneHead = pclone = p.next
        p.next = pclone.next
        p = p.next
        while p is not None:
            pclone.next = p.next
            pclone = pclone.next
            p.next = pclone.next
            p = p.next
        return pcloneHead


