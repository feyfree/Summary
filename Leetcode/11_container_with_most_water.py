class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return 0
        else:
            total = 0
            left, right = 0, len(height)-1
            while left <= right:
                h1 = height[left]
                h2 = height[right]
                temp = (right - left) * min(h1, h2)
                total = max(temp, total)
                if h1 > h2:
                    right -= 1
                else:
                    left += 1
            return total
