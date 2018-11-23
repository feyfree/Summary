class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def helper(res, l, r, n, max):
            if n == max:
                res.append(l)
            for i in range(0, len(r)):
                helper(res, l+[r[i]], r[:i]+r[i+1:], n+1, max)
        helper(res, [], nums, 0, len(nums))
        return res

# class Solution(object):
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         if len(nums) <= 1:
#             return [nums]
#         ans = []
#         for i, num in enumerate(nums):
#             n = nums[:i] + nums[i+1:]
#             for temp_list in self.permute(n):
#                 ans.append([num] + temp_list)
#         return ans

s = Solution()
print(s.permute([1,2,3]))