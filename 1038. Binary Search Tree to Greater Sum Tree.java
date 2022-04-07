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
    int sum = 0;
        
    public TreeNode bstToGst(TreeNode root) {
        gst(root);
        return root;        
    }
    
    public void gst(TreeNode root) {
        // like a reverse inorder traversal: right -> node -> left
        // cache the sum as it goes to save time
        
        // base case
        if (root == null) {
            return;
        }
        // process right child (subtree) first
        gst(root.right);
        // process root next
        sum += root.val;
        root.val = sum;            
        // process left child (subtree) last
        gst(root.left);
    } 
    

    

}