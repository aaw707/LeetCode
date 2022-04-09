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
    public ListNode removeElements(ListNode head, int val) {
        // base case
        if (head == null) {
            return head;
        }
        // remove node if value of head = val
        if (head.val == val) {
            head = head.next;
            return removeElements(head, val);
        } else {
            head.next = removeElements(head.next, val);
            return head;
        }
    }
}