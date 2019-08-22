class Solution:
    def StrToInt(self, s):
        # write code here
        lst  = list(map(str, list(range(10))))
        sum = 0
        label = 1
        for i in range(len(s)):
            if i == 0:
                if s[i] == '+':
                    label = 1
                    continue
                elif s[i] == '-':
                    label = -1
                    continue
            if s[i] in lst:
                sum = 10*sum + lst.index(s[i])
            else:
                sum = 0
                break
        return label * sum
