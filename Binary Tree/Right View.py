'''
Problem Link
https://leetcode.com/problems/binary-tree-right-side-view/submissions/1280182649/
'''
from typing import List
class Node:
    def __init__(self, val):
        self.val= val
        self.left= None
        self.right= None

class Solution:
    def RightView(self, root):
        res= []

        self.Recursion(root,0, res)
        return res

    def Recursion(self,root, level, res):
        if not root:
            return

        if len(res)==level:
            res.append(root.val)

        self.Recursion(root.right, level+1, res)
        self.Recursion(root.left, level+1, res)


root= Node(1)
root.left= Node(2)
root.right= Node(3)
root.right.right= Node(4)
root.left.right= Node(5)
root.left.right.right= Node(6)
solution= Solution()
RView= solution.RightView(root)

print("The right view of Tree:",end=" ")
for node in RView:
    print(node, end=' ')
print()
