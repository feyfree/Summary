# class Solution:
#     def sortColors(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         red = nums.count(0)
#         white = nums.count(1)
#         blue = nums.count(2)
#         for i in range(0, red):
#             nums[i] = 0
#         for i in range(red, red+white):
#             nums[i] = 1
#         for i in range(red+white, red+blue+white):
#             nums[i] = 2

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        k = len(nums)-1
        j = i
        while j <= k:
            if i < j and nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            elif nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1

# solution two realized the sort nums[:i] equals 0, and nums[k+1:] equals 2