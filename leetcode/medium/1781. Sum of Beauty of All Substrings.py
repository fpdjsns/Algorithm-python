# problem : https://leetcode.com/problems/sum-of-beauty-of-all-substrings/
# time complexity : O(N^2)

class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0
        for startInd in range(n):
            cnts = {}
            for endInd in range(startInd, n):
                cnts[s[endInd]] = cnts.get(s[endInd], 0) + 1
                ans += max(cnts.values()) - min(cnts.values())
        return ans
