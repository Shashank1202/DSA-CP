'''
Problem Link
https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1
'''

class Node:
    def __init__(self,val):
        self.val= val
        self.left= None
        self.right= None

class Solution:
    def RootToNode(self, root, x):
        arr= []
        self.getPath(root, arr, x)
        return arr

    def getPath(self, root, arr, x):
        if not root:
            return False

        arr.append(root.val)
        if root.val== x:
            return True

        if self.getPath(root.left, arr, x) or self.getPath(root.right, arr, x):
            return True

        arr.pop()
        return False

root= Node(1)
root.left= Node(2)
root.right= Node(3)
root.left.right=Node(4)
root.left.right.left= Node(5)

target = 5

sol= Solution()

res= sol.RootToNode(root,target)

for i in res:
    print(i, end=' ')
