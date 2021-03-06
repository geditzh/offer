class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode is None:
            return []
        res = []
        while listNode is not None:
            res.append(listNode.val)
            listNode = listNode.next
        return res[::-1]
