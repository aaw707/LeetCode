import java.util.stream.IntStream;

class Solution {
    public boolean canThreePartsEqualSum(int[] arr) {
        
        int sum = IntStream.of(arr).sum();
        
        if (sum % 3 != 0) {
            return false;
        }

        int average = sum / 3;
        int n = arr.length;

        int first_part_sum = 0;
        int second_part_sum = 0;

        for (int i = 0; i < n - 2; i++) {

            first_part_sum += arr[i];
            if (first_part_sum == average) {

                for (int j = i + 1; j < n - 1; j++) {
                    second_part_sum += arr[j];

                    if (second_part_sum == average) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}