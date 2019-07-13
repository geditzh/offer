'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''
class Solution:
    def reOrderArray(self, array):
        # write code here
        if not array:
            return
        i, j = 0, len(array) - 1
        while i < j:
            while i < j and (array[i] & 0x1 != 0):
                i += 1
            while i < j and (array[j] & 0x1 == 0):
                j -= 1
            if i < j:
                array[i], array[j] = array[j], array[i]
        return array


s = Solution()
s.reOrderArray([1,2,6,4,2,56,7,987,654,32,345,676,5432])
