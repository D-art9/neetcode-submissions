# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(curr):

            currvalue = curr.val

            if p.val == currvalue or q.val == currvalue:
                return curr

            elif p.val < currvalue and q.val > currvalue:
                return curr

            elif p.val > currvalue and q.val > currvalue:
                return dfs(curr.right)

            elif p.val < currvalue and q.val < currvalue:
                return dfs(curr.left)

            else:
                return curr

        return dfs(root)


    
        