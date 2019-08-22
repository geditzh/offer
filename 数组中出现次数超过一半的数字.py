'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''
#解法一
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        middle = len(numbers) // 2
        start = 0
        end = len(numbers)-1
        index = self.partition(numbers, start, end)
        while index != middle:
            if index < middle:
                start = index + 1
                index = self.partition(numbers, start, end)
            else:
                end = index - 1
                index = self.partition(numbers, start, end)
        times = 0
        for num in numbers:
            if num == numbers[middle]:
                times += 1
        if times > len(numbers)//2:
            return numbers[middle]
        else:
            return 0

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

#解法二
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        res = numbers[0]
        times = 1
        for i in range(1, len(numbers)):
            if times == 0:
                res = numbers[i]
                times = 1
            elif numbers[i] == res:
                times += 1
            else:
                times -= 1
        count = 0
        for num in numbers:
            if num == res:
                count += 1
        if count > len(numbers)//2:
            return res
        else:
            return 0
