'''Problem Linke
https://leetcode.com/problems/binary-tree-inorder-traversal/description/
'''

class Node:
    def __init__(self, val):
        self.data= val
        self.left= None
        self.right= None


def inorder(root, arr):

    if not root:
        return


    inorder(root.left, arr)
    arr.append(root.data)
    inorder(root.right, arr)


def inorederTraverse(root):

    arr= []

    inorder(root, arr)

    return arr

if __name__== "__main__":
    root= Node(1)
    root.left= Node(2)
    root.right= Node(3)
    root.left.left= Node(4)
    root.left.right= Node(5)

    result= inorederTraverse(root)

    print("Inorder Traversal :", end=" ")
    for val in result:
        print(val, end=" ")
    print()
