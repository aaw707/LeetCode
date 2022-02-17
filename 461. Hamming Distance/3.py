class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        binary_differences = bin(x ^ y)[2:]
        return binary_differences.count("1")

# using bit operators
# similar speed but less code