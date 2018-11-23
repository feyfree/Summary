class Solution(object):
    def reverseStr(self, s, k):
        res = ''
        i = 0
        while i < len(s):
            res = res + s[i:i+k][::-1]
            res = res + s[i+k:i+(k*2)]
            i = i + (k * 2)
        return res
