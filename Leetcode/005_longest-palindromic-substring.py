class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        # empty or one char
        if n < 2:
            return s

        # left index of the target substring
        l = 0
        # right index of the target substring
        r = 0
        # length of the longest palindromic substring for now
        m = 0
        # length of the current substring
        c = 0

        # Whether the substring contains the first character or last character and is palindromic
        b = True
        for i in range(n):
            # Odd situation
            for j in range(min(n-i,i+1)):
                if s[i-j] != s [i+j]:
                    b = False
                    break
                else:
                    c = 2 * j + 1

            if c > m :
                l = i - j + 1 - b
                r = i + j + b
                m = c 
            b = True

            # Even situation
            for j in range(min(n - i - 1, i + 1)):
                if (s[i - j] != s[i + j + 1]):
                    b = False
                    break
                else:
                    c = 2 * j + 2
            if (c > m):
                l = i - j + 1 - b
                r = i + j + 1 + b
                m = c
            b = True
        return s[l:r]