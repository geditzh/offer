#!/usr/bin/python3
# -*- coding:utf-8 -*-

__author__ = "Zhang Han"

class Solution:
    # array 二维列表
    def replaceSpace(self, s):
        count = 0
        for i in s:
            if i == ' ':
                count += 1

        p1 = len(s)-1
        a = [0]*(len(s)+count*2)
        p2 = len(a)-1
        while p2 >=0:
            if s[p1] == ' ':
                for j in ['0', '2', '%']:
                    a[p2] = j
                    p2 -= 1
            else:
                a[p2] = s[p1]
                p2 -=1
            p1 -= 1
        return ''.join(a)

so = Solution()
s = 'zha han zha'
print(so.replaceSpace(s))
