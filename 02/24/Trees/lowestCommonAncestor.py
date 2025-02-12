# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # root
        # case: exist on different branches
        # p > root and q < root
        # q > root and p < root
        # => return root

        # case: on one side
        # p < root and q < root
        # p > root and q > root
        # => continue down that side

        # case: root is p or q
        # p == root or q == root
        # ==> return root

        isDiffBranch = (p.val > root.val and q.val < root.val) or (
            q.val > root.val and p.val < root.val)

        isSameNode = p.val == root.val or q.val == root.val

        if isDiffBranch or isSameNode:
            return root

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
