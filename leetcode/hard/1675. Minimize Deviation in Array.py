# problem : https://leetcode.com/problems/minimize-deviation-in-array/
# time complexity : O(N * logN * logM) // N = |nums|, M = max(nums[i])

from sortedcontainers import SortedList

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        sortedNums = SortedList(list(map(lambda num: num if num%2 == 0 else 2*num, nums)))
        ans = int(1e9)
        while sortedNums[-1] % 2 == 0:
            tmp = int(sortedNums[-1]/2)
            sortedNums.pop(-1)
            sortedNums.add(tmp)
            ans = min(ans, sortedNums[-1] - sortedNums[0])
        return ans
