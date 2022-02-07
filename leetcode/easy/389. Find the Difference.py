# problem : https://leetcode.com/problems/find-the-difference/
# time complexity : O(N)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sCounter = Counter(s)
        tCounter = Counter(t)
        for k, v in tCounter.items():
            if sCounter[k] != v :
                return k
        return ''
        
