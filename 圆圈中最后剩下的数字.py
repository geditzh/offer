class LNode(object):
    def __init__(self, val, _next):
        self.val = val
        self.next = _next
        self.visited = 0

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1
        root = None
        for i in range(n-1,-1,-1):
            root = LNode(i, root)
        p = root
        while p.next is not None:
            p = p.next
        p.next  = root
        times = 0
        while times < n-1:
            sub_times = 0
            while sub_times < m:
                if root.visited == 0:
                    sub_times += 1
                if sub_times < m:
                    root = root.next
            root.visited = 1
            times += 1
        while root.visited != 0:
            root = root.next
        return root.val
