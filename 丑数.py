'''
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''

#method 1
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        count = 0
        countNumber = 0
        while countNumber < index:
            count += 1
            if self.isUgly(count):
                countNumber += 1
        return count

    def isUgly(self, number):
        while number%2 == 0:
            number /= 2
        while number%3 == 0:
            number /= 3
        while number%5 == 0:
            number /= 5
        if number == 1:
            return True
        return False

#method 2
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        res = [1]
        t2 = t3 = t5 = 0
        count = 1
        while count < index:
            min_val = min(res[t2]*2, res[t3]*3, res[t5]*5)
            res.append(min_val)
            while res[t2]*2 <= min_val:
                t2 += 1
            while res[t3]*3 <= min_val:
                t3 += 1
            while res[t5]*5 <= min_val:
                t5 += 1
            count += 1
        return res[-1]

