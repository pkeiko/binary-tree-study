
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def isValidNode(node):
    return node is not None

''' Version 1 
    Checks the height of the tree by iterating through the nodes in each level
    and storing the next level nodes in a list.
    If the next level nodes list is not empty, it means that there are more levels to check,
    so it increments the max_depth and updates the depth_nodes list with the next level nodes.
    If the next level nodes list is empty, it means that there are no more levels to check,
    so it returns the max_depth.
'''
def height_version_1(root):
    depth_nodes = [root]
    max_depth = 0
    while len(depth_nodes) > 0:
        next_depth_nodes = []
        for node in depth_nodes:
            next_depth_nodes += [n for n in [node.left, node.right] if isValidNode(n)]
        if len(next_depth_nodes) > 0:
            max_depth += 1
            depth_nodes = next_depth_nodes
        else:
            return max_depth

''' Version 2
    Checks the height of the tree by recursively checking the left and right subtrees
    and adding 1 to the height of the current node.
    If the current node has no left or right child (is a leaf), it returns 0.
    If the current node has a left child or right child,
    it returns the biggest height between them and adds 1 to it.
'''
def height_version_2(root):
    leftHeight = 0
    rightHeight = 0
    if(root.left):            
        leftHeight = height_version_2(root.left) + 1 
    if(root.right):
        rightHeight = height_version_2(root.right) + 1        
    if( leftHeight > rightHeight ):
        return leftHeight
    else:
        return rightHeight

''' Version 3
    Checks the height of the tree by recursively checking the left and right subtrees
    If the current node has no left or right child (is a leaf), it returns 0.
    If the current node has a left child or right child,
    it returns the biggest height between them and adds 1 to it.
    similar to version 2 but with a more concise code.
'''
def height_verison_3(root):
    if (root.left is None and root.right is None):
        return 0
    else:
        if root.left is None:
            return height_verison_3(root.right)+1
        elif root.right is None:
            return height_verison_3(root.left)+1
        else:
            return max(height_verison_3(root.right), height_verison_3(root.left))+1
            
''' Version 4
    Similar to previous versions but instead of checking if the node is a leaf,
    it checks if the node comes after a leaf (is None) and gives it a height of -1.
    this way the leaf node will have a height of 0 and the root node will have the height of the tree.
    This approach results in a cleaner code since it doesn't check each node's right and left children.
''' 
def height_version_4(root):
    if root is None:
        return -1
    return max(height_version_4(root.right), height_version_4(root.left))+1


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height_version_4(tree.root))