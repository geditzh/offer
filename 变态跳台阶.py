'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
F(n) = F(n-1) + F(n-2) + ... + F(1) + 1
'''

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            lst = [1,2]
            for i in range(2, number):
                lst.append(sum(lst)+1)
        return lst[-1]
