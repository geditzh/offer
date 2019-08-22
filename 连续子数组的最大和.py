    '''
    题：输入一个整形数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为O（n）

解题思路：在数组里从前向后遍历，记录下每次的“当前累加子数组和”和“当前的最大子数组和”（其本身包含“动态规划”的思想，详见剑指offer P220）
    '''


    class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        max_sum = float('-inf')
        count = 0
        for num in array:
            if num + count < num:
                count = 0
            if count + num > max_sum:
                max_sum = count + num
            count += num
        return max_sum

    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        max_sum = float('-inf')
        count = 0
        for num in array:
            if count < 0:
                count = num
            else:
                count += num
            if count > max_sum:
                max_sum = count
        return max_sum
