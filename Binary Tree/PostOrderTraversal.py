'''Problem Link
https://leetcode.com/problems/binary-tree-postorder-traversal/
'''

class Node:
    def __init__(self, val):
        self.data= val
        self.left= None
        self.right= None


def postorder(root, arr):

    if not root:
        return

    arr.append(root.data)
    postorder(root.left, arr)
    postorder(root.right, arr)


def postorederTraverse(root):

    arr= []

    postorder(root, arr)

    return arr

if __name__== "__main__":
    root= Node(1)
    root.left= Node(2)
    root.right= Node(3)
    root.left.left= Node(4)
    root.left.right= Node(5)

    result= postorederTraverse(root)

    print("Postorder Traversal :", end=" ")
    for val in result:
        print(val, end=" ")
    print()
