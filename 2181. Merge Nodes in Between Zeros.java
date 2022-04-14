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
    public ListNode mergeNodes(ListNode head) {
        // new head to return
        ListNode newHead = new ListNode(0);
        // cursor to go through new list
        ListNode cursor = newHead;
        // sum of sub lists
        int sum = 0;
        
        // skip the beginning 0
        head = head.next;
        // go over the list
        while (head != null) {
            // if val == 0
            if (head.val == 0) {
                // create a new node with the cumulated sum
                ListNode newNode = new ListNode(sum);
                // append it to the end of new list
                cursor.next = newNode;
                // move the cursor to the end
                cursor = cursor.next;
                // clear the sum for the next sub list
                sum = 0;
            } else {
                // cumulate the sum
                sum += head.val;
            }
            // go to the next node in list
            head = head.next;            
        }
        // skip the node at initiation
        return newHead.next;
    }
}