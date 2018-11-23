class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def change(nums):
            """
            :type nums: str
            :rtype :str
            """
            sum = 0
            for i in range(len(nums)):
                sum += 10**(len(nums)-i-1)*(ord(nums[i])-ord('0'))
            return sum

        if num1 == "0" or num2 == "0":
            return "0"
        else:
            return str(change(num1) * change(num2))