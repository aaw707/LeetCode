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
    ArrayList<Integer> arr = new ArrayList<Integer>();
    
    public TreeNode balanceBST(TreeNode root) {
        // put node values to a sorted list
        inorder(root); 
        System.out.println(arr.toString());
        // size of arr
        int len = arr.size();
        // construct new root
        TreeNode newRoot = constructTree(0, len - 1);
        return newRoot;
    }
    
    void inorder(TreeNode root) {
        if (root == null) {
            return;
        }
        inorder(root.left);
        arr.add(root.val);
        inorder(root.right);
    }
    
    TreeNode constructTree(int startIdx, int endIdx) { // start & end inclusive
        if (endIdx < startIdx) { //invalid
            return null;
        }
        // reconstruct tree
        TreeNode root = new TreeNode();
        // middle idx
        int midIdx = (int) (endIdx + startIdx) / 2;
        // root value
        root.val = arr.get(midIdx);
        // left child
        root.left = constructTree(startIdx, midIdx - 1);
        // right child
        root.right = constructTree(midIdx + 1, endIdx);
        return root;
    }
}