# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        begin, end = 1, 2
        mid = (tsum+1)//2
        num = begin + end
        lst = []
        while begin < mid:
            if num == tsum:
                lst.append(list(range(begin, end+1)))
                num -= begin
                begin += 1
            elif num > tsum:
                num -= begin
                begin += 1
            else:
                end += 1
                num += end
        return lst
