class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        '''
        分为两种情况，取candidates的某一位，然后target-candidates[index],继续
        另外就是不取继续，结束条件index > len(candidates),一直减下去，为负数
        '''

        def helper(remain, combination, index):cs
            if remain < 0:
                return
            if remain == 0:
                res.append(combination)
                return
            if index >= len(candidates):
                return
            helper(remain, combination, index + 1)
            helper(remain - candidates[index], combination + [candidates[index]], index)

        res = []
        helper(target, [], 0)
        return res
