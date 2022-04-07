# problem : https://leetcode.com/problems/last-stone-weight/
# time complexity : O(NlogN)

import queue
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        que = queue.PriorityQueue()
        for stone in stones:
            que.put(-stone)
        while que.qsize() > 1:
            diff = -1 * (que.get() - que.get())
            print(diff)
            if diff > 0:
                que.put(-diff)
        return 0 if que.empty() else -que.get()
            
