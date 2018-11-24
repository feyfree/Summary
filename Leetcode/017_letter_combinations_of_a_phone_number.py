class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        look_up = {
        	'2':['a', 'b', 'c'],
        	'3':['d', 'e', 'f'],
        	'4':['g', 'h', 'i'],
        	'5':['j', 'k', 'l'],
        	'6':['m', 'n', 'o'],
        	'7':['p', 'q', 'r', 's'],
        	'8':['t', 'u', 'v'],
        	'9':['w', 'x', 'y', 'z']
        }
        res = []
        def combinations(s, digits):
        	if len(digits) == 0:
        		res.append(s)
        	else:
        		cur_digit = digits[0]
        		for char in look_up[cur_digit]:
        			combinations(s+char, digits[1:])
        if not digits or len(digits) == 0:
        	return res
        combinations('', digits)
        return res

