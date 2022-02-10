# problem : https://leetcode.com/problems/longest-substring-without-repeating-characters/
# time complexity : O(N)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxIndex = {}
        answer = 0
        index = -1
        for i in range(len(s)):
            c = s[i]
            index = max(index, maxIndex.get(c, -1))
            answer = max(answer, i - index)
            maxIndex[c] = i
        return answer
