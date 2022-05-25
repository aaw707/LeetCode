class MinStack(object):

    def __init__(self):
        self.stack = []   
        self.min = float('inf')

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val <= self.min:
            self.stack.append(self.min)
            self.min = val
        self.stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()
        if val == self.min:
            self.min = self.stack.pop()
        if not self.stack:
            self.min = float("inf")
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()