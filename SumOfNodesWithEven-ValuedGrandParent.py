class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        stack = [root]
        calc_sum = 0

        while stack:
            node = stack.pop()
            if node.val % 2 == 0:
                #get the sums
                calc_sum += self.getGrandChildSum(node)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return calc_sum

    def getGrandChildSum(self, root):
        totalGrandChildSum = 0
        if root.left and root.left.left:
            totalGrandChildSum += root.left.left.val

        if root.left and root.left.right:
            totalGrandChildSum += root.left.right.val

        if root.right and root.right.left:
            totalGrandChildSum += root.right.left.val
        
        if root.right and root.right.right:
            totalGrandChildSum += root.right.right.val

        return totalGrandChildSum
