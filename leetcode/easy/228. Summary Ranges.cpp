# problem : https://leetcode.com/problems/summary-ranges/
# time complexity : O(N)
# 참고 : https://leetcode.com/problems/summary-ranges/discuss/63193/6-lines-in-Python

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        for num in nums: 
            if not answer or num != (answer[-1][-1] + 1):
                answer.append([num])
            else:
                answer[-1][1:] = num,
        return ['->'.join(list(map(str, tmpAnswer))) for tmpAnswer in answer]
    
    
