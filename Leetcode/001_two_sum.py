class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        # 建立字典，把每一个数字对应的位置编号存入字典， key=num, value=index
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i