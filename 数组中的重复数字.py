#!/usr/bin/python3
# -*- coding:utf-8 -*-

__author__ = "Zhang Han"

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        text = set()
        for number in numbers:
            if number not in text:
                text.add(number)
            else:
                duplication[0] = number
                return True
        return False

