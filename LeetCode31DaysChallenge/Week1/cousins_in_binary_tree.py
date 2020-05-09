"""
Problem Statement
Cousins in Binary Tree
Solution
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.



Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false


Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """Solution-1"""
        # queue = [root]
        # queue2 = [root.val]
        # parents = [0]
        # while queue:
        #     levelSiz = len(queue)
        #     while levelSiz:
        #         element = queue.pop(0)
        #         queue2.pop(0)
        #         parents.pop(0)
        #         if element.left:
        #             queue2.append(element.left.val)
        #             queue.append(element.left)
        #             parents.append(element)
        #         if element.right:
        #             queue2.append(element.right.val)
        #             queue.append(element.right)
        #             parents.append(element)
        #         levelSiz -= 1
        #     if x in queue2 and y in queue2:
        #         x_i = queue2.index(x)
        #         y_i = queue2.index(y)
        #         if parents[x_i] == parents[y_i]:
        #             return False
        #         return True
        # return False

        """Solution-2"""
        def dfs(node: TreeNode, parent: TreeNode, depth: int):
            if not node or len(results) == 2:
                return
            else:
                if node.val == x or node.val == y:
                    results.append((parent, depth))
                dfs(node.left, node, depth + 1)
                dfs(node.right, node, depth + 1)

        results = []
        dfs(root, None, 0)

        return results[0][0] != results[1][0] and results[0][1] == results[1][1]
