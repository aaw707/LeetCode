class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        # to reach ith step, cost = cost[i] + min(cost to reach stair i - 1, cost to reach stair i - 2)
        cost.append(0)
        n = len(cost)
        
        first = cost[0]
        second = cost[1]
        
        # dp
        for i in range(2, n):
            
            step_cost = cost[i] + min(first, second)
            first = second
            second = step_cost
            
        return second
            