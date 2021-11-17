/**
 * problem : https://leetcode.com/problems/unique-paths/
 * time complexity : O(nm)
 * space complexity : O(n)
 * algorithm : DP
 */
 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*(n+1)
        dp[0] = 0
        for x in range(1, m):
            for y in range(1, n+1):
                dp[y] += dp[y-1];
        return dp[n]
        
