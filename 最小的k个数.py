# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, numbers, k):
        # write code here
        if not numbers:
            return 0
        if k > len(numbers):
            return []
        start = 0
        end = len(numbers)-1
        index = self.partition(numbers, start, end)
        while index != k-1:
            if index < k-1:
                start = index + 1
                index = self.partition(numbers, start, end)
            else:
                end = index - 1
                index = self.partition(numbers, start, end)
        out = numbers[:k]
        return sorted(out)

    def partition(self, numbers, start, end):
        dummy = numbers[start]
        i = start
        j = end
        while i < j:
            while numbers[j]>dummy and j>i:
                j -= 1
            if j > i:
                numbers[i] = numbers[j]
                i += 1
            while numbers[i]<dummy and i<j:
                i += 1
            if i < j:
                numbers[j] = numbers[i]
                j -= 1
        numbers[i] = dummy
        return i

s = Solution()
print(s.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8], 4))
