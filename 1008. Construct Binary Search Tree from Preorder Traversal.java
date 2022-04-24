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
    public TreeNode bstFromPreorder(int[] preorder) {
        // base case: if input is an empty list, return null
        if (preorder.length == 0 || preorder[0] == 0) {
            return null;
        }
        // root val = first element in preorder
        TreeNode root = new TreeNode(preorder[0]);
        int len = preorder.length;
        int split = len;
        // find the split between nums smaller than root val, and nums larger
        for (int i = 1; i < len; i++) {
            if (preorder[i] > root.val) {
                split = i;
                break;
            }
        }
        // recursively build the left subtree with nums smaller than root val
        root.left = bstFromPreorder(Arrays.copyOfRange(preorder, 1, split));
        // ... right subtree.. larger...
        root.right = bstFromPreorder(Arrays.copyOfRange(preorder, split, len));
        return root;
    }
}