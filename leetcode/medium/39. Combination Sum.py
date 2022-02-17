# problem : https://leetcode.com/problems/combination-sum/
# time complexity : O(N^2) // N = |candidates|
# algorithm : backtracking

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(index, rest, subList, answer, candidates):
            if rest == 0:
                answer.append(subList)
                return
            for i in range(index, len(candidates)):
                tmpRest = rest - candidates[i]
                if tmpRest >= 0:
                    dfs(i, tmpRest, subList + [candidates[i]], answer, candidates)
                
        answer = []
        dfs(0, target, [], answer, candidates)
        return answer
