"""Properties :
1. Keys and Values (also called map or treemap)
2. Binary Search Tree: The left subtree of any node only contains nodes with keys that are lexicographically smaller
than the node's key, and the right subtree of any node only contains nodes with keys that lexicographically larger 
than the node's key
3. Balanced Tree: it does not skew too heavily to one side or the other

For a tree of height k, here's a list of the number of nodes at each level:
Level 0: 1
Level 1: 2
Level 2: 4 i.e. 2^2
Level 3: 8 i.e. 2^3
...
Level k-1: 2^(k-1)
"""

class TreeNode:
    def __init__(self,data) -> None:
        self.key = data
        self.left = None
        self.right = None

# Create basic tree using above class and print its values
def basic_tree():
    node0 = TreeNode(3)
    node1 = TreeNode(4)
    node2 = TreeNode(5)

    node0.left = node1  # Left node
    node0.right = node2     # Right node
    tree = node0        # Root node with left and right subtrees
    print(tree)
    print(tree.left.key, tree.key, tree.right.key)

#basic_tree()


# Exercise: Create the following binary tree using the TreeNode class defined above.(Tree mentioned as form of tree_tuple)
# Tree diagram here : https://jovian.com/aakashns/python-binary-search-trees/v/19#C91
def parse_tuple(element):
    #print(type(element))
    node = None
    if(type(element) == tuple and len(element) == 3):
        node = TreeNode(element[1])
        node.left = parse_tuple(element[0])
        node.right = parse_tuple(element[2])
    elif element is None:   #Single element None
        pass
    else:   #Single element node with some value
        node = TreeNode(element)
    return node

tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree = parse_tuple(tree_tuple)

def complex_binary_tree():
    print(tree.key, tree.left.key, tree.right.key) #This way you can print all its values

#complex_binary_tree()

# Tree traversal - every node is visited only once(Put visited node in a list for tracking)
# Inorder traversal - 1. Traverse left subtree recursively inorder, 2. Traverse current/root node, 3. Traverse right subtree recursively inorder
'''Input : tree
Output : [1, 3, 2, 3, 4, 5, 6, 7, 8]'''
def traverse_inorder(node):
    traverse_list = []
    #print(node.left.key)
    if(node is None):
        print("None")
        #traverse_list = []
    else:
        print("tuple")
        traverse_list = traverse_inorder(node.left) + [node.key] + traverse_inorder(node.right)
    return traverse_list

inorder_list = traverse_inorder(tree)
print(inorder_list)

# Traverse Preorder(Root first) - 1. Traverse current node, 2. Traverse left subtree recursively preorder, 3. Traverse right subtree recursively preorder
'''Input = tree object
Output = [2, 3, 1, 5, 3, 4, 7, 6, 8]'''
def traverse_preorder(node):
    traverse_list = []
    if node is None:
        traverse_list = []
    else:
        traverse_list = [node.key] + traverse_preorder(node.left) + traverse_preorder(node.right)
    return traverse_list
preorder_list = traverse_preorder(tree)
print(preorder_list)

# Traverse Postorder(Root last)- 1. Traverse left subtree in postorder recursively, 2. Traverse Right subtree in postorder recursively, 3. Traverse current/root node
'''Input = tree object
Output = [1, 3, 4, 3, 6, 8, 7, 5, 2]'''
def traverse_postorder(node):
    traverse_list = []
    if node is None:
        traverse_list = []
    else:
        traverse_list = traverse_postorder(node.left) + traverse_postorder(node.right) + [node.key]
    return traverse_list
postorder_list = traverse_postorder(tree)
print(postorder_list)

