from binary_search_tree import BinarySearchTree, isValidNode

def levelOrder(root):
    nodes = [root]
    ordered_nodes = [root.info]

    while len(nodes) > 0:
        node = nodes[0]
        for child in [node.left, node.right]:
            if isValidNode(child):
                ordered_nodes.append(child.info)
                nodes.append(child)
        nodes = nodes[1:]
    print(' '.join(str(n) for n in ordered_nodes))

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)