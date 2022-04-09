/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        // base case
        if (head == null || head.next == null) {
            return true;
        }
        ArrayList<Integer> arr = new ArrayList<>();
        // store LL vals into arr
        while (head != null) {
            arr.add(head.val);
            head = head.next;
        }
        // size of arr
        int size = arr.size();
        // range of for loop - half of arr
        int range = (int) size / 2;
        for (int i = 0; i < size; i++) {
            // compare the first & last item
            if (arr.get(i) != arr.get(size - 1 - i)) {
                return false;
            }
        }
        return true;
            
    }
}