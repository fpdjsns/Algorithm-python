# problem : https://leetcode.com/problems/gas-station/
# time complexity : O(N)

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        answer, subSum, total, n = 0, 0, 0, len(gas)
        for i in range(n):
            subSum += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if subSum >= 0: # possible
                continue
            # impossible
            subSum = 0
            answer = i+1 # set start to next station
        return answer if total >= 0 else -1
        
        
