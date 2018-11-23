class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        share_start = ""
        if len(strs) > 1:
            for j in range(len(strs[0])):
                a = strs[0][j]
                flag = 1
                length = len(strs)
                for i in range(1, length):
                    if j < len(strs[i]):
                        if strs[i][j] == a:
                            flag = 1
                        else:
                            flag = 0
                            break
                    else:
                        flag = 0
                        break
                if flag == 1:
                    share_start = share_start + a
                else:
                    break
            return share_start

        else:
            if len(strs) == 0:
                return share_start
            else:
                return str(strs[0])
