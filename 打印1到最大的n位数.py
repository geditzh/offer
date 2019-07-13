# -*- coding:utf-8 -*-
'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

'''
题目：打印从1到最大的n位数

题：输入数字n,按顺序打印出从1到最大的n位十进制数，比如输入3，则打印出1、2、3一直到最大的3位数999.



解题思路：需要考虑大数问题，这是题目设置的陷阱。可以把问题转换成数字排列问题，用递归让代码更简洁。 参见剑指offer P114

'''

class Solution:
    def Print1ToMaxOfDigits(self, n):
        if n <= 0:
            return
        num = [None] * n
        for i in range(10):
            num[0] = str(i)
            self.Print1ToMaxOfNDigitsRecursively(num, len(num), 0)

    def Print1ToMaxOfNDigitsRecursively(self, num, length, index):
        if index == length - 1:
            self.PrintNumber(num)
        else:
            for i in range(10):
                num[index+1] = str(i)
                self.Print1ToMaxOfNDigitsRecursively(num, len(num), index+1)

    def PrintNumber(self, num):
        is_begin_0 = True
        for i in range(len(num)):
            if is_begin_0 and num[i] != '0':
                print(num[i], end='')
                is_begin_0 = False
                continue
            if not is_begin_0:
                print(num[i], end='')
        if not is_begin_0:
            print('')

s = Solution()
s.Print1ToMaxOfDigits(3)
