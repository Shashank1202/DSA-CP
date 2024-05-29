'''Problem Link
https://leetcode.com/problems/binary-tree-level-order-traversal/
'''
from collections import deque
class Node:
    def __init__(self, val):
        self.val= val
        self.left=None
        self.right= None

class Solution:
    def LevelOrder(self, root):
        ans=[]
        if not root:
            return

        q=deque()
        q.append(root)
        while q:
            size= len(q)
            level= []
            for i in range(size):
                node= q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans

if __name__=="__main__":
    root= Node(1)
    root.left= Node(2)
    root.right= Node(3)
    root.left.left= Node(4)
    root.left.right= Node(5)

    sol= Solution()
    result= sol.LevelOrder(root)
    for i in result:
        print(i)
