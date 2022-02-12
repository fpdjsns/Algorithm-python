# problem : https://leetcode.com/problems/permutation-in-string/
# time complexity : O(N + M) # N = |s1|, M = |s2|

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1Dict = {}
        for c in s1: 
            s1Dict[c] = s1Dict.get(c, 0) + 1
            
        left = 0
        for right in range(len(s2)):
            c = s2[right]
            s1Dict[c] = s1Dict.get(c, 0) - 1
            if s1Dict[c] < 0:
                while s2[left] != c:
                    s1Dict[s2[left]] += 1
                    left += 1
                s1Dict[s2[left]] += 1
                left += 1
            if right - left + 1 == n:
                return True
        return False
