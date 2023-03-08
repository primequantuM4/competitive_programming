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
    public List<Integer> rightSideView(TreeNode root) {
        if (root==null) return new ArrayList<Integer>();

        List<List<Integer>> res = new ArrayList<>();
        List<Integer> ans = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while(queue.size() > 0){
            int length = queue.size();
            List<Integer> list = new ArrayList<>();
            for (int i = 0; i < length; i++){
                TreeNode value = queue.remove();
                if(value.left !=null) queue.add(value.left);
                if(value.right != null) queue.add(value.right);
                list.add(value.val);
            }
            res.add(list);
        }
        for (List<Integer> i: res) ans.add(i.get(i.size() - 1));
        return ans;
    }
}
