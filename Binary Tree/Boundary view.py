'''
Problem Link
https://leetcode.com/problems/boundary-of-binary-tree/description/
'''

class Node:
    def __init__(self, data):
        self.data= data
        self.left= None
        self.right= None

class Solution:
    def isLeaf(self, root):
        return not root.left and not root.right

    def leftBoundary(self, root, res):
        curr= root.left
        while curr:
            if not self.isLeaf(curr):
                res.append(curr.data)
            if curr.left:
                curr=curr.left
            else:
                curr=curr.right

    def rightBoundary(self, root, res):
        ds= []
        curr= root.right
        while curr:
            if not self.isLeaf(curr):
                ds.append(curr.data)

            if curr.right:
                curr = curr.right
            else:
                curr=curr.left
        for i in range(len(ds)-1, -1, -1):
            res.append(ds[i])

    def addLeaf(self, root, res):
        if self.isLeaf(root):
            res.append(root.data)
            return res
        if root.left:
            self.addLeaf(root.left, res)
        if root.right:
            self.addLeaf(root.right, res)

    def addBoundary(self, root):
        res= []
        if not root:
            return res

        if not self.isLeaf(root):
            res.append(root.data)

        self.leftBoundary(root, res)
        self.addLeaf(root, res)
        self.rightBoundary(root, res)

        return res

def printRes(ans):
    for i in ans:
        print(i, end= ' ')
    print()


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

solution = Solution()

# Get the boundary traversal
result = solution.addBoundary(root)

# Print the result
print("Boundary Traversal:", end=" ")
printRes(result)
