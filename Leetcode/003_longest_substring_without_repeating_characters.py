class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

     

        #1.建立字典，存入键值对
        tempDict = {}
        #2.初始化
        max1 = 0
        pointer = 0
        for index, value in enumerate(s):
            #3.如果值在字典中
            if value in tempDict:
                #4.pointer是这一轮未重复字符串的index
                pointer = max(tempDict[value] + 1, pointer)
            max1 = max(index - pointer + 1, max1)
            tempDict[value] = index
        return max1