# problem : https://leetcode.com/problems/sequential-digits/
# time complexity : O(1)

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        answer = []
        digits = '123456789'
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(0, 9):
                if start+length >= 10: break
                now = int(digits[start: start+length])
                if now < low: continue
                if now > high: break
                answer.append(now)
        return sorted(answer)
