class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        pos = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:pos+1], tin[:pos])
        root.right = self.reConstructBinaryTree(pre[pos+1:] ,tin[pos+1:])
        return root
iii
