class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest_value_so_far = prices[0]

        biggest_profit=0

        for price in prices:
            biggest_profit = max(biggest_profit,price-smallest_value_so_far)
            smallest_value_so_far = min(smallest_value_so_far,price)

        return biggest_profit
