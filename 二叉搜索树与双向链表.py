'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''

#####解法1
class Solution:
    def __init__(self):
        self.lst = []

    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return
        p = pRootOfTree
        stack = []
        while stack or p is not None:
            while p is not None:
                stack.append(p)
                p = p.left
            p = stack.pop()
            self.lst.append(p)
            p = p.right
        for i, v in enumerate(self.lst[:-1]):
            self.lst[i].right = self.lst[i+1]
            self.lst[i+1].left = self.lst[i]
        return self.lst[0]


###解法2
class Solution:
    def __init__(self):
        self.list_end = None

    def Convert(self, pRootOfTree):
        # write code here
        root = pRootOfTree
        if not pRootOfTree:
            return
        while root.left is not None:
            root = root.left
        self.ConvertNode(pRootOfTree)
        return root

    def ConvertNode(self, pRootOfTree):
        if not pRootOfTree:
            return
        p = pRootOfTree
        if p.left is not None:
            self.ConvertNode(p.left)
        p.left = self.list_end
        if self.list_end is not None:
            self.list_end.right = p
        self.list_end = p
        if p.right is not None:
            self.ConvertNode(p.right)
