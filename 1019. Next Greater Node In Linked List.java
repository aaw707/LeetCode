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
    public int[] nextLargerNodes(ListNode head) {
        
        // put LL in an array
        ArrayList<Integer> arr = new ArrayList<>();
        ListNode node = head;
        while (node != null) {
            arr.add(node.val);
            node = node.next;
        }
        
        // another list to store the answers
        int n = arr.size() - 1;
        int[] answers = new int[n + 1];
        
        // stack 
        Stack<Integer> stack = new Stack<>();
        
        // go over vals in arr backwards
        for (int i = n; i >= 0; i--) {
            // current val
            int val = arr.get(i);
            // remove vals in stack <= the current val
            while (!stack.isEmpty() && stack.peek() <= val) {
                stack.pop();
            }
            
            // no val larger than arr[i]
            if (stack.isEmpty()) {
                answers[i] = 0;
                
            // val on top of stack is the next greater val
            } else {
                answers[i] = stack.peek();
            }
            // add current val onto top of stack
            stack.push(val);
        }
        return answers;
    }
}
