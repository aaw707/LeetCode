class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_buy = prices[0]
        
        for price in prices:
            # update the minimum buying value
            if price <= min_buy:
                min_buy = price
            else:              
                profit = price - min_buy
                # update the max profit
                max_profit = max(max_profit, profit)
            
        return max_profit
            