# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return self.sum_(n)
    def sum0(self, n):
        return 0
    def sum_(self, n):
        func = {False:self.sum0, True:self.sum_}
        return func[not not n](n-1) + n
