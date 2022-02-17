class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance_counter = 0

        # start comparing from the last digit
        while x > 0 or y > 0:
            distance_counter += (x % 2) ^ (y % 2)  # XOR 
            # shift the number in binary to the right
            x >>= 1
            y >>= 1
        
        return distance_counter

# using bit shift operators
# little slower than 1.py
