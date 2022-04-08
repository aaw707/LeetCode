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
    public ListNode reverseList(ListNode head) {
        // base case
        if (head == null || head.next == null) {
            return head;
        }        
        //find the last node
        ListNode prev = head;
        ListNode node = prev.next;
        while (node.next != null) {
            prev = node;
            node = node.next;
        }
        // make the last node the new head
        ListNode newHead = new ListNode(node.val);
        // delete the last node
        prev.next = null;
        // reverse the rest recursively
        newHead.next = reverseList(head);
        return newHead;
    }
}