class Solution {
    public int maxArea(int[] height) {
        // starting from the widest container
        // idx of walls
        int i = 0;
        int j = height.length - 1;
        // height of walls
        int left = height[i];
        int right = height[j];
        // width
        int currentMaxHeight = Math.min(left, right);
        int width = j - i;
        // area
        int currentMaxArea = currentMaxHeight * width;
        
        // shrink the width, looking for greater height, checking for possible greater area
        while (i < j) {
            if (height[i] < height[j]) {
                i++;
            } else {
                j--;
            }
            int current_height = Math.min(height[i], height[j]);
            if (current_height > currentMaxHeight) {
                width = j - i;
                int current_area = width * current_height;
                if (current_area > currentMaxArea) {
                    currentMaxArea = current_area;
                    currentMaxHeight = current_height;
                }
            }
        }
        return currentMaxArea;
    }
}