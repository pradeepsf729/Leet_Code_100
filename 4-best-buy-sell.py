"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

"""

"""
def stock_buy_sell(nums):
    max_profit = 0
    cur_buy = nums[0]
    for i in range(1, len(nums)):
        cur_sell = nums[i]
        cur_profit = cur_sell - cur_buy
        if cur_profit > max_profit:
            max_profit = cur_profit
        elif cur_profit < 0:
            cur_buy = cur_sell
    return max_profit

prices = [7,6,4,3,1]
assert stock_buy_sell(prices) == 0

prices = [7,1,5,3,6,4]
assert stock_buy_sell(prices) == 5


