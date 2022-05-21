class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        # bfs with memorization
        
        queue = [(amount, 0)]
        seen = set()
        
        # bfs
        while queue:
            remaining_amount, num_coins = queue.pop(0)
            
            # task finished
            if remaining_amount == 0:
                return num_coins
            
            # try each coin 
            for coin in coins:
                if remaining_amount >= coin and remaining_amount - coin not in seen:
                    queue.append((remaining_amount - coin, num_coins + 1))
                    seen.add(remaining_amount - coin)
                    
        # task can't be completed
        return -1
                    
        
            