class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        list1 = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX",
                 "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC",
                 "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM",
                 "M", "MM", "MMM"]
        str1 = [0] * 4
        str2 = ''
        i = 3
        while num > 0:
            str1[i] = num % 10
            num = num // 10
            i -= 1
        for i in range(4):
            if str1[i] != 0:
                str2 = str2 + (list1[9 * (3 - i) + str1[i] - 1])
        return str2.replace("0", '')
