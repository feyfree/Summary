class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp_str = str(x)
        temp_len = len(temp_str)
        flag = 1
        for i in range(temp_len):
            if temp_str[i]==temp_str[temp_len-i-1]:
                flag = flag
            else:
                flag = 0
                break
        if flag==1:
            return True
        else:
            return False