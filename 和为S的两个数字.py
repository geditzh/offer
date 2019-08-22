#method1
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        dic = dict()
        lst = []
        for num in array:
            temp = tsum - num
            if num not in dic:
                dic[temp] = num
            else:
                lst.append((dic[num], num))
        if len(lst) < 1:
            return []
        res = float('INF')
        while lst:
            a, b = lst.pop()
            if a*b < res:
                res = a*b
                p, q = a, b
        return p, q

#method2
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array) < 1 or tsum <= 0:
            return []
        i, j = 0, len(array)-1
        lst = []
        while i < j:
            if array[i] + array[j] == tsum:
                lst.append((array[i], array[j]))
                i += 1
                j -= 1
            elif array[i] + array[j] < tsum:
                i += 1
            else:
                j -= 1
        res = float('inf')
        if not lst:
            return []
        a, b = 0, 0
        while lst:
            i, j = lst.pop()
            if i * j < res:
                res = i * j
                a, b = i, j
        return [a, b]
