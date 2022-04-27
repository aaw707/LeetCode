/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

      public class Solution extends VersionControl {
        public int firstBadVersion(int n) {
            // binary search
            // O(log(n))
            int start = 1;
            int end = n;
            int mid = -1;
            
            int smallestBadVersionKnown = n;
            int greatestGoodVersionKnown = 0;
            
            while (start < end) {
                mid = (int) (start / 2.0 + end / 2.0);
                // mid is bad. turned bad before mid
                if (isBadVersion(mid)) {
                    end = mid;
                    smallestBadVersionKnown = mid;
                // mid is good. turned bad after mid
                } else {
                    start = mid;
                    greatestGoodVersionKnown = mid;
                }
                if (smallestBadVersionKnown - greatestGoodVersionKnown == 1) {
                    return smallestBadVersionKnown;
                }
            }
            // will not be executed
            return smallestBadVersionKnown;
        }
    }