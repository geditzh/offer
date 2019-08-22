'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

#方法１
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.lst = []

    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        if len(numbers) == 1:
            return numbers[0]
        numbers = list(map(str, numbers))
        self.permutation(numbers, 0)
        self.lst.sort()
        return self.lst[0]

    def permutation(self, ss, begin):
        if begin == len(ss)-1:
            self.lst.append(''.join(ss))
        else:
            for i in range(begin, len(ss)):
                if ss[i] == ss[begin] and i != begin:
                    continue
                else:
                    ss[begin], ss[i] = ss[i], ss[begin]
                    self.permutation(ss, begin+1)
                    ss[begin], ss[i] = ss[i], ss[begin]

#method 2
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        #暴力解法
        if len(numbers)<=0:
            return ""
        str_numbers=[str(i) for i in numbers]
        res=sorted(str_numbers,cmp=lambda x,y:cmp(x+y,y+x))
        return ''.join(res)
