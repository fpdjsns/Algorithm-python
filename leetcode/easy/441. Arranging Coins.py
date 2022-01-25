# problem : https://leetcode.com/problems/arranging-coins/
# algorithm : BST
# time complexity : O(NlogN)

class Solution:
    def arrangeCoins(self, n: int) -> int:
        answer = 0
        l, r = 0, n
        while l <= r:
            m = int((l + r) / 2)
            if m * (m+1) / 2 <= n: 
                l = m+1
                answer = m
            else: 
                r = m-1
        
        return answer
