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
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        int len = nums.length;
        if (len == 0) {
            return null;
        }
        int max = 0;
        int maxIdx = 0;
        for (int i = 0; i < len; i++) {
            int val = nums[i];
            if (val > max) {
                max = val;
                maxIdx = i;
            }
        }
        TreeNode root = new TreeNode(max);
        // left sub arr
        int[] leftNums = Arrays.copyOfRange(nums, 0, maxIdx);
        root.left = constructMaximumBinaryTree(leftNums);
        // right sub arr
        int[] rightNums = Arrays.copyOfRange(nums, maxIdx + 1, len);
        root.right = constructMaximumBinaryTree(rightNums);
        
        // return
        return root;
        
    }
}