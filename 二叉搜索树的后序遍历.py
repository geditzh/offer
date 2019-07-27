class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            print ('False')
        root = sequence[-1]
        i = 0
        while i < len(sequence)-1:
            if sequence[i] > root:
                break
            i += 1
        j = i
        while j < len(sequence)-1：
            if sequence[i] < root:
                print ('False')
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if i < len(sequence)-1:
            right = self.VerifySquenceOfBST(sequence[i:len(sequence)]
        if left and right:
            print 'True'

s = Solution()
s.VerifySquenceOfBST([7,4,6,5])

