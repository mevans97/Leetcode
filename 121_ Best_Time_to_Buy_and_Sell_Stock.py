'''
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
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l,r = 0,1 #Left=Buy #Right = sell
        mp=0
        
        while r < len(prices):
            if prices[r] > prices[l]: #This shows what to do if a profitable transaction is found 
                if prices[r] - prices[l] > mp:
                    mp = prices[r] - prices[l]
            
            if prices[r] < prices[l]:#This shows what to do if an unprofitable transaction is found
                l = r # we move left to where the right pointer is because we know it is the next value less than the current buy value
            r+=1 # we continue moving the r value with an increment of one no matter what if statement is triggered so I keep this outside of each
        
        return mp
'''
Runtime: 773 ms, faster than 54.40% of Python online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 22.5 MB, less than 22.88% of Python online submissions for Best Time to Buy and Sell Stock.
'''
