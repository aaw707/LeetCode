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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // base cases
        if (l1 == null && l2 == null) {
            return null;
        } else if (l1 == null) {
            if (l2.val == 10) {
                l1 = new ListNode(0);
            } else {
                return l2;
            }
        } else if (l2 == null) {
            if (l1.val == 10) {
                l2 = new ListNode(0);                
            } else {
                return l1;
            }
        }
        
        // l1 and l2 are not null
        int val = l1.val + l2.val;
        // carry to the next digit
        if (val >= 10) {
            val = val - 10;
            if (l1.next != null) {
                l1.next.val++;
            } else if (l2.next != null) {
                l2.next.val++;
            } else {
                l1.next = new ListNode(1);
            }
        }
        // recursive solution
        ListNode root = new ListNode(val);
        root.next = addTwoNumbers(l1.next, l2.next);
        return root;
    }
}