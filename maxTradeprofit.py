"""leetCode questions

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        while prices and prices[-1] == 0:
            prices.pop()
        max_profit = 0
        min_price = prices[0]

        #determine max price in all possible combinations

       class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        while prices and prices[-1] == 0:
            prices.pop()
        max_profit = 0
        min_price = prices[0]

        #min price, maximum profit

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        

        return max_profit
        
        

