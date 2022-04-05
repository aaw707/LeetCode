class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # start with the widest area
        L = 0
        R = len(height) - 1
        area = 0
        
        while L < R:
            width_ = R - L
            height_ = min(height[L], height[R])
            area = max(area, width_ * height_)
            
            # since the width is getting smaller, the only way to get bigger area is to have larger height
            # only shrink on the side with shorter line
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
                
        return area