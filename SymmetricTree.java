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
    public boolean isSymmetric(TreeNode root) {
        return checkSymmetry(root.left, root.right);
    }
    public boolean checkSymmetry(TreeNode node1, TreeNode node2){
        //check left and right
        if (node1 == null && node2 == null) return true;
        else if (node1 == null || node2 == null) return false;
        
        boolean symmetric = checkSymmetry(node1.left, node2.right);
        if (node1.val != node2.val || !symmetric) return false;

        return checkSymmetry(node1.right, node2.left);
    }
}
