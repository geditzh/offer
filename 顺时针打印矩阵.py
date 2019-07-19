# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        size = len(matrix)
        if size == 0:
            return
        if size == 1:
            print(matrix[0])
        times = 0
        for i in range(size//2):
            for j in range(i, size-times):
                print(matrix[i][j], end=',')
            for k in range(i+1, size-times):
                print(matrix[k][j], end=',')
            for j in range(size-times-2, -1+i, -1):
                print(matrix[k][j], end=',')
            for k in range(size-times-2, i, -1):
                print(matrix[k][j], end=',')
            times += 1


matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
s = Solution()
s.printMatrix(matrix)
