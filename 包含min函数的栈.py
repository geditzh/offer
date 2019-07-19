'''
题目：包含min函数的栈

题：定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。在该栈中，调用min、push、pop的时间复杂度都是O(1)

解题思路：1）如果每次压入新元素时，再调整让新元素位于栈顶，这种思路不能保证最后压入栈的元素最先出栈，因此这个数据结构已经不是栈了。X

               2）如果在栈中添加一个成员变量存放最小元素，那么当最小元素弹出后，就不知道下一个最小元素在哪儿了。因此，必须将次小元素保存。X

　　　　　3）把每次的最小元素保存起来放在另一个辅助栈里。 √
'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.data_stack = []
        self.min_stack = []
    def push(self, node):
        # write code here
        self.data_stack.append(node)
        if not self.min_stack or self.min_stack[-1] > node:
            self.min_stack.append(node)
        else:
            self.min_stack.append(self.min_stack[-1])
    def pop(self):
        # write code here
        if not self.data_stack or not self.min_stack:
            return None
        self.min_stack.pop()
        return self.data_stack.pop()

    def top(self):
        # write code here
        if not self.data_stack:
            return None
        return self.data_stack[-1]

    def min(self):
        # write code here
        if not self.min_stack:
            return None
        return self.min_stack[-1]
