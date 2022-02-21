# problem : https://leetcode.com/problems/majority-element/
# time complexity : O(N)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cnts = {}
        for num in nums:
            cnts[num] = cnts.get(num, 0) + 1
            if cnts[num] > n/2:
                return num
        return 0
        
