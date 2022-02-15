# problem : https://leetcode.com/problems/single-number/
# time complexity : O(N)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y:x^y, nums)
        
