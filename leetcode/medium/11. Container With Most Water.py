# problem : https://leetcode.com/problems/container-with-most-water/
# time complexity : O(N)

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        answer = 0
        while left < right:
            answer = max(answer, (right-left) * min(height[right], height[left]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return answer
