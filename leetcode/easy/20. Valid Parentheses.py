# problem : https://leetcode.com/problems/valid-parentheses/
# time complexity : O(N)

class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch in ['(', '{', '[']:
                st.append(ch)
            elif len(st) == 0:
                return False
            elif st[-1] == '(' and ch == ')':
                st.pop(-1)
            elif st[-1] == '{' and ch == '}':
                st.pop(-1)
            elif st[-1] == '[' and ch == ']':
                st.pop(-1)
            else:
                return False
        return len(st) == 0
                
