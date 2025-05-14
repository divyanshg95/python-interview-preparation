from typing import Optional

class Node:
    def __init__(self, key : int = None, left  = None, right = None):
       self.key = key
       self.left = left 
       self.right = right


# insert operation will take O(h) time and space 
# in worst case the h of BST can be n and time 
# taken can be O(n)
# instead of taking recursive approach you can also take 
# iterative appraoch check reference for that
def insert(root: Node, key: int): 
    if root is None: 
        return Node(key)
    
    # assuming the each node in tree is unique
    if root.key == key:
        return root
    if root.key < key: 
        root.right = insert(root.right, key)
    else: 
        root.left = insert(root.left, key)

    return root 

# preorder traversal root, left, right 
# complexity : time O(n), space : O(h)
def preorder(root): 
    if root is None:
        return 
    print(root.key, end=", ")
    preorder(root.left)
    preorder(root.right)

# inorder traversal left, root, right 
# complexity : time O(n), space : O(h)
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.key, end=",")
    inorder(root.right)

# postorder traversal: 
# complexity : time O(n), space : O(h)
def postorder(root):
    if root is None:
        return
    print(root.key, end=", ")
    postorder(root.right)
    postorder(root.left)
    


# search a given a key and root node search the key 
# Complexity : Time: O(h), Space: O(h)
def search(root, key): 
    if root is None or root.key == key:
        return root
    elif key < root.key: 
       return search(root.left, key)
    else: 
        return search(root.right, key)


# this is no-generic successor method 
# it finds the successor node for a given root 
# node more precisely it look in the right subtree
# and find the left most node
def successor(root): 
    if root is None or root.right is None:
        return None
    root = root.right
    while root.left is not None:
        root = root.left
    return root
        

# deletion 
# case 1: node does not have any child delete the node 
# case 2: node has one child delete the node and replace with child 
# case 3: node has two child, replace the node with successor and delete 
#         successor node
# Complexity: O(h), O(h)
# you have to carefully notice that when we move to left 
def delete(root, key):
    if root is None: 
        return None 
    
    if key < root.key:
        root.left =  delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:

        if root.left is None:
            return root.right 
        if root.right is None: 
            return root.left 
        
        # when both children are present 
        succ = successor(root)
        root.key = succ.key 
        root.right = delete(root.right, succ.key)
    
    return root 

# left most child from root whose left is NULL
def minimum(root): 
    if root is None: 
        return None 
    
    ##left most child will be minimum 
    while root.left: 
        root = root.left 
    
    return root

def maximum(root):
    if root is None:
        return None 
    #right most chile 
    while root.right: 
        root = root.right

    return root


# return the left most child in a tree 
def leftMost(root):
    if root == None: 
        return root 
    while root.left:
        root = root.left

    
    

# Given a root of tree and a general node find inorder successor.
# Inorder successor of a node is node which which comes next in the inorder 
# traversal BST 
# Solution 1. We can perform inorder traversal and just print next node O(n)
# Solution 2: If parent reference is present then it can be easy. You can later explore this 
#             in detail 
# Solution 3: We can find based on BST property in O(h) time  
def inorder_sucessor(root, target): 
    if root is None or root.right == None:
        return None 
    # if key matches the root then success whille be the left most node 
    # in right subtree
    if root.key == target:
        leftMost(root.right)
    else:
        succ = None
        curr = root

        while curr is not None: 
            if target < curr.key:
                succ = curr
                curr = curr.left 
            else: 
               curr = curr.right  

    return succ 


if __name__ == "__main__":
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)

    # Creating the following BST
    #      50
    #     /  \
    #    30   70
    #   / \   / \
    #  20 40 60 80

    # traversal 
    print("inorder", end=": ")
    inorder(r), print()
    print("preorder", end=": ")
    preorder(r), print()
    print("postorder", end=": ")
    postorder(r), print()

    def printS(result):
        if result == None:
            return "NA"
        else:
            return result.key
    

    # searching 
    
    print("searching 20.. result", printS(search(r,20)))
    print("searching 30.. result",printS(search(r,30)))
    print("searching 70.. result ", printS(search(r, 70)))
    print("searching 40.. result ",printS(search(r, 40)))
    print("searching 90.. result ",printS(search(r, 99)))

    print("deleting 30")
    delete(r, 30)
    inorder(r)
    print()
    print("deleting 50")
    delete(r,50)
    inorder(r)
    print()
    
    print("minimum of tree ", printS(minimum(r)))
    print("maximum of tree ", printS(maximum(r)))







            



    












    
