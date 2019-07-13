'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        g_InvalidInput = False
        if base == 0.0 and exponent < 0:
            g_InvalidInput = True
            return 0.0
        if exponent < 0:
            exponent = -exponent
        res = self.PowerWithUnsignedExponent(base, exponent)
        if exponent < 0:
            return 1.0 / res
        else:
            return res

    # def PowerWithUnsignedExponent(self, base, exponent):
    #     res = 1
    #     for i in range(exponent):
    #         res *= base
    #     return res

    def PowerWithUnsignedExponent(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        res = self.PowerWithUnsignedExponent(base, exponent>>1)
        result = res * res
        if exponent & 1:        #位与运算符比乘除法和求余数效率要高很多.
            result *= base
        return result


s = Solution()
print(s.Power(2,3))
