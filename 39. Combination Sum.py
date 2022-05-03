class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        
        for num in candidates:
            if num > target:
                pass
            elif num == target:
                res.append([num])
            else: # num < target
                backtracking = self.combinationSum(candidates, target - num)
                for combination in backtracking:
                    # only add combination with ascending order to res to avoid duplicates
                    if num >= combination[-1]:
                        combination.append(num)
                        res.append(combination)
        
        return res