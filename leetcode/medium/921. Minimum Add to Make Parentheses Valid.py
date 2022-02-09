# problem : https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# time complexity : O(N)

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openBracket = 0
        answer = 0
        
        for c in s:
            if c == ')':
                answer += (openBracket == 0)
                openBracket = max(0, openBracket-1)
            elif c == '(':
                openBracket += 1
        answer += openBracket
        return answer
