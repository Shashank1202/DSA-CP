'''Problem Link:
https://leetcode.com/problems/binary-tree-preorder-traversal/description/
'''

class Node:
    def __init__(self, val):
        self.data= val
        self.left= None
        self.right= None


def preorder(root, arr):

    if not root:
        return

    arr.append(root.data)
    preorder(root.left, arr)
    preorder(root.right, arr)


def preorederTraverse(root):

    arr= []

    preorder(root, arr)

    return arr

if __name__== "__main__":
    root= Node(1)
    root.left= Node(2)
    root.right= Node(3)
    root.left.left= Node(4)
    root.left.right= Node(5)

    result= preorederTraverse(root)

    print("Preorder Traversal :", end=" ")
    for val in result:
        print(val, end=" ")
    print()
