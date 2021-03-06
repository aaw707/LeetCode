class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        # 1-indexed
        for i in range(1, n + 1):
            if i % (3 * 5) == 0:
                res.append("FizzBuzz")
            elif i % 5 == 0:
                res.append("Buzz")
            elif i % 3 == 0:
                res.append("Fizz")
            else:
                res.append(str(i))
        return res