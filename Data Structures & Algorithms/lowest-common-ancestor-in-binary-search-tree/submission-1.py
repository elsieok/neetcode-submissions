# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestor = root
        left = min(p.val, q.val)
        right = max(p.val, q.val)
        while not (left <= ancestor.val and right >= ancestor.val):
            if right < ancestor.val:
                ancestor = ancestor.left
                continue
            if left > ancestor.val:
                ancestor = ancestor.right
                continue
        return ancestor