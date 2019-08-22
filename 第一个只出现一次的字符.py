#method 1
from collections import Counter
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        dic = Counter(s)
        index = float('inf')
        for i, val in dic.items():
            if val == 1:
                if s.index(i) < index:
                    index = s.index(i)
        if index == float('inf'):
            return -1
        else:
            return index

#method 2
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s)<=0:
            return -1

        char_dict={}
        for i in s:
            if i in char_dict:
                char_dict[i]+=1
            else:
                char_dict[i]=1
        for index,value in enumerate(s):
            if char_dict[value]==1:
                return index
        return -1
