# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if len(array) < 2:
            return
        resEOR = 0
        for i in array:
            resEOR ^= i
        index = self.FindFirstBit(resEOR)
        res1, res2 = 0, 0
        for i in array:
            if self.IsBit(i, index):
                res1 ^= i
            else:
                res2 ^= i
        return [res1, res2]

    def FindFirstBit(self, num):
        count = 0
        while num&1 == 0 and count < 32:
            num = num >> 1
            count += 1
        return count

    def IsBit(self, num, count):
        num = num >> count
        return num & 1
