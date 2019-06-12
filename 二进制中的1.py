'''
最佳方法：把一个整数减去1，再和原整数做“与运算”，
会把该整数最右边的1变成0。那么一个整数的二进制中表示中有多少个1，就可以进行多少次这样的操作。
在python中,负数是源码加-号表示的,要想表示成补码的形式,就需要和0xFFFFFFFF相与
'''
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xFFFFFFFF
        while n:
            count += 1
            n = n & (n - 1)
        return count
