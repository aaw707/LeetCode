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
    public void flatten(TreeNode root) {
        
        helper(root);
        
    }
    
    private TreeNode helper(TreeNode root) {
        
        // base case
        if (root == null) {
            return null;
        }
        
        // take out the subtrees
        TreeNode left_subtree = root.left;
        TreeNode right_subtree = root.right;
        
        // delete the original left subtree
        root.left = null;
        
        // add the flattened left subtree to the right
        root.right = helper(left_subtree);
        
        // traverse to the end of our new tree
        TreeNode node = root;
        while (node.right != null) {
            node = node.right;
        }
        
        // add the flattened right subtree to the right
        node.right = helper(right_subtree);
        
        // return the root: tree is flattened
        return root;
        
    }
}