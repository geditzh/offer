#!/usr/bin/python3
# -*- coding:utf-8 -*-

__author__ = "Zhang Han"

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        m, n = len(array), len(array[0])
        i, j = 0, n-1
        if m == 0 or n == 0:
            return False
        while i < m and j >= 0:
            if array[i][j] > target:
                j -= 1
            elif array[i][j] < target:
                i += 1
            else:
                return True
        return False

