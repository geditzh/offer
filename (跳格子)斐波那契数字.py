'''一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
F(n) = F(n-1) + F(n-2)
'''
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n<=0:
            return 0
        elif n==1:
            return 1
#        return self.Fibonacci(n-1) + self.Fibonacci(n-2)
        first = 0
        second = 1
        while n > 1:
            first, second = second, first + second
            n -= 1
        return second
