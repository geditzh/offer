'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等
。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）
如果第一个序列的值和第二个序列的第一值不相等,则压入栈中.
'''
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        while popV:
            while not stack or stack[-1] != popV[0]:
                if not pushV:
                    return False
                stack.append(pushV.pop(0))
            popV.pop(0)
            stack.pop()
        if not stack and not popV:
            return True
        return False
