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
    public int pairSum(ListNode head) {
        // find length
        ListNode node = head;
        int n = 0;
        while (node != null) {
            n++;
            node = node.next;
        }
        // length half of the LL to put on stack
        n = n / 2;
        
        // create stack
        Stack<ListNode> s = new Stack<>();
        // put cursor back to head
        node = head;
        // put first half of LL on stack
        while (n > 0) {
            s.push(node);
            node = node.next;
            n--;
        }
        // node now points at the beginning of the second half of LL
        
        // record max twin sum
        int max = 0;
        // go over the second half of LL
        while (node != null) {
            // take the top node off from stack
            ListNode top = s.pop();
            // calculate twin sum
            int twin_sum = node.val + top.val;
            // record max twin sum
            if (twin_sum > max) {
                max = twin_sum;
            }
            node = node.next;
        }
        // return max twin sum
        return max;
    }
}