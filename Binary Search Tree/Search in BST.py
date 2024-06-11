'''Problem Link
https://leetcode.com/problems/search-in-a-binary-search-tree/submissions/1284585779/
'''

class Node:
    def __init__(self, val):
        self.val= val
        self.left= None
        self.right= None

class Solution():
    def search(self, root, x):
        while root is not None and root.val!=x:
            root= root.left if x<root.val else root.right
        return root

root= Node(10)
root.left= Node(5)
root.right= Node(15)
root.left.left= Node(4)
root.left.right= Node(6)
root.right.left= Node(14)
root.right.right= Node(16)

x=6
sol= Solution()
res= sol.search(root, x)
print(f"Result: {res}")
