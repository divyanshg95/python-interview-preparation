import queue

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

class Tree:
    def __init__(self) -> None:
        self.root = None
    
    #Insert at the last level 
    def insert(self, val) -> None:
        n = Node(val)
        if self.root is None:
            self.root = n
        else:
            q = queue.Queue()
            q.put(self.root) 
            inserted = False
            while not q.empty() and not inserted:
                node = q.get()
                if node.left is None:
                    node.left = n
                    inserted = True
                elif node.right is None:
                    node.right = n
                    inserted = True
                else:
                    q.put(node.left)
                    q.put(node.right)
           
                     
    def pre_order_traversal_helper(self, root):
        if root == None:
            return 
        else:
            print(root.val, end = " ")
            self.pre_order_traversal_helper(root.left)
            self.pre_order_traversal_helper(root.right)
        

    def pre_order_traversal(self) -> None:
        print("Pre-order : ", end = " ")
        self.pre_order_traversal_helper(self.root)
        print("")

    def post_order_traversal_helper(self, root):
        if root == None:
            return 
        else: 
            print(root.val, end = " ")
            self.post_order_traversal_helper(root.right)
            self.post_order_traversal_helper(root.left)
        
    
    def post_order_traversal(self):
        print("Post-order : ", end = " ")
        self.post_order_traversal_helper(self.root)
        print("")
        
    def in_order_traversal_helper(self, root):
        if root is None:
            return 
        else:
            self.in_order_traversal_helper(root.left) 
            print(root.val, end =" ")
            self.in_order_traversal_helper(root.right)     
        
    
    def in_order_traversal(self) -> None:
        print("In-order : ", end = " ")
        self.in_order_traversal_helper(self.root)
        print("")

    def level_order_traversal(self) -> None:
        if self.root is None:
            return 
        else:
            q = queue.Queue()
            q.put(self.root)
            while not q.empty():
                node = q.get()
                print(node.val, end=" ")
                if node.left != None:
                    q.put(node.left)
                elif node.right != None: 
                    q.put(node.right)
        print("")
        
    def serachDFS_helper(self, root, val) -> bool:
        if root is None:
            return False
        else:
            if root.val == val:
                return True
            else:
                return self.serachDFS_helper(root.left, val) or self.serachDFS_helper(root.right, val) 
        print("")    


def main():
    t = Tree()     
    t.insert(10)
    t.insert(12)
    t.insert(13)  
    t.insert(14)  
    t.level_order_traversal()
    t.pre_order_traversal()
    t.post_order_traversal()
    t.in_order_traversal()
    

if __name__ == "__main__":
    main()

        