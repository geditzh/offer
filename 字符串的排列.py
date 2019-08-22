'''
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''

class Solution1:
    def __init__(self):
        self.lst = []

    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        if len(ss)==1:
            return list(ss)
        charlist = list(ss)
        self.permutation(charlist, 0)
        self.lst.sort()
        return self.lst

    def permutation(self, ss, begin):
        if begin == len(ss)-1:
            self.lst.append(''.join(ss))
        else:
            for i in range(begin, len(ss)):
                if ss[i] == ss[begin] and i != begin:
                    continue
                else:
                    ss[begin], ss[i] = ss[i], ss[begin]
                    self.permutation(ss, begin+1)
                    ss[begin], ss[i] = ss[i], ss[begin]

s = Solution1()
print(s.Permutation('aa'))
