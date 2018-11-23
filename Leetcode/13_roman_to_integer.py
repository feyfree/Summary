class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_rome = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        initial = 0
        str_len = len(s)
        for i in range(str_len - 1):
            value_f = num_rome[s[i]]
            value_b = num_rome[s[i + 1]]
            if value_f < value_b:
                initial -= value_f
            else:
                initial += value_f
        initial += num_rome[s[-1]]

        return initial