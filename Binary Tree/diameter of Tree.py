'''
Problem Link
https://leetcode.com/problems/diameter-of-binary-tree/
'''

class Node:
    def __init__(self, data):
        self.data= data
        self.left= None
        self.right= None

''' Brute Force approach O(N^2) compexity
class Solution():
    def __init__(self):
        self.maxi=0


    def cal(self, node):
        if node is None:
            return 0

        left_height= self.cal(node.left)
        right_height= self.cal(node.right)

        self.maxi= max(self.maxi, left_height+ right_height)
        return 1+ max(left_height, right_height)

    def diameter(self, root):
        self.cal(root)
        return self.maxi
'''
'''Best approach :- O(N) Compexity'''
class Solution():
    def diameter(self, root):
        diameter= [0]
        self.height(root, diameter)
        return diameter[0]

    def height(self, root, diameter):
        if not root:
            return 0

        lh=self.height(root.left, diameter)
        rh= self.height(root.right, diameter)

        diameter[0]= max(diameter[0], lh+rh)
        return 1+ max(lh, rh)

if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)

    # Creating an instance of the Solution class
    solution = Solution()

    # Calculate the diameter of the binary tree
    diameter= solution.diameter(root)

    print("The diameter of the binary tree is:", diameter)
