# problem : https://leetcode.com/problems/counting-bits/
# time complexity : O(NlogN)

class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(num).count('1') for num in range(n+1)]
