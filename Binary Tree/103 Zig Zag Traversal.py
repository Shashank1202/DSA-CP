'''Problem Link:
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result= []
        if not root:
            return result
        
        queue= deque()
        queue.append(root)
        flag= True
        while queue:
            size= len(queue)
            row= [0]* size
            for i in range(size):
                node=queue.popleft()
                index= i if flag else(size-1-i)
                row[index]=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            flag= not flag
            result.append(row)
        return result
