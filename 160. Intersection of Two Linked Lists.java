/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
import java.util.*;

public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        // cursors
        ListNode cursorA = headA;
        ListNode cursorB = headB;
        // cursorA: walks down listA then listB
        // cursorB: walks down listB then listA
        // cursorA == cursorB when cursorA in listB and cursorB in listA
        // or they both = null at the end of journey when there's no intersection
        while (cursorA != cursorB) {
            if (cursorA == null) {
                cursorA = headB;
            } else {
                cursorA = cursorA.next;
            }
            if (cursorB == null) {
                cursorB = headA;
            } else {
                cursorB = cursorB.next;
            }
        }
        return cursorA; // either the intersection node or null
    }
}