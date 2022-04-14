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
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode nodeA;
        ListNode nodeB;
        ListNode node = list1;
        // num of nodes to go through from 0 to a-1 th node
        int n = a - 1;
        // num of nodes to go through from a-1 th to b+1 th node
        int m = b - a + 2;
        
        // find a-1 th node
        while (n > 0) {
            node = node.next;
            n--;
        }
        // a-1 th node
        nodeA = node;
        
        // find b+1 th node
        while (m > 0) {
            node = node.next;
            m--;
        }
        // b+1 th node
        nodeB = node;
        
        // set cursor at beginning of list2
        node = list2;
        // connect a-1 th node to the beginning of list2
        nodeA.next = list2;
        // move cursor to end of list2
        while (node.next != null) {
            node = node.next;
        }
        // connect end of list2 to b+1 th node
        node.next = nodeB;
        // return
        return list1;
    }
}