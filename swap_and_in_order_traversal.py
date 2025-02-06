import sys
from binary_search_tree import Node
from collections import deque
sys.setrecursionlimit(2000)

''' 
when building the tree for this problem, the root is always 1
and we buils the rest of the tree using the indexes entries
'''
def buildTree(indexes):
    root = Node(1)
    nodes = deque([root])
    for left, right in indexes:
        node = nodes.popleft()
        if left != -1:
            node.left = Node(left)
            nodes.append(node.left)
        if right != -1:
            node.right = Node(right)
            nodes.append(node.right)
    return root

'''
only swaps left and right children if the node height is a multiple of k
that is why we need to keep sending the node height
we receive in order traversal because we need to append values on it on the recursive calls
'''
def swapIfNeeded(node, k, node_height, in_order_traversal):
    if node:
        if node_height%k == 0:
            node.swapNodes()
        swapIfNeeded(node.left, k, node_height+1, in_order_traversal)
        in_order_traversal.append(node)
        swapIfNeeded(node.right, k, node_height+1, in_order_traversal)
    return node

def swapNodes(indexes, queries):
    root = buildTree(indexes)
    
    result = []
    for q in queries:
        in_order_traversal = []
        root = swapIfNeeded(root, q, 1, in_order_traversal)
        result.append(in_order_traversal)
        
    return result

if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
