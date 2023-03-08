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

    public int kthSmallest(TreeNode root, int k) {
        List<Integer> sortedValues = getSmallest(root, new ArrayList<Integer>());
        return sortedValues.get(k-1);
    }
    public List<Integer> getSmallest(TreeNode root, List<Integer> order){
        if (root==null) return new ArrayList<Integer>();

        getSmallest(root.left, order);
        order.add(root.val);
        getSmallest(root.right, order);

        return order;
    }
}
