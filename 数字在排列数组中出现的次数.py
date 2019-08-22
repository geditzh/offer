# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        length = len(data)
        num = 0
        first = self.get_first(data, length, k, 0, length-1)
        last = self.get_last(data, length, k, 0, length-1)
        if first > -1 and last > -1:
            num = last - first + 1
        return num

    def get_first(self, data, length, k, begin, end):
        if begin > end:
            return -1
        mid = (begin+end)//2
        if data[mid] == k:
            if (mid > 0 and data[mid-1] != k) or mid == 0:
                return mid
            else:
                end = mid - 1
        elif data[mid] > k:
            end = mid - 1
        else:
            begin = mid + 1
        return self.get_first(data, length, k, begin, end)

    def get_last(self, data, length, k, begin, end):
        if begin > end:
            return -1
        mid = (begin+end)//2
        if data[mid] == k:
            if (mid < length-1 and data[mid+1] != k) or mid == length-1:
                return mid
            else:
                begin = mid + 1
        elif data[mid] > k:
            end = mid - 1
        else:
            begin = mid + 1
        return self.get_last(data, length, k, begin, end)
