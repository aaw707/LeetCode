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
    public int getDecimalValue(ListNode head) {
        String num = "";
        // convert linkedlist values to a string
        while (head != null) {
            num += head.val;
            head = head.next;
        }
        int decimal = Integer.parseInt(num, 2);
        return decimal;
    }
}