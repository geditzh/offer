# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        queue = []
        queue.insert(0, root)
        lst = []
        while queue:
            p = queue.pop()
            lst.append(p.val)
            if p.left is not None:
                queue.insert(0, p.left)
            if p.right is not None:
                queue.insert(0, p.right)
        return lst
