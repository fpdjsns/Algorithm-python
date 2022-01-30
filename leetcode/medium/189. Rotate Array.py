/**
 * problem : https://leetcode.com/problems/rotate-array/
 * time complexity : O(N)
 */
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        tmp = k % len(nums)
        nums[:] = nums[-tmp:] + nums[:-tmp]
