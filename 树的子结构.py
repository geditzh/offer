'''
题目：树的子结构

题：输入两棵二叉树A和B，判断B是不是A的子结构。

解题思路：递归，注意空指针的情况。
'''

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        res = False
        if not pRoot1 or not pRoot2:
            return False
        if pRoot1.val == pRoot2.val:
            res = self.Tree1HasTree2(pRoot1, pRoot2)
        if not res:
            res = self.HasSubtree(pRoot1.left, pRoot2)
        if not res:
            res = self.HasSubtree(pRoot1.right, pRoot2)
        return res

    def Tree1HasTree2(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.Tree1HasTree2(pRoot1.left, pRoot2.left) and self.Tree1HasTree2(pRoot1.right, pRoot2.right)
