class Solution {
    public boolean isPerfectSquare(int num) {
        // base case
        if (num == 1) {
            return true;
        }
        // try out possible factors one by one
        double factor = 2.0;
        while (true) {
            double res = num / factor;
            if (res > factor) {
                factor++;
            } else if (res < factor) {
                return false;
            } else {
                return true;
            }
        }
    }
}