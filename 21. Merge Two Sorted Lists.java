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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // one list is empty, return the other one
        if (list1 == null) {
            return list2;
        } else if (list2 == null) {
            return list1;
        }
        // both lists are not empty
        // construct the new head
        ListNode newHead = new ListNode();
        // find the larger head
        if (list1.val < list2.val) {
            newHead.val = list1.val;
            newHead.next = mergeTwoLists(list1.next, list2);
        } else {
            newHead.val = list2.val;
            newHead.next = mergeTwoLists(list1, list2.next);
        }
        return newHead;
    }
    
}