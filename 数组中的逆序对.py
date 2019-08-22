'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P
'''

#method 1
class Solution:
    def InversePairs(self, data):
        # write code here
        if len(data) <= 1:
            return 0
        copy = data[:]
        copy.sort()
        count = 0
        for i in range(len(copy)):
            count += data.index(copy[i])
            data.remove(copy[i])
        return count

#method2
# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if len(data) <= 1:
            return 0
        copy = data[:]
        count = self.Core(data, copy, 0, len(data)-1)
        return count

    def Core(self, data, copy, begin, end):
        if begin >= end:
            return 0
        length = (end - begin) // 2
        left = self.Core(copy, data, begin, begin+length)
        right = self.Core(copy, data, begin+length+1, end)
        i = begin+length
        j = end
        k = end
        count = 0
        while i >= begin and j >= begin+length+1:
            if data[i] > data[j]:
                copy[k] = data[i]
                count += j-begin-length
                i -= 1
            else:
                copy[k] = data[j]
                j -= 1
            k -= 1
        while i >= begin:
            copy[k] = data[i]
            k -= 1
            i -= 1
        while j >= begin+length+1:
            copy[k] = data[j]
            k -= 1
            j -= 1
        return count + left + right
