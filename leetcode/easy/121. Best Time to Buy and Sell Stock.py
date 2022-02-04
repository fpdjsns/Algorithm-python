# problem : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# time complexity : O(N)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        answer = 0
        for price in prices:
            if minPrice < price:
                answer = max(answer, price - minPrice)
            else:
                minPrice = price
        return answer
