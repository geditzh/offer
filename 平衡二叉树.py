# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        left = self.get_length(pRoot.left)
        right = self.get_length(pRoot.right)
        diff = left - right
        if diff > 1 or diff < -1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def get_length(self, pRoot):
        if not pRoot:
            return 0
        left = self.get_length(pRoot.left)
        right = self.get_length(pRoot.right)
        return max(left, right) + 1
