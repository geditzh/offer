# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        numbers.sort()
        num_zero = 0
        for num in numbers:
            if num > 0:
                break
            num_zero += 1
        gap = 0
        for i in range(len(numbers)-1):
            if numbers[i] == 0:
                continue
            if numbers[i] == numbers[i+1]:
                return False
            if numbers[i+1] - numbers[i] > 1:
                gap += numbers[i+1] - numbers[i] - 1

        if num_zero >= gap:
            return True
        return False
