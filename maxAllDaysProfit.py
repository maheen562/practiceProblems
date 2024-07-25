"""You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve."""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min_price = prices[0]
        curr_max_price = 0
        total_profit = 0

        arr_len = len(prices)
        # we achieve maxprofit by always selling it when the price is higher from when we bought it
        # first we determine when it is cheapest to by
        # then sell it when we find a price higher then that price, before it goes down again
        index = 1
        curr_min_index = 0
        curr_max_index = 0
        #we determine the curr min, and curr max
        while(index<arr_len):
            if prices[index] < curr_min_price:
                curr_min_price = prices[index]
                curr_min_index = index
            elif prices[index] > curr_max_price and index>curr_min_index and prices[index] > curr_min_price:
                curr_max_price = prices[index]
                curr_max_index = index
            

            if index+1< arr_len and curr_max_price > prices[index + 1] and curr_min_price<curr_max_price and        curr_min_index< curr_max_index:
                # we sell
                total_profit =  total_profit + (curr_max_price - curr_min_price)
                curr_min_price =  prices[index+1]
                curr_max_price = 0
                print(curr_max_price, curr_min_price,curr_min_index)

            # if last position we only see if the current price gives us the profit
            
            if index == arr_len - 1 and curr_max_price>curr_min_price and curr_min_index< curr_max_index:

                total_profit =  total_profit + (curr_max_price - curr_min_price)
                
            index=index+1
        
        return total_profit