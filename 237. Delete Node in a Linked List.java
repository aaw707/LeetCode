/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        // replace node's val with the next node's val
        node.val = node.next.val;
        // skip the next node and point to the one after
        node.next = node.next.next;
        // essentially deleting the "next" node 
        
    }
}