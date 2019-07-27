'''
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if root is None:
            return []
        stack = []
        count = 0
        res = []
        res = self.findPath(root, expectNumber, stack, count, res)
        return res

    def findPath(self, root, expectNumber, stack, count, res):
        stack.append(root.val)
        count += root.val
        if count == expectNumber and not root.left and not root.right:
            tempres = []
            for i in stack:
                tempres.append(i)
            res.append(tempres)
        if count < expectNumber:
            if root.left:
                self.findPath(root.left, expectNumber, stack, count, res)
            if root.right:
                self.findPath(root.right, expectNumber, stack, count, res)
        stack.pop()
        return res

