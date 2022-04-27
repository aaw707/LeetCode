/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

      public class Solution extends VersionControl {
        public int firstBadVersion(int n) {
            // binary search
            // O(log(n))
            int start = 1;
            int end = n;
            int mid = 1;
            while (start <= end) {
                mid = start / 2 + end / 2;
                // mid and mid+1 are both bad. turned bad before mid+1
                if (isBadVersion(mid) && isBadVersion(mid + 1)) {
                    end = mid;
                // mid and mid+1 are both good. turned bad after mid
                } else if (!isBadVersion(mid) && !isBadVersion(mid + 1)) {
                    start = mid + 1;
                } else {
                    return mid + 1;
                }
            }
            // will not be executed
            return -1;
        }
    }