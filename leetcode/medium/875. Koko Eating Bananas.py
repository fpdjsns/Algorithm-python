# problem : https://leetcode.com/problems/koko-eating-bananas/
# time complexity : O(NlogN)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        def canAns(k: int, h: int) -> bool:
            for pile in piles:
                h -= int((pile + k - 1) / k)
                if h < 0:
                    return False
            return True
        l, r = 1, 1
        for pile in piles:
            r = max(r, pile)
        
        while l < r:
            m = int((l + r)/2)
            if canAns(m, h):
                r = m
            else:
                l = m + 1
        return l
            
