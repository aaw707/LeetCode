/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int prev = 0;
    int curMax = 0;
    int max = 0;
    ArrayList<Integer> res = new ArrayList<Integer>();
    
    public int[] findMode(TreeNode root) {
        // go through tree and save the modes in res
        inorder(root);
        // copy the modes from list to array
        int ans[] = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            ans[i] = res.get(i);
        }
        return ans;
        }
    
    
    void inorder(TreeNode root) {
        if (root == null) {
            return;
        }
        // process left child
        inorder(root.left);
        
        // process root
        
        // if root has same value as prev, add on the current max
        if (prev == root.val) {
            curMax++;
            
        // else, set prev as current value, re-count curMax
        } else {
            prev = root.val;
            curMax = 1;
        }
        
        // if curMax exceeded max, set max as curMax, clear the existing values in res and add root value
        if (curMax > max) {
            max = curMax;
            res.clear();
            res.add(root.val);
            
        // if curMax == max, add root val into res as it's currently the mode
        } else if (curMax == max) {
            res.add(root.val);
        }
        
        // process right child
        inorder(root.right);
    }
}