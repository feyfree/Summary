class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mark = ["()", "[]", "{}"]
        stack = []
        for i in range(0, len(s)):
            stack.append(s[i])
            if len(stack) >= 2 and (stack[-2] + stack[-1]) in mark:
                stack.pop()
                stack.pop()

        return len(stack) == 0

