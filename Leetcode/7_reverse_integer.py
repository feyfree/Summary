class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_abs = abs(x)
        if x >= 2 ** 31 - 1 or x <= -2 ** 31:
            return 0
        else:
            if x >= 0:
                j = int(str(x)[::-1])
                if j >= 2 ** 31 - 1 or j <= -2 ** 31:
                    return 0
                else:
                    return j
            else:
                j = 0 - int(str(x_abs)[::-1])
                if j >= 2 ** 31 - 1 or j <= -2 ** 31:
                    return 0
                else:
                    return j
