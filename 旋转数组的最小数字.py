# -*- coding:utf-8 -*-
'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if rotateArray == []:
            return 0
        index1 = 0
        index2 = len(rotateArray) - 1
        index_mid = 0
        while index2 > index1:
            if (index2-index1) == 1:
                return rotateArray[index2]
            index_mid = (index1+index2)//2
            if rotateArray[index1] == rotateArray[index2] and rotateArray[index2] == rotateArray[index_mid]:
                index_mid = self.find_min(rotateArray, index1, index2)
                return index_mid
            if rotateArray[index1] <= rotateArray[index_mid]:
                index1 = index_mid
            if rotateArray[index2] >= rotateArray[index_mid]:
                index2 = index_mid

    def find_min(self, rotateArray, index1, index2):
        res=rotateArray[index1]
        for i in range(index1+1,index2+1):
            if res>rotateArray[i]:
                res=rotateArray[i]
        return res
