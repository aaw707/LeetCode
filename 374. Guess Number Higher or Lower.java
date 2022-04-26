/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int start = 1;
        int end = n;
        int mid;
        int res;
        // binary search for target
        while (start < end) {
            mid = start / 2 + end / 2; // avoid exceeding int range
            res = guess(mid);
            // update pointers by res
            if (res < 0) {
               end = mid - 1; 
            } else if (res > 0) {
                start = mid + 1;
            } else {
                return mid;
            }
        }
        return start;
    }
}