class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n == 1:
            return 1
        num = 0
        for i in range(1, n+1):
            num += self.count_number(i)
        return num

    def count_number(self, n):
        count = 0
        while n:
            if n % 10 == 1:
                count += 1
            n = n//10
        return count
`
