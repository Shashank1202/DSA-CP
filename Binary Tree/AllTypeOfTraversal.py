class Node:
    def __init__(self, val):
        self.data= val
        self.left= None
        self.right= None

class Solution:
    def postorder(self,root, arr):
        if not root:
            return
        self.postorder(root.left, arr)
        self.postorder(root.right, arr)
        arr.append(root.data)
    def postorederTraverse(self, root):
        arr= []
        self.postorder(root, arr)
        return arr

    def inorder(self, root, arr):
        if not root:
            return
        self.inorder(root.left, arr)
        arr.append(root.data)
        self.inorder(root.right, arr)

    def inorderTraverse(self, root):
        arr = []
        self.inorder(root, arr)
        return arr

    def preorder(self, root, arr):
        if not root:
            return
        arr.append(root.data)
        self.preorder(root.left, arr)
        self.preorder(root.right, arr)

    def preorederTraverse(self, root):
        arr = []
        self.preorder(root, arr)
        return arr


if __name__== "__main__":
    root= Node(1)
    root.left= Node(2)
    root.right= Node(3)
    root.left.left= Node(4)
    root.left.right= Node(5)
    Sol= Solution()
    result1= Sol.postorederTraverse(root)
    result2= Sol.preorederTraverse(root)
    result3= Sol.inorderTraverse(root)
    print("Postorder Traversal :", end=" ")
    for val in result1:
        print(val, end=" ")
    print()
    print("Preorder Traversal :", end=" ")
    for val in result2:
        print(val, end=" ")
    print()
    print("Inorder Traversal :", end=" ")
    for val in result3:
        print(val, end=" ")
    print()

