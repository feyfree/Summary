class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strset = {}
        for i in range(len(strs)):
            target = "".join(sorted(strs[i]))
            if target not in strset:
                strset[target] = [strs[i]]
            else:
                strset[target].append(strs[i])
        result = []
        for values in strset.values():
            result += [values]
        return result
