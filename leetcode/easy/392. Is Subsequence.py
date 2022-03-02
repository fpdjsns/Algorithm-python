# problem : https://leetcode.com/problems/is-subsequence/
# time complexity : O(N), N = |t|

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tInd, sInd = 0, 0
        tLen, sLen = len(t), len(s)
        while sInd < sLen and tInd < tLen:
            sInd += s[sInd] == t[tInd]
            tInd += 1
        return sInd == sLen
        
