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
    public ListNode middleNode(ListNode head) {
        int count = 0;
        ListNode node = head;
        // count the num of nodes in the LL
        while (node != null) {
            count++;
            node = node.next;
        }
        // find the idx of middle node
        int middle = (int) count / 2;
        // find the middle node
        ListNode cursor = head;
        while (middle > 0) {
            cursor = cursor.next;
            middle--;
        }
        return cursor;
    }
}