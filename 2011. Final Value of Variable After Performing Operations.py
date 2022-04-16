class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        t = {
            "X++": 1,
            "++X": 1,
            "X--": -1,
            "--X": -1
        }
        res = 0
        for op in operations:
            res += t[op]
        return res